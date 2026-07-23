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
    lines = raw_text.splitlines()

    merchant_name = lines[0].removeprefix("MERCHANT:").strip()
    purchase_date = lines[1].removeprefix("DATE:").strip()

    items = []
    calculated_receipt_total = Decimal("0")

    for line_number, item_line in enumerate(lines[2:-1], start=3):
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

    receipt_total = lines[-1].removeprefix("TOTAL:").strip()
    if calculated_receipt_total != Decimal(receipt_total):
        raise ValueError("Receipt total does not match the sum of item totals.")

    return {
        "merchant": {"name": merchant_name},
        "purchase_date": purchase_date,
        "items": items,
        "receipt_total": receipt_total,
    }
