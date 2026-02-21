from pydantic import BaseModel
from typing import List
from datetime import datetime

class Expense(BaseModel):
    date: datetime
    amount: float

class Transaction(BaseModel):
    date: datetime
    amount: float
    ceiling: float
    remanent: float

class QPeriod(BaseModel):
    fixed: float
    start: datetime
    end: datetime

class PPeriod(BaseModel):
    extra: float
    start: datetime
    end: datetime

class KPeriod(BaseModel):
    start: datetime
    end: datetime

class ValidatorRequest(BaseModel):
    wage: float
    transactions: List[Transaction]

class FilterRequest(BaseModel):
    q: List[QPeriod]
    p: List[PPeriod]
    k: List[KPeriod]
    transactions: List[Transaction]

class ReturnsRequest(BaseModel):
    age: int
    wage: float
    inflation: float
    q: List[QPeriod]
    p: List[PPeriod]
    k: List[KPeriod]
    transactions: List[Expense]