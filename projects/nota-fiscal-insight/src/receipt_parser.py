from decimal import Decimal, InvalidOperation


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


def _convert_decimal(
    value: str,
    *,
    error_code: str,
    error_message: str,
) -> Decimal:
    try:
        return Decimal(value)
    except InvalidOperation as exc:
        raise ReceiptValidationError(
            code=error_code,
            message=error_message,
        ) from exc


def _parse_item_record(
    line_text: str,
    line_number: int,
) -> tuple[dict[str, str], Decimal]:
    item_fields = [
        field.strip()
        for field in line_text.removeprefix("ITEM:").split("|")
    ]

    if len(item_fields) != 4:
        raise ReceiptValidationError(
            code="invalid_item_format",
            message="ITEM record must contain exactly four fields.",
        )

    description, quantity, unit_price, line_total = item_fields

    if not description:
        raise ReceiptValidationError(
            code="invalid_item_description",
            message="Item description cannot be empty.",
        )

    decimal_quantity = _convert_decimal(
        quantity,
        error_code="invalid_quantity",
        error_message="Quantity has an invalid or unsupported numeric format.",
    )

    whole_unit_price, separator, fractional_unit_price = unit_price.partition(".")

    if (
        not whole_unit_price
        or separator != "."
        or len(fractional_unit_price) != 2
    ):
        raise ReceiptValidationError(
            code="invalid_unit_price",
            message="Unit price must have exactly two decimal places.",
        )

    decimal_unit_price = _convert_decimal(
        unit_price,
        error_code="invalid_unit_price",
        error_message="Unit price has an invalid numeric format.",
    )

    decimal_line_total = _convert_decimal(
        line_total,
        error_code="invalid_line_total",
        error_message="Line total has an invalid numeric format.",
    )

    if decimal_line_total < 0:
        raise ReceiptValidationError(
            code="invalid_line_total",
            message="Line total cannot be negative.",
        )

    expected_line_total = decimal_quantity * decimal_unit_price

    if expected_line_total != decimal_line_total:
        raise ReceiptValidationError(
            code="line_total_mismatch",
            message=(
                "Item line total does not match quantity multiplied by unit price."
            ),
            line_number=line_number,
        )

    item = {
        "description": description,
        "quantity": quantity,
        "unit_price": unit_price,
        "line_total": line_total,
    }

    return item, decimal_line_total


def parse_receipt(raw_text: str) -> dict:
    normalized_lines: list[tuple[int, str]] = []

    for line_number, raw_line in enumerate(raw_text.splitlines(), start=1):
        normalized_line = raw_line.strip()

        if normalized_line:
            normalized_lines.append((line_number, normalized_line))

    if not normalized_lines:
        raise ReceiptValidationError(
            code="empty_input",
            message="Receipt input is empty.",
        )

    merchant_line_number, merchant_line = normalized_lines[0]
    date_line_number, date_line = normalized_lines[1]
    total_line_number, total_line = normalized_lines[-1]
    has_total = total_line.startswith("TOTAL:")
    item_lines = normalized_lines[2:-1] if has_total else normalized_lines[2:]

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

    if not has_total and any(
        not item_line.startswith("ITEM:") for _, item_line in item_lines
    ):
        raise ReceiptValidationError(
            code="invalid_record_order",
            message=(
                "Record is out of order; expected TOTAL "
                f"on line {total_line_number}."
            ),
            line_number=total_line_number,
        )

    for line_number, item_line in item_lines:
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

    for line_number, item_line in item_lines:
        item, decimal_line_total = _parse_item_record(item_line, line_number)

        items.append(item)
        calculated_receipt_total += decimal_line_total

    if not items:
        raise ReceiptValidationError(
            code="missing_item",
            message="Receipt must contain at least one item.",
        )

    if not has_total:
        raise ReceiptValidationError(
            code="missing_total",
            message="Receipt total record is missing.",
        )

    receipt_total = total_line.removeprefix("TOTAL:").strip()

    decimal_receipt_total = _convert_decimal(
        receipt_total,
        error_code="invalid_receipt_total",
        error_message="Receipt total has an invalid numeric format.",
    )

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
