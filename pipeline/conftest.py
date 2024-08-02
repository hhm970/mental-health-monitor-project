"""Conftest file for tests in pipeline directory."""

import datetime

import pytest


FAKE_TODAY = datetime.datetime(year=2024, month=7, day=4)

# Fixtures for test_extract.py


@pytest.fixture
def example_sheets_api_response():
    """Example response from Google Sheets API."""
    return {"range": "responses!A1:S104",
            "majorDimension": "ROWS",
            "values": [
                [
                    "Timestamp",
                    "On a scale of 1 to 10, please rate how well you slept last night.",
                    "On a scale of 1 to 10, please rate how hydrated you were today.",
                    "On a scale of 1 to 10, please rate your quality of food consumption today.",
                    "On a scale of 1 to 10, please rate your quantity of exercise today.",
                    "On a scale of 1 to 10, please rate how stressed you felt today.",
                    "On a scale of 1 to 10, please rate how lonely you felt today",
                    "On a scale of 1 to 10, please rate how happy you felt today",
                    "On a scale of 1 to 10, please rate your overall mental health today",
                    "Are there any other thoughts on your day that you want to share with us?",
                    "Email address"
                ],
                [
                    "12/06/2024 13:02:29",
                    "8",
                    "8",
                    "6",
                    "8",
                    "Happiness, Hope, Joy, Contentment, Sadness",
                    "7",
                    "10",
                    "9",
                    "9",
                    "I felt scared",
                    "howardppg@gmail.com"
                ],
                [
                    "12/06/2024 15:07:39",
                    "",
                    "",
                    "",
                    "",
                    "Happiness",
                    "1",
                    "1",
                    "4",
                    "4",
                    "I had a bad day",
                    "howard-haw-xuen.man@sigmalabs.co.uk"
                ]
            ]
            }


@pytest.fixture
def empty_sheets_api_response():
    """Case for when the response from Google Sheets API is empty."""
    return {}


# Fixtures for test_transform.py

@pytest.fixture
def example_extracted_json():
    """Example JSON data after extraction process."""
    return [
        {
            "range": "responses!A1:S104",
            "majorDimension": "ROWS",
            "values": [
                [
                    "Timestamp",
                    "On a scale of 1 to 10, please rate how well you slept last night.",
                    "On a scale of 1 to 10, please rate how hydrated you were today.",
                    "On a scale of 1 to 10, please rate your quality of food consumption today.",
                    "Please tick all emotions that you experienced today.",
                    "On a scale of 1 to 10, please rate how stressed you felt today.",
                    "On a scale of 1 to 10, please rate how lonely you felt today",
                    "On a scale of 1 to 10, please rate how happy you felt today",
                    "On a scale of 1 to 10, please rate your overall mental health today",
                    "Are there any other thoughts on your day that you want to share with us?",
                    "Email address"
                ],
                [
                    "12/06/2024 13:02:29",
                    "8",
                    "8",
                    "6",
                    "8",
                    "Happiness, Hope, Joy, Contentment, Sadness",
                    "7",
                    "10",
                    "9",
                    "9",
                    "I felt scared",
                    "howardppg@gmail.com"
                ],
                [
                    "12/06/2024 15:07:39",
                    "",
                    "",
                    "",
                    "",
                    "Happiness",
                    "1",
                    "1",
                    "4",
                    "4",
                    "I had a bad day",
                    "howard-haw-xuen.man@sigmalabs.co.uk"
                ],
                [
                    "19/06/2024 14:47:44",
                    "8",
                    "6",
                    "10",
                    "4",
                    "Happiness, Love, Hope, Compassion, Interest, Sadness, Disappointment",
                    "6",
                    "5",
                    "9",
                    "6",
                    "",
                    "howard-haw-xuen.man@sigmalabs.co.uk"
                ]
            ]
        }
    ]


@pytest.fixture
def all_optional_responses_empty_json():
    """Case when the extracted JSON data has all optional responses as empty."""
    return [
        {
            "range": "responses!A1:S105",
            "majorDimension": "ROWS",
            "values": [
                [
                    "Timestamp",
                    "On a scale of 1 to 10, please rate how well you slept last night.",
                    "On a scale of 1 to 10, please rate how hydrated you were today.",
                    "On a scale of 1 to 10, please rate your quality of food consumption today.",
                    "Please tick all emotions that you experienced today.",
                    "On a scale of 1 to 10, please rate how stressed you felt today.",
                    "On a scale of 1 to 10, please rate how lonely you felt today",
                    "On a scale of 1 to 10, please rate how happy you felt today",
                    "On a scale of 1 to 10, please rate your overall mental health today",
                    "Are there any other thoughts on your day that you want to share with us?",
                    "Email address"
                ],
                [
                    "03/07/2024 16:06:29",
                    "",
                    "",
                    "",
                    "",
                    "Happiness",
                    "",
                    "",
                    "10",
                    "10",
                    "",
                    "howard-haw-xuen.man@sigmalabs.co.uk"
                ]
            ]
        }
    ]


