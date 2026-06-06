def generate_report_text(
    symbol,
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
):

    report = f"""
🚀 BTC AI SIGNAL ENGINE

Symbol : {symbol}
Price  : {last_price:,.2f}

📈 Trend

1D  : {trend_1d}
4H  : {trend_4h}
1H  : {trend_1h}
15M : {trend_15m}
5M  : {trend_5m}
1M  : {trend_1m}

📊 Market

RSI            : {rsi_data['value']:.2f}
RSI Status     : {rsi_data['status']}
Volume Status  : {volume_data['status']}

Funding Rate   : {funding:.4f}%
OI Change      : {oi_change:.2f}%

Market Regime  : {market_regime}
Order Flow     : {orderflow_bull}-{orderflow_bear}

Pattern        : {pattern}
Pattern Score  : {pattern_score}

Market Score   : {market_score}

🔥 Decision : {final_decision}
"""

    return report