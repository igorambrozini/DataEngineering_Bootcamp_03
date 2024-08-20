"""Exercise 1: Data Quality Check

You are analyzing a sales dataset and need to ensure that all records have
positive values for quantity and price. Write a program that checks these
fields and prints "Valid data" if both are positive or "Invalid data" otherwise.
"""

def check_data(quantity, price):
    if quantity > 0 and price > 0:
        return "Valid data"
    else:
        return "Invalid data"
        
quantity = float(input("Digite a quantidade: "))
price = float(input("Digite o preço: "))

result = check_data(quantity, price)
print(result)