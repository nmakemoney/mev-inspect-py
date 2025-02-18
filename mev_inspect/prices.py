from typing import List

from mev_inspect.classifiers.specs.weth import WETH_ADDRESS
from mev_inspect.coinbase import fetch_coinbase_prices
from mev_inspect.schemas.prices import (
    AAVE_TOKEN_ADDRESS,
    CDAI_TOKEN_ADDRESS,
    CUSDC_TOKEN_ADDRESS,
    DAI_TOKEN_ADDRESS,
    LINK_TOKEN_ADDRESS,
    REN_TOKEN_ADDRESS,
    UNI_TOKEN_ADDRESS,
    USDC_TOKEN_ADDRESS,
    WBTC_TOKEN_ADDRESS,
    YEARN_TOKEN_ADDRESS,
    Price,
)
from mev_inspect.schemas.transfers import ETH_TOKEN_ADDRESS

SUPPORTED_TOKENS = [
    AAVE_TOKEN_ADDRESS,
    CDAI_TOKEN_ADDRESS,
    CUSDC_TOKEN_ADDRESS,
    DAI_TOKEN_ADDRESS,
    ETH_TOKEN_ADDRESS,
    LINK_TOKEN_ADDRESS,
    REN_TOKEN_ADDRESS,
    UNI_TOKEN_ADDRESS,
    USDC_TOKEN_ADDRESS,
    WBTC_TOKEN_ADDRESS,
    WETH_ADDRESS,
    YEARN_TOKEN_ADDRESS,
]


async def fetch_all_supported_prices() -> List[Price]:
    prices = []

    for token_address in SUPPORTED_TOKENS:
        coinbase_prices = await fetch_coinbase_prices(token_address)
        for usd_price, timestamp_seconds in coinbase_prices.all.prices:
            price = Price(
                token_address=token_address,
                usd_price=usd_price,
                timestamp=timestamp_seconds,
            )

            prices.append(price)

    return prices
