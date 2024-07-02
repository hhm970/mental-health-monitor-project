"""Tests for extract.py"""

from unittest.mock import MagicMock, patch, mock_open

from extract import get_sheets_api_data, input_api_data_into_json_file


def test_get_sheets_api_data_success(requests_mock, example_sheets_api_response):
    """Tests for a successful GET request to Google Sheets API."""

    config = {"API_KEY": "asdkjasbdlkbaskdbas;",
              "SPREADSHEET_ID": "1qg_1umxZXJiqpZymo1EC8FUWugNGNZJ_liZkJJP2n0w",
              "SPREADSHEET_RANGE": "responses"}

    api_url = f"https://sheets.googleapis.com/v4/spreadsheets/{config['SPREADSHEET_ID']}/values/{config['SPREADSHEET_RANGE']}?key={config['API_KEY']}"

    requests_mock.get(api_url, json=example_sheets_api_response)

    result = get_sheets_api_data(api_url)

    assert isinstance(result, dict)
    assert list(result.keys()) == ["range", "majorDimension", "values"]


def test_get_sheets_api_data_empty_response(requests_mock, empty_sheets_api_response):
    """Tests for a successful GET request when there is no data in the response."""

    config = {"API_KEY": "asdkjasbdlkbaskdbas;",
              "SPREADSHEET_ID": "1qg_1umxZXJiqpZymo1EC8FUWugNGNZJ_liZkJJP2n0w",
              "SPREADSHEET_RANGE": "responses"}

    api_url = f"https://sheets.googleapis.com/v4/spreadsheets/{config['SPREADSHEET_ID']}/values/{config['SPREADSHEET_RANGE']}?key={config['API_KEY']}"

    requests_mock.get(api_url, json=empty_sheets_api_response)

    result = get_sheets_api_data(api_url)

    assert isinstance(result, dict)
    assert list(result.keys()) == []


def test_input_api_data_into_json_file_success(example_sheets_api_response):
    """Tests for a successful writing into a JSON file, given JSON data."""

    mock_file = MagicMock()

    mock_file.name = "mock.json"

    m = mock_open()

    with patch("builtins.open", m):
        input_api_data_into_json_file(
            example_sheets_api_response, mock_file.name)

    m.assert_called_once_with(mock_file.name, 'w')


def test_input_empty_data_into_json(empty_sheets_api_response):
    """Tests that the function input_api_data_into_json_file() returns None
    when given an empty object."""

    json_filename = "mock.json"

    assert input_api_data_into_json_file(
        empty_sheets_api_response, json_filename) is None
