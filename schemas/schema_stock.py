from datetime import datetime
from ninja import Schema
from typing import Optional

class StockSchema(Schema):
    id: int
    name: str
    code: int
    buy_price: float
    sell_price: float
    total_schares: int
    is_active: bool
    updated_at: datetime
    created_at: datetime
    
class CreateStockSchema(Schema):
    name: str
    code: int
    total_schares: int
    
class UpdateStockSchema(Schema):
    name: Optional[str] = None
    code: Optional[int] = None
    buy_price: Optional[float] = None
    sell_price: Optional[float] = None
    total_schares: Optional[int] = None
    is_active: Optional[bool] = None