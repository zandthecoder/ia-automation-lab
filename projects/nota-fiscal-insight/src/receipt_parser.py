from decimal import Decimal


def parse_receipt(raw_text: str) -> dict:
    lines = raw_text.splitlines()

    merchant_name = lines[0].removeprefix("MERCHANT:").strip()
    purchase_date = lines[1].removeprefix("DATE:").strip()

    item_fields = lines[2].removeprefix("ITEM:").split("|")
    description, quantity, unit_price, line_total = (
        field.strip() for field in item_fields
    )

    receipt_total = lines[3].removeprefix("TOTAL:").strip()

    decimal_line_total = Decimal(line_total)
    if Decimal(quantity) * Decimal(unit_price) != decimal_line_total:
        raise ValueError("Item line total does not match quantity and unit price.")

    if decimal_line_total != Decimal(receipt_total):
        raise ValueError("Receipt total does not match the item total.")

    return {
        "merchant": {"name": merchant_name},
        "purchase_date": purchase_date,
        "items": [
            {
                "description": description,
                "quantity": quantity,
                "unit_price": unit_price,
                "line_total": line_total,
            }
        ],
        "receipt_total": receipt_total,
    }
