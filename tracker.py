import datetime

print("Welcome to the Daily Calorie Tracker!")
print("Log your meals, track calories, and compare to your daily goal.\n")

# Task: Collect Data Using Dictionary
meals = {}

try:
    meal_count = int(input("How many meals would you like to log today? "))
    for i in range(meal_count):
        meal_name = input(f"\nEnter name of meal #{i+1}: ").strip()
        calorie = float(input(f"Enter calories for '{meal_name}': "))
        meals[meal_name] = calorie
except ValueError:
    print("Invalid input. Numbers only please!")
    exit()

# Task: Calculate Totals
total_calories = sum(meals.values())
average_calories = total_calories / meal_count if meal_count else 0

try:
    daily_limit = float(input("\nWhat is your daily calorie limit? "))
except ValueError:
    print("Please enter a valid number for the calorie limit.")
    exit()

# Task: Daily Limit Notification
print()
if total_calories > daily_limit:
    print("⚠ You exceeded your daily calorie limit today!")
else:
    print("✅ You stayed within your daily calorie limit!")

# Task: Print Table Summary
print("\nYour Meal Summary:")
print("Meal\t\tCalories")
print("----------------------------")
for meal, cal in meals.items():
    print(f"{meal}\t\t{cal}")
print("----------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")

# Task: Save Results to File (Bonus)
save = input("\nDo you want to save this session to a file? (yes/no): ").strip().lower()
if save == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"calorie_session_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write("Daily Calorie Tracker Log\n")
        f.write(f"Timestamp: {timestamp}\n\n")
        f.write("Meal\t\tCalories\n")
        f.write("----------------------------\n")
        for meal, cal in meals.items():
            f.write(f"{meal}\t\t{cal}\n")
        f.write("----------------------------\n")
        f.write(f"Total:\t\t{total_calories}\n")
        f.write(f"Average:\t{average_calories:.2f}\n")
        f.write(f"Daily Limit:\t{daily_limit}\n")
        if total_calories > daily_limit:
            f.write("Status:\tExceeded Limit ⚠\n")
        else:
            f.write("Status:\tWithin Limit ✅\n")
    print(f"\n✅ Session saved to '{filename}'")
else:
    print("Session not saved.")
