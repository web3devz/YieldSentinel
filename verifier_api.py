
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
import verifier_logic

app = FastAPI()

class DailyYield(BaseModel):
    date: str
    yield_: float

class DepositEvent(BaseModel):
    date: str
    amount: float

class WithdrawalEvent(BaseModel):
    date: str
    amount: float
    early: bool

class StrategyData(BaseModel):
    strategyAddress: str
    dailyYields: List[dict]
    depositEvents: List[DepositEvent] = []
    withdrawalEvents: List[WithdrawalEvent] = []

@app.post("/analyze")
async def analyze(data: StrategyData):
    raw_data = {
        "strategyAddress": data.strategyAddress,
        "dailyYields": data.dailyYields,
        "depositEvents": [e.dict() for e in data.depositEvents],
        "withdrawalEvents": [w.dict() for w in data.withdrawalEvents]
    }
    result = verifier_logic.analyze_strategy(raw_data)
    return result
