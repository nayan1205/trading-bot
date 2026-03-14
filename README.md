# Binance Futures Testnet Trading Bot

A simple Python CLI application to place **MARKET** and **LIMIT** orders on **Binance Futures Testnet (USDT-M)**.

This project was built as part of a Python Developer application task. It focuses on clean structure, input validation, logging, and error handling.

## Features

- Place **MARKET** orders
- Place **LIMIT** orders
- Supports both **BUY** and **SELL**
- CLI input using `argparse`
- Input validation with clear error messages
- Structured code with separate API, order, validation, and logging layers
- Logging of API requests, responses, and errors
- Exception handling for invalid input, API errors, and network failures

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── sample_logs/
│   ├── market_order.log
│   └── limit_order.log
│
├── .env
├── .gitignore
├── cli.py
├── README.md
└── requirements.txt
````

## Requirements

* Python 3.9+
* Binance Futures Testnet account
* Binance Futures Testnet API key and secret

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/nayan1205/trading-bot.git
cd trading-bot
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Add a `.env` file in the project root with:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
BINANCE_BASE_URL=https://testnet.binancefuture.com
```

## Binance Futures Testnet Setup

1. Log in to Binance Futures Testnet.
2. Generate your API key and secret.
3. Paste them into the `.env` file.
4. Make sure your testnet account is active and funded with test balance.

## Usage

Run the CLI with:

```bash
python cli.py --symbol <SYMBOL> --side <BUY/SELL> --type <MARKET/LIMIT> --quantity <QUANTITY> [--price <PRICE>]
```

### Arguments

* `--symbol`: Trading pair symbol, for example `BTCUSDT`
* `--side`: `BUY` or `SELL`
* `--type`: `MARKET` or `LIMIT`
* `--quantity`: Order quantity
* `--price`: Required only for `LIMIT` orders

## Examples

### Place a MARKET BUY order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a MARKET SELL order

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

### Place a LIMIT BUY order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

### Place a LIMIT SELL order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 90000
```

## Example Output

```text
=== Order Request Summary ===
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

=== Order Response ===
Order ID: 123456789
Status: FILLED
Executed Quantity: 0.001
Average Price: 68000.5

Order placed successfully.
```

## Validation

The application validates:

* symbol is provided
* side is `BUY` or `SELL`
* order type is `MARKET` or `LIMIT`
* quantity is a valid number greater than 0
* price is provided for `LIMIT` orders
* price is greater than 0 for `LIMIT` orders

## Logging

Runtime logs are written to:

```text
logs/trading_bot.log
```

Included sample logs:

```text
sample_logs/market_order.log
sample_logs/limit_order.log
```

## Error Handling

The application handles:

* invalid CLI input
* missing required values
* invalid quantity or price
* Binance API errors
* network/request failures
* unexpected runtime exceptions

Errors are printed in the terminal and written to the log file.

## Assumptions

* Built for **Binance USDT-M Futures Testnet** only
* Supports only **MARKET** and **LIMIT** orders
* `timeInForce=GTC` is used for LIMIT orders
* API credentials are loaded from `.env`

## Notes

* Do not commit your real `.env` file
* Do not share your API credentials
* `logs/` is for runtime logs
* `sample_logs/` contains logs included for submission

## Deliverables Included

* Source code
* `README.md`
* `requirements.txt`
* Sample logs for one MARKET order
* Sample logs for one LIMIT order

## Author

Submitted by **Nayan** for the Python Developer application task.

```
```
