
# Adds two floats together.
def add(x: float, y: float) -> float:
    result = x + y
    return result

# Multiplies two floats together
def multiply(x: float, y: float) -> float:
    result = x * y
    return result

# Sqaures two floats together
def sqaure(x: float) -> float:
    result = multiply(x, x)
    return result


# Adds two squares together
def add_sqaures(x: float, y: float) -> float:
    result = add(multiply(x), multiply(y))
    return result