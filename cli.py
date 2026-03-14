import argparse
import sys

from bot.client import BinanceFuturesClient
from bot.logging_config import setup_logger
from bot.orders import place_order


def parse_args():
    parser = argparse.ArgumentParser(
        description="Place orders on Binance Futures Testnet"
    )

    parser.add_argument("--symbol", required=True, help="Trading pair symbol, e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", required=False, help="Price for LIMIT orders")

    return parser.parse_args()


def print_order_summary(symbol, side, order_type, quantity, price=None):
    print("\n=== Order Request Summary ===")
    print(f"Symbol: {symbol}")
    print(f"Side: {side}")
    print(f"Type: {order_type}")
    print(f"Quantity: {quantity}")
    if price is not None:
        print(f"Price: {price}")


def print_order_response(response):
    print("\n=== Order Response ===")
    print(f"Order ID: {response.get('orderId', 'N/A')}")
    print(f"Status: {response.get('status', 'N/A')}")
    print(f"Executed Quantity: {response.get('executedQty', 'N/A')}")
    print(f"Average Price: {response.get('avgPrice', 'N/A')}")


def main():
    logger = setup_logger()
    args = parse_args()

    try:
        print_order_summary(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        client = BinanceFuturesClient(logger)

        response = place_order(
            client=client,
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print_order_response(response)
        print("\nOrder placed successfully.")

    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        print(f"\nOrder failed: {str(e)}")
        sys.exit(1)

    except Exception as e:
        logger.error(f"Application error: {str(e)}")
        print(f"\nOrder failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()