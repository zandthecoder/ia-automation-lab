from decimal import Decimal


def parse_receipt(raw_text: str) -> dict:
    lines = raw_text.splitlines()

    merchant_name = lines[0].removeprefix("MERCHANT:").strip()
    purchase_date = lines[1].removeprefix("DATE:").strip()

    items = []
    calculated_receipt_total = Decimal("0")

    for item_line in lines[2:-1]:
        item_fields = item_line.removeprefix("ITEM:").split("|")
        description, quantity, unit_price, line_total = (
            field.strip() for field in item_fields
        )

        decimal_line_total = Decimal(line_total)
        if Decimal(quantity) * Decimal(unit_price) != decimal_line_total:
            raise ValueError("Item line total does not match quantity and unit price.")

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
