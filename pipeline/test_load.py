"""Tests for load.py"""
from datetime import datetime

from unittest.mock import patch, MagicMock
from psycopg2.extras import execute_values, RealDictCursor, RealDictRow
from psycopg2.extensions import connection
