"""
Script for extracting data from the Google Sheets API. 

Data is requested, and then stored onto a JSON file, before the transformation phase. 
As the ETL pipeline runs every 24 hours, only records less than 24 hours old will 
be stored in the JSON file.
"""

from os import environ as ENV
from datetime import datetime, timedelta
import json
import requests

from dotenv import load_dotenv
from psycopg2 import connect
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection


def filter_out_records_older_than_24hrs(input_records: list[list[str]]) -> list[list[str]]:
    """
    Given a list of lists, where each embedded list has a 1st element of a 
    timestamp, returns the list of lists, but only containing lists with a timestamp
    within the last 24 hours.
    """

    for record in input_records:
        record_timestamp = datetime.


def input_api_data_into_json_file(url: str, json_filename: str = "data.json") -> None:
    """Given the URL of an API endpoint, it takes the response and writes it into
    a JSON file of a given name."""

    pass

    # response = requests.get(url)

    # if response.status_code == 200:
    #     new_data = response.json()

    #     try:
    #         with open(json_filename, "r") as json_file:
    #             existing_data = json.load(json_file)
    #     except FileNotFoundError:
    #         existing_data = []

    #     existing_data.append(new_data)

    #     with open(json_filename, "w") as json_file:
    #         json.dump(existing_data, json_file, indent=4)

    # else:
    #     print("Failed to retrieve data from the API. Status code:",
    #           response.status_code)


if __name__ == "__main__":

    load_dotenv()

    api_url = f"https://sheets.googleapis.com/v4/spreadsheets/{ENV['SPREADSHEET_ID']}/values/{ENV['SPREADSHEET_RANGE']}?key={ENV['API_KEY']}"

    input_api_data_into_json_file(api_url, "data.json")
