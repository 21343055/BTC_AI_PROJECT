import pandas as pd


def get_price_change(df):

    current_price = (
        df["close"].iloc[-1]
    )

    previous_price = (
        df["close"].iloc[-2]
    )

    return (
        (
            current_price
            -
            previous_price
        )
        /
        previous_price
    ) * 100


def get_atr(
    df,
    period=14
):

    previous_close = (
        df["close"].shift(1)
    )

    tr1 = (
        df["high"]
        -
        df["low"]
    )

    tr2 = (
        df["high"]
        -
        previous_close
    ).abs()

    tr3 = (
        df["low"]
        -
        previous_close
    ).abs()

    true_range = pd.concat(
        [tr1, tr2, tr3],
        axis=1
    ).max(axis=1)

    atr = (
        true_range
        .rolling(period)
        .mean()
        .iloc[-1]
    )

    return float(atr)