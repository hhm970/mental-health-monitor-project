"""Script for extracting data from the Google Sheets API. Data is requested, and then
stored onto a JSON file, before getting transformed."""

from os import environ as ENV
from datetime import datetime, timedelta
import json
import requests

import pandas as pd
from dotenv import load_dotenv
from psycopg2 import connect
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection


def input_api_data_into_json_file(url: str, json_filename: str = "data.json") -> None:
    """Given the URL of an API endpoint, it takes the response and writes it into
    a JSON file of a given name."""

    response = requests.get(url)

    if response.status_code == 200:
        new_data = response.json()

        try:
            with open(json_filename, "r") as json_file:
                existing_data = json.load(json_file)
        except FileNotFoundError:
            existing_data = []

        existing_data.append(new_data)

        with open(json_filename, "w") as json_file:
            json.dump(existing_data, json_file, indent=4)

    else:
        print("Failed to retrieve data from the API. Status code:",
              response.status_code)


if __name__ == "__main__":

    load_dotenv()

    api_url = f"https://sheets.googleapis.com/v4/spreadsheets/{ENV['SPREADSHEET_ID']}/values/{ENV['SPREADSHEET_RANGE']}?key={ENV['API_KEY']}"

    input_api_data_into_json_file(api_url, "data.json")
