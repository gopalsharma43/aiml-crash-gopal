# This program calculates tip amount and total bill using functions.

# print() only displays output on the screen.
# return sends a value back from the function so it can be reused later.

def calculate_tip(bill, tip_percent):

    tip_amount = (bill * tip_percent) / 100
    total_amount = bill + tip_amount

    return {
        "bill": bill,
        "tip_percent": tip_percent,
        "tip_amount": tip_amount,
        "total_amount": total_amount
    }


# Test Case 1
result1 = calculate_tip(1000, 10)

# Test Case 2
result2 = calculate_tip(2500, 15)

# Test Case 3
result3 = calculate_tip(5000, 20)


print("Test Case 1")
print(result1)

print("\nTest Case 2")
print(result2)

print("\nTest Case 3")
print(result3)