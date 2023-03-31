from datetime import datetime, timedelta

import pytest
from sales_management.utils import execute_script_file
import django
from django.utils import timezone
import os


@pytest.fixture
def load_test_data():
    current_path = os.path.dirname(os.path.abspath(__file__))
    sql_dir_path = os.path.join(current_path, "data2")
    conn = django.db.connections['default']

    execute_script_file(
        os.path.join(sql_dir_path, "sales.sql"), conn)
    execute_script_file(
        os.path.join(sql_dir_path, "sales_items.sql"), conn)
    execute_script_file(
        os.path.join(sql_dir_path, "sellers.sql"), conn)
    execute_script_file(
        os.path.join(sql_dir_path, "freee_deals.sql"), conn)
    execute_script_file(
        os.path.join(sql_dir_path, "omron_transactions.sql"), conn)
    execute_script_file(
        os.path.join(sql_dir_path, "payments.sql"), conn)
    execute_script_file(
        os.path.join(sql_dir_path, "hps.sql"), conn)
    execute_script_file(
        os.path.join(sql_dir_path, "emoney.sql"), conn)
    execute_script_file(
        os.path.join(sql_dir_path, "emoney_types.sql"), conn)
    execute_script_file(
        os.path.join(sql_dir_path, "salon_items.sql"), conn)
    execute_script_file(
        os.path.join(sql_dir_path, "retail_items.sql"), conn)
    
    yield

    # clean up
    conn.cursor().execute("DELETE FROM sales")
    conn.cursor().execute("DELETE FROM sales_items")
    conn.cursor().execute("DELETE FROM sellers")
    conn.cursor().execute("DELETE FROM freee_deals")
    conn.cursor().execute("DELETE FROM omron_transactions")
    conn.cursor().execute("DELETE FROM payments")
    conn.cursor().execute("DELETE FROM hps")
    conn.cursor().execute("DELETE FROM emoney")
    conn.cursor().execute("DELETE FROM emoney_types")
    conn.cursor().execute("DELETE FROM salon_items")
    conn.cursor().execute("DELETE FROM retail_items")


def is_valid_datetime( date_serializer, date_db ):
    # time delta is 9 hours
    return datetime.fromisoformat(date_serializer) - timezone.make_aware(datetime.fromisoformat(date_db))== timedelta(0, 0, 0, 0, 0, 9)

