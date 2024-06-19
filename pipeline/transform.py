"""Given our extracted data in the JSON file, we will aim to"""

from datetime import datetime, timedelta


def filter_records_older_24hrs(input_records: list[list[str]]) -> list[list[str]]:
    """
    Given a list of lists, where each embedded list has a 1st element of a 
    timestamp, returns the list of lists, but only containing lists with a timestamp
    within the last 24 hours.
    """

    result = []

    n = datetime.now()

    delta = timedelta(days=1)

    for record in input_records:
        record_dt_str = record[0]
        record_timestamp = datetime.strptime(
            record_dt_str, "%d/%m/%Y %H:%M:%S")

        if n - record_timestamp <= delta:
            result.append(record_timestamp)

    return result
