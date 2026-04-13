def add(a, b):
    """두 수의 합을 반환합니다.
    Args: a, b (float): 더할 두 수
    Returns: float: a + b"""
    return a + b

def subtract(a, b):
    """두 수의 차를 반환합니다.
    Args: a, b (float): 첫 번째 수에서 두 번째 수를 뺩니다
    Returns: float: a - b"""
    return a - b

def multiply(a, b):
    """두 수의 곱을 반환합니다.
    Args: a, b (float): 곱할 두 수
    Returns: float: a * b"""
    return a * b

def divide(a, b):
    """두 수의 나눗셈 결과를 반환합니다. 0 나누기 시 ValueError 발생.
    Args: a (float): 피제수 / b (float): 제수
    Returns: float: a / b
    Raises: ValueError: b가 0일 때"""
    if b == 0 :
        raise ValueError(f"Cannot divide by zero: divisor was {b}") 
    return a / b