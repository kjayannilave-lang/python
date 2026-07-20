# Step 1: Create lists for each workshop
web_development = ["Rahul", "Priya", "Asha"]
data_science = ["Kiran", "Meera", "Arun"]
ui_ux_design = ["Neha", "Riya", "Vikram"]

# Step 2: Combine all workshop lists into a nested list
all_participants = [web_development, data_science, ui_ux_design]

# Step 3: Add a new participant to the Web Development workshop
web_development.append("Sanjay")

# Step 4: Insert a participant at the 2nd position in the Data Science list
data_science.insert(1, "Anita")

# Step 5: Remove the last participant from the UI/UX Design list
ui_ux_design.pop()

# Step 6: Copy the Data Science list and clear the original
data_science_copy = data_science.copy()
data_science.clear()

# Step 7: Display the first two participants from Web Development
print("First two Web Development participants:", web_development[:2])

# Step 8: Create a list of the length of each name in the copied Data Science list
name_lengths = [len(name) for name in data_science_copy]
print("Length of each Data Science participant name:", name_lengths)

# Step 9: Check if "Asha" is in any workshop list
asha_found = (
    "Asha" in web_development or
    "Asha" in data_science or
    "Asha" in ui_ux_design
)
print("Is Asha in any workshop?", asha_found)

# Step 10: Create a tuple with the first participant from each workshop
first_participants = (
    web_development[0],
    data_science_copy[0],   # Original Data Science list is cleared
    ui_ux_design[0]
)
print("First participants tuple:", first_participants)

# Print all lists
print("\nWeb Development:", web_development)
print("Data Science (Original):", data_science)
print("Data Science (Copy):", data_science_copy)
print("UI/UX Design:", ui_ux_design)

print("\nNested List:")
print(all_participants) 