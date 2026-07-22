import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.receipt_parser import parse_receipt


FIXTURE_PATH = PROJECT_ROOT / "fixtures" / "inputs" / "valid_single_item.txt"
EXPECTED_PATH = PROJECT_ROOT / "fixtures" / "expected" / "valid_single_item.json"
MULTIPLE_ITEMS_FIXTURE_PATH = (
    PROJECT_ROOT / "fixtures" / "inputs" / "valid_multiple_items.txt"
)
MULTIPLE_ITEMS_EXPECTED_PATH = (
    PROJECT_ROOT / "fixtures" / "expected" / "valid_multiple_items.json"
)
DECIMAL_QUANTITY_FIXTURE_PATH = (
    PROJECT_ROOT / "fixtures" / "inputs" / "valid_decimal_quantity.txt"
)
DECIMAL_QUANTITY_EXPECTED_PATH = (
    PROJECT_ROOT / "fixtures" / "expected" / "valid_decimal_quantity.json"
)


def test_parse_valid_single_item_receipt():
    raw_text = FIXTURE_PATH.read_text(encoding="utf-8")

    with EXPECTED_PATH.open(encoding="utf-8") as expected_file:
        expected_receipt = json.load(expected_file)

    assert parse_receipt(raw_text) == expected_receipt


def test_parse_multiple_items_preserving_order():
    raw_text = MULTIPLE_ITEMS_FIXTURE_PATH.read_text(encoding="utf-8")

    with MULTIPLE_ITEMS_EXPECTED_PATH.open(encoding="utf-8") as expected_file:
        expected_receipt = json.load(expected_file)

    assert parse_receipt(raw_text) == expected_receipt


def test_parse_decimal_quantity_preserving_lexical_value():
    raw_text = DECIMAL_QUANTITY_FIXTURE_PATH.read_text(encoding="utf-8")

    with DECIMAL_QUANTITY_EXPECTED_PATH.open(encoding="utf-8") as expected_file:
        expected_receipt = json.load(expected_file)

    result = parse_receipt(raw_text)

    assert result == expected_receipt
    assert result["items"][0]["quantity"] == "0.750"
