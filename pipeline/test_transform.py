"""Tests for transform.py"""

from unittest.mock import MagicMock

import pytest

from transform import (get_user_records, filter_records_older_24hrs,
                       make_emotions_list, make_all_scores_ints, check_for_empty_entries)

NUMERIC_ENTRIES_INDICES = {1, 2, 3, 4, 6, 7, 8, 9}
REQUIRED_ENTRIES_INDICES = {9, 10}


def get_user_records_example_response(example_extracted_json):

    assert isinstance(get_user_records(example_extracted_json), list)

    for record in example_extracted_json:
        assert isinstance(record, list)
        assert len(record) == 11


def get_user_records_optional_responses_empty(all_optional_responses_empty_json):

    assert isinstance(get_user_records(
        all_optional_responses_empty_json), list)

    for record in all_optional_responses_empty_json:
        assert isinstance(record, list)
        assert len(record) == 11


def get_user_records_no_responses(no_responses_json):

    assert isinstance(get_user_records(no_responses_json), list)
    assert len(get_user_records(no_responses_json)) == 0


def filter_records_older_24hrs_success(example_user_records):
    # TODO: Research how to mock datetime object!
    pass


def filter_records_older_24hrs_no_records(no_user_records):

    assert isinstance(filter_records_older_24hrs(no_user_records), list)
    assert len(filter_records_older_24hrs(no_user_records)) == 0


def make_emotions_list_example_records(example_user_records):

    for record in make_emotions_list(example_user_records):

        record_emotion = record[5]

        assert isinstance(record_emotion, list)

        if len(record_emotion) > 0:

            for emotion in record_emotion:

                assert isinstance(emotion, str)


def make_emotions_list_record_no_emotions(example_user_records_no_emotions):

    for record in make_emotions_list(example_user_records_no_emotions):

        assert isinstance(record[5], list)

        assert len(record[5]) == 0


def make_all_scores_ints_success(example_user_records):

    for record in make_all_scores_ints(example_user_records):

        for i in NUMERIC_ENTRIES_INDICES:

            assert isinstance(record[i], int)


def make_all_scores_ints_no_records(no_user_records):

    assert make_all_scores_ints(no_user_records) == []


def make_all_scores_ints_all_optional_qs_blank(user_record_all_optional_qs_blank):

    for record in make_all_scores_ints(user_record_all_optional_qs_blank):

        for i in REQUIRED_ENTRIES_INDICES:

            assert isinstance(record[i], int)


def check_for_empty_entries_record_no_emotions(example_user_records_no_emotions):

    for record in check_for_empty_entries(example_user_records_no_emotions):

        assert record[5] is None


def check_for_empty_entries_all_optional_qs_blank(user_record_all_optional_qs_blank):

    for record in check_for_empty_entries(user_record_all_optional_qs_blank):

        for i in REQUIRED_ENTRIES_INDICES:

            assert record[i] is None
