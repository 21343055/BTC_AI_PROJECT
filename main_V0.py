# ==================================
# SERVICES
# ==================================

from services.market_services import (
    load_market_data
)

from services.scoring_services import (
    generate_signal_score
)

# ==================================
# ANALYZER
# ==================================

from analyzer.trend import (
    detect_trend
)

from analyzer.volatility import (
    get_price_change,
    get_atr
)

from analyzer.support_resistance import (
    get_support_resistance
)

from analyzer.volume import (
    analyze_volume
)

from analyzer.rsi import (
    analyze_rsi
)

from analyzer.timeframe import (
    get_multi_timeframe_trend
)

from analyzer.market_regime import (
    detect_market_regime
)

from analyzer.candlestick import (
    detect_pattern
)

# ==================================
# SIGNAL
# ==================================

from signal.orderflow import (
    calculate_orderflow_score
)

from signal.market_bias import (
    get_market_bias
)

# ==================================
# STRATEGY
# ==================================

from strategy.entry import (
    generate_entry
)

from strategy.risk_reward import (
    calculate_rr
)

from strategy.trade_quality import (
    get_trade_quality
)

from strategy.position_size import (
    calculate_position_size
)

from strategy.validation import (
    validate_entry
)

# ==================================
# OUTPUT
# ==================================

from output.report import (
    print_report,
    print_trade_setup
)

# ==================================
# CONFIG
# ==================================

from config.settings import *

# ==================================
# LOAD MARKET DATA
# ==================================

market_data = load_market_data(
    SYMBOL
)

df = market_data["df"]

funding = market_data["funding"]

oi_change = market_data["oi_change"]

orderbook = market_data["orderbook"]

aggtrade = market_data["aggtrade"]

if df is None or df.empty:

    print(
        "Failed to load kline data."
    )

    exit()

if funding is None:

    print(
        "Failed to load funding data."
    )

    exit()

if oi_change is None:

    print(
        "Failed to load open interest data."
    )

    exit()

if orderbook is None:

    print(
        "Failed to load orderbook data."
    )

    exit()

if aggtrade is None:

    print(
        "Failed to load aggtrade data."
    )

    exit()

# ==================================
# ANALYZER
# ==================================

trend = detect_trend(df)

price_change = get_price_change(df)

atr = get_atr(df)

support, resistance = (
    get_support_resistance(df)
)

volume_data = analyze_volume(df)

rsi_data = analyze_rsi(df)

pattern = detect_pattern(df)

# ==================================
# MULTI TIMEFRAME
# ==================================

trends = get_multi_timeframe_trend(
    SYMBOL
)

trend_1m = trends["1m"]

trend_5m = trends["5m"]

trend_15m = trends["15m"]

trend_1h = trends["1h"]
