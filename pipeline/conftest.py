"""Conftest file for tests in pipeline directory."""

import datetime

import pytest


FAKE_TODAY = datetime.datetime(year=2024, month=7, day=4)

# Fixtures for test_extract.py


@pytest.fixture
def example_sheets_api_response():
    return {"range": "responses!A1:S104",
            "majorDimension": "ROWS",
            "values": [
                [
                    "Timestamp",
                    "On a scale of 1 to 10, please rate how well you slept last night.\n\nAdults need around 7-9 hours of sleep per night.",
                    "On a scale of 1 to 10, please rate how hydrated you were today.\n\nThe Eatwell Guide recommends that people should aim to drink 6 to 8 cups or glasses of fluid a day. Water, lower-fat milk and sugar-free drinks, including tea and coffee, all count.",
                    "On a scale of 1 to 10, please rate your quality of food consumption today.\n\nA good rule of thumb is to have 3 meals a day (breakfast, lunch, and dinner). See the EatWell Guide for more on nutrition.",
                    "On a scale of 1 to 10, please rate your quantity of exercise today.\n\nThe NHS recommends adults aged 19 - 64 to do at least 150 minutes of moderate intensity activity, or 75 minutes of vigorous intensity activity a week, and spread exercise evenly over 4 to 5 days a week, or every day. See here for ideas on exercises to do.",
                    "Please tick all emotions that you experienced today. If an emotion you experienced does not come up, please insert it into the 'Other' checkbox",
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
    return {}


# Fixtures for test_transform.py

@pytest.fixture
def example_extracted_json():
    return [
        {
            "range": "responses!A1:S104",
            "majorDimension": "ROWS",
            "values": [
                [
                    "Timestamp",
                    "On a scale of 1 to 10, please rate how well you slept last night.\n\nAdults need around 7-9 hours of sleep per night.",
                    "On a scale of 1 to 10, please rate how hydrated you were today.\n\nThe Eatwell Guide recommends that people should aim to drink 6 to 8 cups or glasses of fluid a day. Water, lower-fat milk and sugar-free drinks, including tea and coffee, all count.",
                    "On a scale of 1 to 10, please rate your quality of food consumption today.\n\nA good rule of thumb is to have 3 meals a day (breakfast, lunch, and dinner). See the EatWell Guide for more on nutrition.",
                    "On a scale of 1 to 10, please rate your quantity of exercise today.\n\nThe NHS recommends adults aged 19 - 64 to do at least 150 minutes of moderate intensity activity, or 75 minutes of vigorous intensity activity a week, and spread exercise evenly over 4 to 5 days a week, or every day. See here for ideas on exercises to do.",
                    "Please tick all emotions that you experienced today. If an emotion you experienced does not come up, please insert it into the 'Other' checkbox",
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
                    "Happiness, Love, Hope, Compassion, Interest, Sadness, Disappointment, Frustration",
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
    return [
        {
            "range": "responses!A1:S105",
            "majorDimension": "ROWS",
            "values": [
                [
                    "Timestamp",
                    "On a scale of 1 to 10, please rate how well you slept last night.\n\nAdults need around 7-9 hours of sleep per night.",
                    "On a scale of 1 to 10, please rate how hydrated you were today.\n\nThe Eatwell Guide recommends that people should aim to drink 6 to 8 cups or glasses of fluid a day. Water, lower-fat milk and sugar-free drinks, including tea and coffee, all count.",
                    "On a scale of 1 to 10, please rate your quality of food consumption today.\n\nA good rule of thumb is to have 3 meals a day (breakfast, lunch, and dinner). See the EatWell Guide for more on nutrition.",
                    "On a scale of 1 to 10, please rate your quantity of exercise today.\n\nThe NHS recommends adults aged 19 - 64 to do at least 150 minutes of moderate intensity activity, or 75 minutes of vigorous intensity activity a week, and spread exercise evenly over 4 to 5 days a week, or every day. See here for ideas on exercises to do.",
                    "Please tick all emotions that you experienced today. If an emotion you experienced does not come up, please insert it into the 'Other' checkbox",
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
    return [
        {
            "range": "responses!A1:S105",
            "majorDimension": "ROWS",
            "values": [
                [
                    "Timestamp",
                    "On a scale of 1 to 10, please rate how well you slept last night.\n\nAdults need around 7-9 hours of sleep per night.",
                    "On a scale of 1 to 10, please rate how hydrated you were today.\n\nThe Eatwell Guide recommends that people should aim to drink 6 to 8 cups or glasses of fluid a day. Water, lower-fat milk and sugar-free drinks, including tea and coffee, all count.",
                    "On a scale of 1 to 10, please rate your quality of food consumption today.\n\nA good rule of thumb is to have 3 meals a day (breakfast, lunch, and dinner). See the EatWell Guide for more on nutrition.",
                    "On a scale of 1 to 10, please rate your quantity of exercise today.\n\nThe NHS recommends adults aged 19 - 64 to do at least 150 minutes of moderate intensity activity, or 75 minutes of vigorous intensity activity a week, and spread exercise evenly over 4 to 5 days a week, or every day. See here for ideas on exercises to do.",
                    "Please tick all emotions that you experienced today. If an emotion you experienced does not come up, please insert it into the 'Other' checkbox",
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
def example_user_records_no_emotions_empty_entries_formatted():
    return [
        [
            "12/06/2024 13:02:29",
            "8",
            "8",
            "6",
            "8",
            None,
            "7",
            "10",
            "9",
            "9",
            "I felt scared",
            "howardppg@gmail.com"
        ],
        [
            "12/06/2024 15:07:39",
            None,
            None,
            None,
            None,
            None,
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
            None,
            "6",
            "5",
            "9",
            "6",
            "",
            "howard-haw-xuen.man@sigmalabs.co.uk"
        ],
        [
            "03/07/2024 16:06:29",
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            "10",
            "10",
            "",
            "howard-haw-xuen.man@sigmalabs.co.uk"
        ]
    ]


@pytest.fixture
def no_user_records():
    return []


@pytest.fixture
def user_record_all_optional_qs_blank():
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

    class mydatetime(datetime.datetime):
        @classmethod
        def now(cls):
            return FAKE_TODAY

    monkeypatch.setattr(datetime, 'datetime', mydatetime)
