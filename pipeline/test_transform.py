"""Tests for transform.py"""

from unittest.mock import MagicMock

from transform import (get_user_records, filter_records_older_24hrs,
                       make_emotions_list, make_all_scores_ints, check_for_empty_entries)


OPTIONAL_ENTRIES_INDICES = {1, 2, 3, 4, 6, 7, 10}

REQUIRED_ENTRIES_INDICES = {8, 9}

NUMERIC_ENTRIES_INDICES = {1, 2, 3, 4, 6, 7, 8, 9}


def test_get_user_records_example_response():

    mock_file = MagicMock()

    mock_file.name = "mock.json"

    assert isinstance(get_user_records(mock_file.name), list)

    for record in get_user_records(mock_file.name):
        assert isinstance(record, list)
        assert len(record) == 12


def test_filter_records_older_24hrs_success(example_user_records, patch_datetime_now):

    assert isinstance(filter_records_older_24hrs(example_user_records), set)
    assert len(filter_records_older_24hrs(example_user_records)) == 0


def test_filter_records_older_24hrs_no_records(no_user_records):

    assert isinstance(filter_records_older_24hrs(no_user_records), set)
    assert len(filter_records_older_24hrs(no_user_records)) == 0


def test_make_emotions_list_example_records(example_user_records):

    for record in make_emotions_list(example_user_records):

        record_emotion = record[5]

        assert isinstance(record_emotion, list)

        if len(record_emotion) > 0:

            for emotion in record_emotion:

                assert isinstance(emotion, str)


def test_make_emotions_list_record_no_emotions(
        example_user_records_no_emotions_empty_entries_formatted):

    for record in make_emotions_list(example_user_records_no_emotions_empty_entries_formatted):

        assert record[5] is None


def test_make_all_scores_ints_success(example_user_records):

    example_user_records_no_empty_str = check_for_empty_entries(
        example_user_records)

    for record in make_all_scores_ints(example_user_records_no_empty_str):

        for i in NUMERIC_ENTRIES_INDICES:

            if record[i] is not None:

                assert isinstance(record[i], int)


def test_make_all_scores_ints_no_records(no_user_records):

    assert make_all_scores_ints(no_user_records) == []


def test_make_all_scores_ints_all_optional_qs_blank(user_record_all_optional_qs_blank):

    user_record_all_optional_qs_blank_no_empty_str = check_for_empty_entries(
        user_record_all_optional_qs_blank)

    for record in make_all_scores_ints(user_record_all_optional_qs_blank_no_empty_str):

        for i in REQUIRED_ENTRIES_INDICES:

            assert isinstance(record[i], int)


def test_check_for_empty_entries_record_no_emotions(example_user_records_no_emotions_empty_entries_formatted):

    for record in check_for_empty_entries(example_user_records_no_emotions_empty_entries_formatted):

        assert record[5] is None


def test_check_for_empty_entries_all_optional_qs_blank(user_record_all_optional_qs_blank):

    for record in check_for_empty_entries(user_record_all_optional_qs_blank):

        for i in OPTIONAL_ENTRIES_INDICES:

            assert record[i] is None
