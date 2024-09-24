"""Script for loading cleaned data into our database"""

from datetime import datetime
from os import environ as ENV

from psycopg2 import connect
from psycopg2.extras import execute_values, RealDictCursor, RealDictRow
from psycopg2.extensions import connection


def get_db_connection(config: dict) -> connection:
    """Returns a connection to a database."""
    pass


def load_into_db(conn: connection, input_data: list[list]) -> None:
    """Inputs all data into the database."""
    pass


if __name__ == "__main__":
    pass
