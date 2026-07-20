# Step 1: Create Boolean variables
has_account = True
email_verified = False

# Step 2: Check if the user can log in
can_login = has_account and email_verified

# Step 3: Validate the email address
email = "g@example.com"
is_email_valid = "@" in email

# Step 4: Check the user's age
user_age = 17
is_age_valid = user_age >= 18

# Step 5: Final login check
can_login_final = has_account and email_verified and is_email_valid and is_age_valid

# Step 6: Print the results
print("Can Login:", can_login)
print("Is Email Valid:", is_email_valid)
print("Is Age Valid:", is_age_valid)
print("Can Login Final:", can_login_final)

# Step 7: Use the identity operator
print("Has Account is True:", has_account is True)