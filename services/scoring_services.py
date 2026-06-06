from signal.pattern_score import (
    calculate_pattern_score
)

from signal.market_score import (
    calculate_market_score
)

from signal.decision import (
    get_final_decision
)


def generate_signal_score(

    trend_1d,
    trend_4h,
    trend_1h,
    trend_15m,
    trend_5m,
    trend_1m,

    orderflow_bull,
    orderflow_bear,

    pattern
):

    pattern_score = (
        calculate_pattern_score(
            pattern
        )
    )

    score = (
        calculate_market_score(

            trend_1d,
            trend_4h,
            trend_1h,
            trend_15m,
            trend_5m,
            trend_1m,

            orderflow_bull,
            orderflow_bear,

            pattern_score
        )
    )

    decision = (
        get_final_decision(
            score
        )
    )

    return {

        "pattern_score":
            pattern_score,

        "market_score":
            score,

        "decision":
            decision
    }