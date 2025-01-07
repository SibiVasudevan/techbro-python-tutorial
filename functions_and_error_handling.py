def greet(name: str)-> str: #Takes a string, spits out a string
    return f"Hello, {name}!"

result = greet("10x Developer")
print(result)

#function to calculate subtotal, tax, and total like a finance bro
def calculate_total(items: list[float], tax_rate: float = 0.1) -> tuple[float,float,float]:
    subtotal = sum(items) #sum it up, bro
    tax_amount = subtotal*tax_rate
    total = subtotal+tax_amount #grand total
    return subtotal, tax_amount, total

prices = [11, 12.50, 24.45] #spend wisely, or not

sub, tax, total = calculate_total(prices)

#print it all with style
print(f"Subtotal: ${sub:.2f} 💵")  # Clean subtotal
print(f"Tax: ${tax:.2f} 🏦")  # Tax, because we all pay the piper
print(f"Total: ${total:.2f} 🤑")  # Total, aka damage report

#Error Handling!
def divide_number(a: float, b: float) -> float:
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        #Zero division protection!  
        raise ValueError("Bruh, dividing by zero? Not in my codebase!")
    except TypeError:
        #Type validation error
        raise TypeError ("Types looking kinda sus bro")
    except Exception as e:
        #Catch-all cus we're playing 4-d chess
        logging.error(f"Unexpected error in critical path: {e}")
        raise

a = 5
b = 2
div = divide_number(a,b)
print(div)