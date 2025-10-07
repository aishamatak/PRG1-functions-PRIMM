def calculate_total(price, tax_rate=0.20, discount=0):
    subtotal = price - discount
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

# Test cases
print(f"£{calculate_total(100):.2f}")
print(f"£{calculate_total(100, 0.1):.2f}")
print(f"£{calculate_total(100, 0.08, 10):.2f}")

#adding a default 12% tip 
def calculate_total(price, tax_rate=0.2, discount=0): 
    subtotal = price - discount 
    tax = subtotal * tax_rate 
    total = subtotal + tax 
    tip = total * 1.12 
    return tip 

