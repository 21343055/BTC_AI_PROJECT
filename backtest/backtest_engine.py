import pandas as pd


def run_backtest(df):

    total_trade = 0

    win = 0

    loss = 0

    breakeven = 0

    total_pnl = 0

    trade_history = []

    # ==========================
    # Streak Tracking
    # ==========================

    current_win_streak = 0
    current_loss_streak = 0

    max_win_streak = 0
    max_loss_streak = 0

    # ==========================
    # Indicator
    # ==========================

    df = df.copy()

    df["EMA20"] = (
        df["close"]
        .ewm(
            span=20,
            adjust=False
        )
        .mean()
    )

    df["EMA50"] = (
        df["close"]
        .ewm(
            span=50,
            adjust=False
        )
        .mean()
    )

    # ==========================
    # Backtest Loop
    # ==========================

    for i in range(50, len(df) - 10):

        current = df.iloc[i]

        future = df.iloc[i + 10]

        signal = "NO TRADE"

        # ==========================
        # Trend Logic
        # ==========================

        if current["EMA20"] > current["EMA50"]:

            signal = "LONG"

        elif current["EMA20"] < current["EMA50"]:

            signal = "SHORT"

        else:

            continue

        entry = float(
            current["close"]
        )

        exit_price = float(
            future["close"]
        )

        # ==========================
        # PNL Calculation
        # ==========================

        if signal == "LONG":

            pnl = (
                (
                    exit_price
                    - entry
                )
                /
                entry
            ) * 100

        else:

            pnl = (
                (
                    entry
                    - exit_price
                )
                /
                entry
            ) * 100

        total_trade += 1

        total_pnl += pnl

        # ==========================
        # Trade Result
        # ==========================

        if pnl > 0:

            win += 1

            result = "WIN"

            current_win_streak += 1
            current_loss_streak = 0

            max_win_streak = max(
                max_win_streak,
                current_win_streak
            )

        elif pnl < 0:

            loss += 1

            result = "LOSS"

            current_loss_streak += 1
            current_win_streak = 0

            max_loss_streak = max(
                max_loss_streak,
                current_loss_streak
            )

        else:

            breakeven += 1

            result = "BREAKEVEN"

            current_win_streak = 0
            current_loss_streak = 0

        trade_history.append({

            "index": i,

            "signal": signal,

            "entry": round(
                entry,
                2
            ),

            "exit": round(
                exit_price,
                2
            ),

            "pnl_percent": round(
                pnl,
                2
            ),

            "result": result
        })

    # ==========================
    # Summary
    # ==========================

    winrate = 0

    if total_trade > 0:

        winrate = (
            win
            /
            total_trade
        ) * 100

    avg_pnl = 0

    if total_trade > 0:

        avg_pnl = (
            total_pnl
            /
            total_trade
        )

    # ==========================
    # Return
    # ==========================

    return {

        "total_trade":
            total_trade,

        "win":
            win,

        "loss":
            loss,

        "breakeven":
            breakeven,

        "winrate":
            round(
                winrate,
                2
            ),

        "total_pnl":
            round(
                total_pnl,
                2
            ),

        "avg_pnl":
            round(
                avg_pnl,
                2
            ),

        "max_win_streak":
            max_win_streak,

        "max_loss_streak":
            max_loss_streak,

        "trade_history":
            trade_history
    }