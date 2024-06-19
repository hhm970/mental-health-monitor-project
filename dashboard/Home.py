"""Script that create the home page of the dashboard."""

from os import environ as ENV
from datetime import datetime, timedelta

import pandas as pd
import altair as alt
import streamlit as st
from dotenv import load_dotenv

from psycopg2 import connect
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection


def get_db_connection(config: dict) -> connection:
    """Returns a connection to the database."""

    return connect(
        dbname=config["DB_NAME"],
        user=config["DB_USER"],
        password=config["DB_PASSWORD"],
        host=config["DB_HOST"],
        port=config["DB_PORT"],
        cursor_factory=RealDictCursor
    )


if __name__ == "__main__":

    load_dotenv()

    conn = get_db_connection(ENV)

    st.set_page_config(page_title='Mood For Thought',
                       page_icon=":brain:", layout="wide")

    st.title("Welcome To Mood for Thought, your data-driven mental-health monitor!")
