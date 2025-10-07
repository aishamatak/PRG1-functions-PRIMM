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


# grading system 
def calculate_grade(homework_score, test_score): 
    homework_weight = homework_score * 7 
    test_weight = test_score * 3
    total_weight = homework_weight + test_weight
    return total_weight

# main 
# if score is above --- else ... 
