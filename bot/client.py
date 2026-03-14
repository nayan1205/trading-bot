import os
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException


class BinanceFuturesClient:
    def __init__(self, logger):
        load_dotenv()

        self.logger = logger
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")
        self.base_url = os.getenv("BINANCE_BASE_URL", "https://testnet.binancefuture.com")

        if not self.api_key or not self.api_secret:
            raise ValueError("Missing Binance API credentials in .env file.")

        self.client = Client(self.api_key, self.api_secret)
        self.client.FUTURES_URL = f"{self.base_url}/fapi"

    def create_futures_order(self, order_params: dict) -> dict:
        try:
            safe_log_data = {k: v for k, v in order_params.items()}
            self.logger.info(f"Sending futures order request: {safe_log_data}")

            response = self.client.futures_create_order(**order_params)

            self.logger.info(f"Received Binance response: {response}")
            return response

        except BinanceAPIException as e:
            self.logger.error(f"Binance API error: status={e.status_code}, message={e.message}")
            raise Exception(f"Binance API error: {e.message}")

        except BinanceRequestException as e:
            self.logger.error(f"Binance request error: {str(e)}")
            raise Exception(f"Network/request error: {str(e)}")

        except Exception as e:
            self.logger.exception("Unexpected error while creating futures order.")
            raise Exception(f"Unexpected error: {str(e)}")