import random

# Prices per kilogram
rice_price = 45
sugar_price = 40
oil_price = 130

# Quantities purchased
rice_qty = 3
sugar_qty = 2.5
oil_qty = 1.8

# Calculate total price for each item
rice_total = rice_price * rice_qty
sugar_total = sugar_price * sugar_qty
oil_total = oil_price * oil_qty

# Calculate final bill
total_bill = rice_total + sugar_total + oil_total

# Print item totals
print("Rice Total:", rice_total)
print("Sugar Total:", sugar_total)
print("Oil Total:", oil_total)

# Print total bill
print("Total Bill:", total_bill)

# Convert total bill to integer
bill_int = int(total_bill)
print("Total Bill (Integer):", bill_int)

# Convert total bill to string
bill_str = str(total_bill)
print("Total Bill (String): " + bill_str)

# Generate random delivery charge between ₹5 and ₹10
delivery_charge = random.randint(5, 10)

# Final bill including delivery charge
final_bill = total_bill + delivery_charge

print("Delivery Charge:", delivery_charge)
print("Final Bill:", final_bill)