@pytest.fixture
def no_responses_json():
    """Extracted JSON data where no user responses are extracted."""
    return [
        {
            "range": "responses!A1:S105",
            "majorDimension": "ROWS",
            "values": [
                [
                    "Timestamp",
                    "On a scale of 1 to 10, please rate how well you slept last night.",
                    "On a scale of 1 to 10, please rate how hydrated you were today.",
                    "On a scale of 1 to 10, please rate your quality of food consumption today.",
                    "On a scale of 1 to 10, please rate your quantity of exercise today.",
                    "Please tick all emotions that you experienced today.",
                    "On a scale of 1 to 10, please rate how stressed you felt today.",
                    "On a scale of 1 to 10, please rate how lonely you felt today",
                    "On a scale of 1 to 10, please rate how happy you felt today",
                    "On a scale of 1 to 10, please rate your overall mental health today",
                    "Are there any other thoughts on your day that you want to share with us?",
                    "Email address"
                ]
            ]
        }
    ]


@pytest.fixture
def example_user_records():
    """Example user JSON data."""
    return [
        [
            "12/06/2024 13:02:29",
            "8",
            "8",
            "6",
            "8",
            "Happiness, Hope, Joy, Contentment, Sadness",
            "7",
            "10",
            "9",
            "9",
            "I felt scared",
            "howardppg@gmail.com"
        ],
        [
            "12/06/2024 15:07:39",
            "",
            "",
            "",
            "",
            "Happiness",
            "1",
            "1",
            "4",
            "4",
            "I had a bad day",
            "howard-haw-xuen.man@sigmalabs.co.uk"
        ],
        [
            "19/06/2024 14:47:44",
            "8",
            "6",
            "10",
            "4",
            "Happiness, Love, Hope, Compassion, Interest, Sadness, Disappointment, Frustration",
            "6",
            "5",
            "9",
            "6",
            "",
            "howard-haw-xuen.man@sigmalabs.co.uk"
        ],
        [
            "03/07/2024 16:06:29",
            "",
            "",
            "",
            "",
            "Happiness",
            "",
            "",
            "10",
            "10",
            "",
            "howard-haw-xuen.man@sigmalabs.co.uk"
        ]
    ]


@pytest.fixture
def example_user_records_no_emotions():
    """
    Extracted JSON data where empty entries have been formatted for,
    and the user has not inputted any emotions.
    """
    return [
        [
            "12/06/2024 13:02:29",
            "8",
            "8",
            "6",
            "8",
            "",
            "7",
            "10",
            "9",
            "9",
            "I felt scared",
            "howardppg@gmail.com"
        ],
        [
            "12/06/2024 15:07:39",
            "",
            "",
            "",
            "",
            "",
            "1",
            "1",
            "4",
            "4",
            "I had a bad day",
            "howard-haw-xuen.man@sigmalabs.co.uk"
        ],
        [
            "19/06/2024 14:47:44",
            "8",
            "6",
            "10",
            "4",
            "",
            "6",
            "5",
            "9",
            "6",
            "",
            "howard-haw-xuen.man@sigmalabs.co.uk"
        ],
        [
            "03/07/2024 16:06:29",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "10",
            "10",
            "",
            "howard-haw-xuen.man@sigmalabs.co.uk"
        ]
    ]


@pytest.fixture
def no_user_records():
    """Extracted JSON data where no data is present."""
    return []


@pytest.fixture
def user_record_all_optional_qs_blank():
    """Extracted JSON data where the user does not answer optional questions."""
    return [
        [
            "03/07/2024 16:06:29",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "10",
            "10",
            "",
            "howard-haw-xuen.man@sigmalabs.co.uk"
        ]
    ]


@pytest.fixture
def patch_datetime_now(monkeypatch):
    """Creates a fake datetime object to replace datetime.datetime.now()"""

    class MyDatetime(datetime.datetime):
        """Used to mock datetime object for test_transform.py"""
        @classmethod
        def now(cls):
            return FAKE_TODAY

    monkeypatch.setattr(datetime, 'datetime', MyDatetime)
