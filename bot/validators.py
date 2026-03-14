def validate_symbol(symbol: str) -> str:
    if not symbol or not symbol.strip():
        raise ValueError("Symbol is required.")
    return symbol.upper().strip()


def validate_side(side: str) -> str:
    side = side.upper().strip()
    if side not in {"BUY", "SELL"}:
        raise ValueError("Side must be BUY or SELL.")
    return side


def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper().strip()
    if order_type not in {"MARKET", "LIMIT"}:
        raise ValueError("Order type must be MARKET or LIMIT.")
    return order_type


def validate_quantity(quantity: float) -> float:
    try:
        quantity = float(quantity)
    except (TypeError, ValueError):
        raise ValueError("Quantity must be a valid number.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")
    return quantity


def validate_price(price, order_type: str):
    order_type = order_type.upper().strip()

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")
        try:
            price = float(price)
        except (TypeError, ValueError):
            raise ValueError("Price must be a valid number.")
        if price <= 0:
            raise ValueError("Price must be greater than 0.")
        return price

    return None