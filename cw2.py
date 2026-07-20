# Multiline string for the receipt header
header = """\tABC BOOKSTORE
\tCUSTOMER RECEIPT
---------------------------"""

# Book details
book1 = "Python Basics"
price1 = 450

book2 = "Data Science Intro"
price2 = 600

# Receipt lines using format()
line1 = "Book Title: {}\tPrice: ₹{}".format(book1, price1)
line2 = "Book Title: {}\tPrice: ₹{}".format(book2, price2)

# Calculate total
total = price1 + price2

# Total line using format()
total_line = "Total Price:\t₹{}".format(total)

# Thank-you message
message = "\nThank you for shopping with us!"

# Combine everything
receipt = (
    header + "\n" +
    line1 + "\n" +
    line2 + "\n" +
    "---------------------------\n" +
    total_line +
    message
)

# Display receipt in uppercase
print(receipt.upper())