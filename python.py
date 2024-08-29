def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)

# Example usage
expression = "2 + 3 * 5"
print(calculate_expression(expression))