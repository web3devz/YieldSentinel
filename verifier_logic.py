
import math

def calculate_weighted_average(yields, decay_factor=0.95):
    weighted_sum = 0
    total_weight = 0
    for i, y in enumerate(reversed(yields)):
        weight = decay_factor ** i
        weighted_sum += y["yield"] * weight
        total_weight += weight
    return weighted_sum / total_weight if total_weight > 0 else 0

def calculate_volatility(yields):
    n = len(yields)
    if n == 0:
        return 0
    mean = sum(y["yield"] for y in yields) / n
    variance = sum((y["yield"] - mean) ** 2 for y in yields) / n
    return math.sqrt(variance)

def calculate_performance_score(yield_avg, benchmark, volatility, early_withdrawal):
    base_score = (yield_avg / benchmark) * 100 if benchmark > 0 else 0
    volatility_penalty = min(volatility * 10, 15)
    withdrawal_penalty = 10 if early_withdrawal else 0
    return max(base_score - volatility_penalty - withdrawal_penalty, 0)

def analyze_strategy(data, window=30, decay_factor=0.95):
    daily_yields = data["dailyYields"][-window:]
    deposit_events = data.get("depositEvents", [])
    withdrawal_events = data.get("withdrawalEvents", [])

    weighted_avg_yield = calculate_weighted_average(daily_yields, decay_factor)
    volatility = calculate_volatility(daily_yields)
    benchmark_yield = calculate_weighted_average(data["dailyYields"], decay_factor)

    early_withdrawal = any(w["early"] for w in withdrawal_events)
    performance_score = calculate_performance_score(weighted_avg_yield, benchmark_yield, volatility, early_withdrawal)

    result = {
        "strategyAddress": data["strategyAddress"],
        "benchmarkYield": round(benchmark_yield, 2),
        "performanceScore": round(performance_score, 2),
        "analysis": {
            "weightedAverageYield": round(weighted_avg_yield, 2),
            "volatility": round(volatility, 2),
            "depositActivity": {
                "totalDeposited": sum(d["amount"] for d in deposit_events),
                "depositCount": len(deposit_events)
            },
            "withdrawalActivity": {
                "totalWithdrawn": sum(w["amount"] for w in withdrawal_events),
                "earlyWithdrawal": early_withdrawal
            }
        },
        "recommendation": "Strategy eligible for bonus." if performance_score >= 70 else "Strategy performance below target."
    }

    return result
