"""Given our extracted data in the JSON file, we will aim to clean the data,
and acquire the relevant parts of the data, ready to load into our database."""

from datetime import datetime, timedelta
import json


OPTIONAL_ENTRIES_INDICES = {1, 2, 3, 4, 5, 6, 7, 10}

REQUIRED_ENTRIES_INDICES = {8, 9}

NUMERIC_ENTRIES_INDICES = {1, 2, 3, 4, 6, 7, 8, 9}


def get_user_records(json_filename: str) -> list[list]:
    """Given the name of the JSON file, returns the user entry data."""

    with open(json_filename, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    json_data_values = json_data[0]["values"][1:]

    return json_data_values


def filter_records_older_24hrs(input_records: list[list[str]]) -> set[int]:
    """
    Given a list of lists, where each embedded list has a first element of a 
    timestamp, returns the list of lists, but only containing indices of lists with 
    a timestamp from the last 24 hours.
    """

    n = datetime.today()

    delta = timedelta(days=1)

    l = len(input_records)

    result = set()

    for i in range(l):
        record_date = datetime.strptime(
            input_records[i][0], "%d/%m/%Y %H:%M:%S")

        if n - record_date < delta:

            result.add(i)

    return result


def make_emotions_list(input_records: list[list[str]]) -> list[list]:
    """Given our user records, where each embedded list has a 6th element containing
    a string with commas separating each substring,

    "Happiness, Hope, Joy, Contentment, Sadness"

    return the records, so that the 6th element of each embedded list is a list[str]
    object.
    """

    for record in input_records:

        emotions = record[5]

        if emotions is not None:

            record[5] = emotions.split(", ")

    return input_records


def make_all_scores_ints(input_records: list[list[str]]) -> list[list]:
    """Given our user records, we turn each numeric string entry in each embedded
    list into an int object. All numeric string entries are to be taken as None
    for this function."""

    for record in input_records:

        for i in NUMERIC_ENTRIES_INDICES:

            if record[i] is not None:

                record[i] = int(record[i])

    return input_records


def check_for_empty_entries(input_records: list[list]) -> list[list]:
    """Given our user records, we turn each empty string in each embedded object
    into None. If it is a question with a quantitative answer"""

    for record in input_records:

        for i in OPTIONAL_ENTRIES_INDICES:

            if record[i] == "":

                record[i] = None

    return input_records


if __name__ == "__main__":

    record_data = get_user_records("2024-07-10.json")

    indices_24hrs = filter_records_older_24hrs(record_data)

    record_data_24hrs = [record_data[j] for j in indices_24hrs]

    record_data_24hrs_noempty = check_for_empty_entries(record_data_24hrs)

    record_data_24hrs_f_emotions = make_emotions_list(
        record_data_24hrs_noempty)

    record_data_24hrs_formatted = make_all_scores_ints(
        record_data_24hrs_f_emotions)

    print(record_data_24hrs_formatted)
