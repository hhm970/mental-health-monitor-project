"""
Script for extracting data from the Google Sheets API. 

Data is requested, and then stored onto a JSON file, before the transformation phase. 
As the ETL pipeline runs every 24 hours, only records less than 24 hours old will 
be stored in the JSON file.
"""

from os import environ as ENV
from datetime import datetime
import json
import requests

from dotenv import load_dotenv


def get_sheets_api_data(url: str) -> dict:
    """Given the URL of an API endpoint, returns the response as a JSON dict."""

    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        new_data = response.json()
        return new_data

    print("Failed to retrieve data from the API. Status code:",
          response.status_code)


def input_api_data_into_json_file(json_data: dict, json_file: str) -> None:
    """Given a JSON dict object, it writes it into a JSON file of a given name."""

    if len(json_data) == 0:
        return None

    existing_data = []

    existing_data.append(json_data)

    with open(json_file, "w", encoding="utf-8") as g:
        json.dump(existing_data, g, indent=4)


if __name__ == "__main__":

    load_dotenv()

    json_filename = datetime.today().strftime('%Y-%m-%d')

    api_url = f"https://sheets.googleapis.com/v4/spreadsheets/{ENV['SPREADSHEET_ID']}/values/{ENV['SPREADSHEET_RANGE']}?key={ENV['API_KEY']}"

    api_data = get_sheets_api_data(api_url)

    if api_data is not None:
        input_api_data_into_json_file(api_data, f"{json_filename}.json")
