from decimal import Decimal


class ReceiptValidationError(Exception):
    def __init__(
        self,
        code: str,
        message: str,
        line_number: int | None = None,
    ) -> None:
        self.code = code
        self.message = message
        self.line_number = line_number
        super().__init__(message)


def parse_receipt(raw_text: str) -> dict:
    normalized_lines: list[tuple[int, str]] = []

    for line_number, raw_line in enumerate(raw_text.splitlines(), start=1):
        normalized_line = raw_line.strip()

        if normalized_line:
            normalized_lines.append((line_number, normalized_line))

    merchant_line_number, merchant_line = normalized_lines[0]
    date_line_number, date_line = normalized_lines[1]
    total_line_number, total_line = normalized_lines[-1]

    if not merchant_line.startswith("MERCHANT:"):
        raise ReceiptValidationError(
            code="invalid_record_order",
            message=(
                "Record is out of order; expected MERCHANT "
                f"on line {merchant_line_number}."
            ),
            line_number=merchant_line_number,
        )

    if not date_line.startswith("DATE:"):
        raise ReceiptValidationError(
            code="invalid_record_order",
            message=(
                "Record is out of order; expected DATE "
                f"on line {date_line_number}."
            ),
            line_number=date_line_number,
        )

    if not total_line.startswith("TOTAL:"):
        raise ReceiptValidationError(
            code="invalid_record_order",
            message=(
                "Record is out of order; expected TOTAL "
                f"on line {total_line_number}."
            ),
            line_number=total_line_number,
        )

    for line_number, item_line in normalized_lines[2:-1]:
        if not item_line.startswith("ITEM:"):
            raise ReceiptValidationError(
                code="invalid_record_order",
                message=f"Record is out of order; expected ITEM on line {line_number}.",
                line_number=line_number,
            )

    merchant_name = merchant_line.removeprefix("MERCHANT:").strip()
    purchase_date = date_line.removeprefix("DATE:").strip()

    items = []
    calculated_receipt_total = Decimal("0")

    for line_number, item_line in normalized_lines[2:-1]:
        item_fields = item_line.removeprefix("ITEM:").split("|")
        description, quantity, unit_price, line_total = (
            field.strip() for field in item_fields
        )

        decimal_quantity = Decimal(quantity)
        decimal_unit_price = Decimal(unit_price)
        decimal_line_total = Decimal(line_total)
        expected_line_total = decimal_quantity * decimal_unit_price

        if expected_line_total != decimal_line_total:
            raise ReceiptValidationError(
                code="line_total_mismatch",
                message=(
                    "Item line total does not match quantity multiplied by unit price."
                ),
                line_number=line_number,
            )

        items.append(
            {
                "description": description,
                "quantity": quantity,
                "unit_price": unit_price,
                "line_total": line_total,
            }
        )
        calculated_receipt_total += decimal_line_total

    if not items:
        raise ReceiptValidationError(
            code="missing_item",
            message="Receipt must contain at least one item.",
        )

    receipt_total = total_line.removeprefix("TOTAL:").strip()
    decimal_receipt_total = Decimal(receipt_total)

    if calculated_receipt_total != decimal_receipt_total:
        raise ReceiptValidationError(
            code="receipt_total_mismatch",
            message="Receipt total does not match the sum of item totals.",
            line_number=total_line_number,
        )

    return {
        "merchant": {"name": merchant_name},
        "purchase_date": purchase_date,
        "items": items,
        "receipt_total": receipt_total,
    }
