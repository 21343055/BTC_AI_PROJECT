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
    print_trade_setup,
    generate_report_text
)

# ==================================
# DATABASE
# ==================================

from database.db_manager import (
    initialize_database,
    save_trade
)

# ==================================
# LOGGER
# ==================================

from utils.logger import (
    logger
)

# ==================================
# CONFIG
# ==================================

from config.settings import *

# ==================================
# OTHER
# ==================================

from datetime import datetime

from utils.telegram_notifier import send_telegram_message

# ==================================
# DATABASE INIT
# ==================================

initialize_database()

# ==================================
# LOAD MARKET DATA
# ==================================

logger.info(
    "Loading market data..."
)

market_data = load_market_data(
    SYMBOL
)

df = market_data["df"]

funding = market_data["funding"]

oi_change = market_data["oi_change"]

orderbook = market_data["orderbook"]

aggtrade = market_data["aggtrade"]

# ==================================
# VALIDATION
# ==================================

if df is None or df.empty:

    logger.error(
        "Failed to load kline data."
    )

    exit()

if funding is None:

    logger.error(
        "Failed to load funding data."
    )

    exit()

if oi_change is None:

    logger.error(
        "Failed to load open interest data."
    )

    exit()

if orderbook is None:

    logger.error(
        "Failed to load orderbook data."
    )

    exit()

if aggtrade is None:

    logger.error(
        "Failed to load aggtrade data."
    )

    exit()

# ==================================
# ANALYZER
# ==================================

logger.info(
    "Running analyzer..."
)

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

trend_4h = trends["4h"]

trend_1d = trends["1d"]

# ==================================
# ORDERFLOW
# ==================================

aggressor = (
    "BUYER"
    if aggtrade["delta"] > 0
    else "SELLER"
)

cvd_bias = (
    "BULLISH"
    if aggtrade["cvd"] > 0
    else "BEARISH"
)

if orderbook["imbalance"] > 0.55:

    orderbook_bias = "BULLISH"

elif orderbook["imbalance"] < 0.45:

    orderbook_bias = "BEARISH"

else:

    orderbook_bias = "NEUTRAL"

orderflow_bull, orderflow_bear = (
    calculate_orderflow_score(
        orderbook_bias,
        orderbook["buy_wall_size"],
        orderbook["sell_wall_size"],
        aggressor,
        cvd_bias
    )
)

# ==================================
# MARKET BIAS
# ==================================

market_state = get_market_bias(
    trend,
    orderflow_bull,
    orderflow_bear
)

# ==================================
# MARKET REGIME
# ==================================

market_regime = detect_market_regime(

    trend_1d,
    trend_4h,
    trend_1h,
    trend_15m,
    trend_5m,
    trend_1m,

    orderflow_bull,
    orderflow_bear
)

# ==================================
# SIGNAL SCORE
# ==================================

signal_data = generate_signal_score(

    trend_1d,
    trend_4h,
    trend_1h,
    trend_15m,
    trend_5m,
    trend_1m,

    orderflow_bull,
    orderflow_bear,

    pattern
)

pattern_score = (
    signal_data["pattern_score"]
)

market_score = (
    signal_data["market_score"]
)

final_decision = (
    signal_data["decision"]
)

# ==================================
# ENTRY SETUP
# ==================================

setup = generate_entry(

    market_state,

    orderbook["buy_wall_price"],

    orderbook["sell_wall_price"],

    support,

    resistance,

    atr
)

# ==================================
# REPORT
# ==================================

last_price = float(
    df["close"].iloc[-1]
)

print_report(

    SYMBOL,
    last_price,

    trend_1d,
    trend_4h,
    trend_1h,
    trend_15m,
    trend_5m,
    trend_1m,

    rsi_data,
    volume_data,

    funding,
    oi_change,

    market_regime,

    orderflow_bull,
    orderflow_bear,

    pattern,
    pattern_score,

    market_score,
    final_decision
)

# ==================================
# TELEGRAM REPORT
# ==================================

telegram_report = (
    generate_report_text(

        SYMBOL,
        last_price,

        trend_1d,
        trend_4h,
        trend_1h,
        trend_15m,
        trend_5m,
        trend_1m,

        rsi_data,
        volume_data,

        funding,
        oi_change,

        market_regime,

        orderflow_bull,
        orderflow_bear,

        pattern,
        pattern_score,

        market_score,
        final_decision
    )
)

send_telegram_message(
    telegram_report
)

logger.info(
    "Telegram notification sent."
)

# ==================================
# STRATEGY OUTPUT
# ==================================

if setup is not None:

    rr = calculate_rr(

        setup["entry"],

        setup["stop_loss"],

        setup["tp1"],

        setup["tp2"]
    )

    quality = get_trade_quality(
        rr["rr1"]
    )

    position = (
        calculate_position_size(

            ACCOUNT_SIZE,

            RISK_PERCENT,

            setup["entry"],

            setup["stop_loss"]
        )
    )

    validation = (
        validate_entry(
            last_price,
            setup["entry"]
        )
    )

    print_trade_setup(

        setup,

        rr,

        quality,

        validation,

        position
    )

    # ==================================
    # SAVE TO DATABASE
    # ==================================

    save_trade(

        timestamp=str(
            datetime.now()
        ),

        symbol=SYMBOL,

        decision=final_decision,

        market_score=market_score,

        market_regime=market_regime,

        entry_price=setup["entry"],

        stop_loss=setup["stop_loss"],

        tp1=setup["tp1"],

        tp2=setup["tp2"],

        rr=rr["rr1"],

        trade_grade=quality,

        setup_status=validation[
            "status"
        ]
    )

    logger.info(
        f"Trade saved | "
        f"{final_decision}"
    )

else:

    logger.info(
        "No trade setup generated."
    )

logger.info(
    "Execution finished."
)
