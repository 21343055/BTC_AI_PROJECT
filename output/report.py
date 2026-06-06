def print_report(
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

    print("=" * 60)

    print(
        f"{symbol} AI SIGNAL ENGINE"
    )

    print("=" * 60)

    print(
        f"Price         : {last_price:,.2f}"
    )

    print()

    print(
        f"1D Trend      : {trend_1d}"
    )

    print(
        f"4H Trend      : {trend_4h}"
    )

    print(
        f"1H Trend      : {trend_1h}"
    )

    print(
        f"15M Trend     : {trend_15m}"
    )

    print(
        f"5M Trend      : {trend_5m}"
    )

    print(
        f"1M Trend      : {trend_1m}"
    )

    print()

    print(
        f"RSI           : {rsi_data['value']:.2f}"
    )

    print(
        f"RSI Status    : {rsi_data['status']}"
    )

    print(
        f"Volume Status : {volume_data['status']}"
    )

    print()

    print(
        f"Funding Rate  : {funding:.4f}%"
    )

    print(
        f"OI Change     : {oi_change:.2f}%"
    )

    print()

    print(
        f"Market Regime : {market_regime}"
    )

    print(
        f"Order Flow    : {orderflow_bull}-{orderflow_bear}"
    )

    print(
        f"Pattern       : {pattern}"
    )

    print(
        f"Pattern Score : {pattern_score}"
    )

    print()

    print(
        f"Market Score  : {market_score}"
    )

    print()

    print(
        f"Decision      : {final_decision}"
    )
    
    
def print_trade_setup(
    setup,
    rr,
    quality,
    validation,
    position
):

    if setup is None:

        print(
            "\nNo trade setup found."
        )

        return

    print()

    print(
        f"Entry         : {setup['entry']:,.2f}"
    )

    print(
        f"Stop Loss     : {setup['stop_loss']:,.2f}"
    )

    print(
        f"TP1           : {setup['tp1']:,.2f}"
    )

    print(
        f"TP2           : {setup['tp2']:,.2f}"
    )

    print()

    print(
        f"RR TP1        : {rr['rr1']:.2f}"
    )

    print(
        f"RR TP2        : {rr['rr2']:.2f}"
    )

    print()

    print(
        f"Trade Grade   : {quality}"
    )

    print(
        f"Setup Status  : {validation['status']}"
    )

    print(
        f"Position Size : "
        f"{position['position_size']:.6f} BTC"
    )

    print("=" * 60)
    
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