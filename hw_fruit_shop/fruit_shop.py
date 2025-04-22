import decimal
import logging

from pywebio.input import slider, FLOAT, NUMBER, input as pw_input
from pywebio.output import put_html, put_success


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("fruit_shop.log"), logging.StreamHandler()]
)


APPLE_PRICE = decimal.Decimal(52.75)
BANANA_PRICE = decimal.Decimal(81.40)


logging.info("info")


put_html("<h1>Welcome to our Fruit Shop</h1>")


apple_weight = slider("Apple", type=FLOAT, value=0.0, min_value=0, max_value=5, required=True)
apple_weight = decimal.Decimal(apple_weight).quantize(decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP)

banana_weight = pw_input("Banana", type=NUMBER, value=0, min=0, max=10, required=True)
banana_weight = decimal.Decimal(banana_weight).quantize(decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP)


logging.info(f"Apple weight: {apple_weight}\nBanana weight: {banana_weight}")


apple_cost = (APPLE_PRICE*apple_weight).quantize(decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP)
banana_cost = (BANANA_PRICE*banana_weight).quantize(decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP)

total_cost = apple_cost + banana_cost


put_success(f"Apple cost: {apple_cost}\nBanana cost: {banana_cost}\nTotal cost: {total_cost}")