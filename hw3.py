# Step 1: Declare Boolean variables
is_logged_in = True
is_subscribed = False

# Step 2: Initialize credit values
user_credits = 100
max_credits = 200
min_credits = 50

# Step 3: Check if credits are within the valid range
credits_valid = (user_credits >= min_credits) and \
                (user_credits <= max_credits) and \
                (user_credits != min_credits)

# Step 4: Check bonus eligibility
bonus_eligible = is_subscribed or (user_credits > min_credits and not False)

# Step 5: Modify user_credits
user_credits += 50    # 100 + 50 = 150
user_credits -= 20    # 150 - 20 = 130
user_credits *= 2     # 130 * 2 = 260
user_credits %= 150   # 260 % 150 = 110

# Step 6: Compute the square
power_result = user_credits ** 2

# Step 7: Check full access
full_access = is_logged_in and is_subscribed

# Step 8: Identity operator
is_true_login = (is_logged_in is True)

# Step 9: Demonstrate operator precedence
access_result = is_logged_in or is_subscribed and False

# Step 10: Print the results
print("Is Logged In:", is_logged_in)
print("Is Subscribed:", is_subscribed)
print("Credits Valid:", credits_valid)
print("Bonus Eligible:", bonus_eligible)
print("Final User Credits:", user_credits)
print("Power Result:", power_result)
print("Full Access:", full_access)
print("Is True Login:", is_true_login)
print("Access Result:", access_result)