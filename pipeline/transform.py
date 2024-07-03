"""Given our extracted data in the JSON file, we will aim to clean the data,
and acquire the relevant parts of the data, ready to load into our database."""

from datetime import datetime, timedelta
import json


def get_user_records(json_filename: str) -> list[list]:
    """Given the name of the JSON file, returns the user entry data."""
    pass


def filter_records_older_24hrs(input_records: list[list[str]]) -> list[int]:
    """
    Given a list of lists, where each embedded list has a first element of a 
    timestamp, returns the list of lists, but only containing indices of lists with 
    a timestamp within the last 24 hours.
    """
    n = datetime.today()


def make_emotions_list(input_records: list[list[str]]) -> list[list]:
    """Given our user records, where each embedded list has a 6th element containing
    a string with commas separating each substring,

    "Happiness, Hope, Joy, Contentment, Sadness"

    return the records, so that the 6th element of each embedded list is a list[str]
    object.
    """
    pass


def make_all_scores_ints(input_records: list[list[str]]) -> list[list]:
    """Given our user records, we turn each numeric string entry in each embedded
    list into an int object."""
    pass


def check_for_empty_entries(input_records: list[list]) -> list[list]:
    """Given our user records, we turn each empty string in each embedded object
    into None."""
    pass


if __name__ == "__main__":
    pass
