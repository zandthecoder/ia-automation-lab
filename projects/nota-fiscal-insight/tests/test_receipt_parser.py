import json
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.receipt_parser import ReceiptValidationError, parse_receipt


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
INVALID_LINE_TOTAL_FIXTURE_PATH = (
    PROJECT_ROOT / "fixtures" / "inputs" / "invalid_line_total.txt"
)
INVALID_RECEIPT_TOTAL_FIXTURE_PATH = (
    PROJECT_ROOT / "fixtures" / "inputs" / "invalid_receipt_total.txt"
)
INVALID_MISSING_ITEM_FIXTURE_PATH = (
    PROJECT_ROOT / "fixtures" / "inputs" / "invalid_missing_item.txt"
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


def test_reject_inconsistent_line_total():
    raw_text = INVALID_LINE_TOTAL_FIXTURE_PATH.read_text(encoding="utf-8")

    with pytest.raises(ReceiptValidationError) as exc_info:
        parse_receipt(raw_text)

    error = exc_info.value

    assert error.code == "line_total_mismatch"
    assert error.line_number == 3
    assert isinstance(error.message, str)
    assert error.message.strip() != ""


def test_reject_inconsistent_receipt_total():
    raw_text = INVALID_RECEIPT_TOTAL_FIXTURE_PATH.read_text(encoding="utf-8")

    with pytest.raises(ReceiptValidationError) as exc_info:
        parse_receipt(raw_text)

    error = exc_info.value

    assert error.code == "receipt_total_mismatch"
    assert error.line_number == 5
    assert isinstance(error.message, str)
    assert error.message.strip() != ""


def test_reject_receipt_without_items():
    raw_text = INVALID_MISSING_ITEM_FIXTURE_PATH.read_text(encoding="utf-8")

    with pytest.raises(ReceiptValidationError) as exc_info:
        parse_receipt(raw_text)

    error = exc_info.value

    assert error.code == "missing_item"
    assert isinstance(error.message, str)
    assert error.message.strip() != ""
