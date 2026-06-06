import sqlite3
import pandas as pd

from pathlib import Path


# ==================================
# DATABASE CONFIG
# ==================================

DB_PATH = (
    Path(__file__).parent
    / "trades.db"
)


# ==================================
# CREATE DATABASE
# ==================================

def initialize_database():

    conn = sqlite3.connect(
        DB_PATH
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS trades (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            symbol TEXT,

            decision TEXT,

            market_score REAL,

            market_regime TEXT,

            entry_price REAL,

            stop_loss REAL,

            tp1 REAL,

            tp2 REAL,

            rr REAL,

            trade_grade TEXT,

            setup_status TEXT
        )
        """
    )

    conn.commit()

    conn.close()


# ==================================
# SAVE TRADE
# ==================================

def save_trade(

    timestamp,

    symbol,

    decision,

    market_score,

    market_regime,

    entry_price,

    stop_loss,

    tp1,

    tp2,

    rr,

    trade_grade,

    setup_status
):

    conn = sqlite3.connect(
        DB_PATH
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO trades (

            timestamp,

            symbol,

            decision,

            market_score,

            market_regime,

            entry_price,

            stop_loss,

            tp1,

            tp2,

            rr,

            trade_grade,

            setup_status

        )

        VALUES (

            ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?
        )
        """,

        (

            timestamp,

            symbol,

            decision,

            market_score,

            market_regime,

            entry_price,

            stop_loss,

            tp1,

            tp2,

            rr,

            trade_grade,

            setup_status
        )
    )

    conn.commit()

    conn.close()


# ==================================
# GET ALL TRADES
# ==================================

def get_all_trades():

    conn = sqlite3.connect(
        DB_PATH
    )

    query = (
        "SELECT * FROM trades"
    )

    df = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return df


# ==================================
# GET LAST TRADE
# ==================================

def get_last_trade():

    conn = sqlite3.connect(
        DB_PATH
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM trades
        ORDER BY id DESC
        LIMIT 1
        """
    )

    trade = cursor.fetchone()

    conn.close()

    return trade


# ==================================
# DELETE ALL TRADES
# ==================================

def delete_all_trades():

    conn = sqlite3.connect(
        DB_PATH
    )

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM trades"
    )

    conn.commit()

    conn.close()


# ==================================
# EXPORT CSV
# ==================================

def export_to_csv(

    filename=(
        "database/trades_export.csv"
    )
):

    df = get_all_trades()

    df.to_csv(
        filename,
        index=False
    )

    return filename