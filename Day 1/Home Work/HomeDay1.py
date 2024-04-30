weather = "Cloudy"
if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

#How are you feeling today
Mood = "Sad"
if Mood == "Happy":
    print("That's great to hear!")
else:
    print("I hope your day gets better!")

PI_VALUE = 3.14
user_age = 25
user_location = "New_York"
MAX_LIMIT = 1000

Bread = 3.00
Peanut_butter = 4.26
Jelly = 1.29
Grocery_Cart = Bread+Peanut_butter+Jelly
print(Grocery_Cart)

def calculate_total_amount(principal, interest_rate):
    # Convert the interest rate from percentage to decimal
    interest_rate_decimal = interest_rate / 100
    # Calculate the total amount after a year
    total_amount = principal * (1 + interest_rate_decimal)
    return total_amount

# Test the function with $10,000 at 7% interest
principal = 10000
interest_rate = 7
print(calculate_total_amount(principal, interest_rate))
          