from typing import Any, Dict
from src.schemas.price import PriceCreate

def model_dump(price_create: PriceCreate) -> Dict[str, Any]:
    return {
        "name": price_create.name,
        "one_day": price_create.one_day,
        "two_three_days": price_create.two_three_days,
        "four_seven_days": price_create.four_seven_days,
        "eight_fourteen_days": price_create.eight_fourteen_days,
        "fifteen_thirty_days": price_create.fifteen_thirty_days,
        "weekend": price_create.weekend,
        "deposit": price_create.deposit
    }