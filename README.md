# 🥗 Daily Calorie Tracker

> A simple and lightweight Python program to log your meals, track your calorie intake, and compare it against your daily limit — all from the terminal.

---

## 🚀 Features

✅ Log **meal names** and **calorie counts**  
✅ Automatically calculate **total** and **average** calories  
✅ Compare results with your **daily calorie limit**  
✅ Optionally **save your session** to a timestamped `.txt` log file  
✅ Clean, minimal code using **Python dictionaries** for data storage  
✅ **No external dependencies** – just pure Python 🐍  

---

## 🧠 Requirements

- **Python 3.6** or higher  
- No additional libraries required (uses only built-in modules)

---

## ⚙️ How to Run

1. **Clone** this repository:
   ```bash
   git clone https://github.com/chiragchanchal/daily-calorie-tracker.git
   cd daily-calorie-tracker
Run the script:

bash
Copy code
python calorie_tracker.py
Follow the prompts:

Enter how many meals you had.

Provide each meal’s name and calorie count.

Input your daily calorie limit.

🧾 Example Output
vbnet
Copy code
Welcome to the Daily Calorie Tracker!
Log your meals, track calories, and compare to your daily goal.

How many meals would you like to log today? 3

Enter name of meal #1: Breakfast
Enter calories for 'Breakfast': 350

Enter name of meal #2: Lunch
Enter calories for 'Lunch': 600

Enter name of meal #3: Dinner
Enter calories for 'Dinner': 500

What is your daily calorie limit? 1600

✅ You stayed within your daily calorie limit!

Your Meal Summary:
Meal            Calories
----------------------------
Breakfast       350
Lunch           600
Dinner          500
----------------------------
Total:          1450
Average:        483.33

Do you want to save this session to a file? (yes/no): yes
✅ Session saved to 'calorie_session_20251026_003012.txt'
📄 Example Log File
When saved, a timestamped text file (e.g. calorie_session_20251026_003012.txt) will be created automatically:

yaml
Copy code
Daily Calorie Tracker Log
Timestamp: 2025-10-26 00:30:12

Meal            Calories
----------------------------
Breakfast       350
Lunch           600
Dinner          500
----------------------------
Total:          1450
Average:        483.33
Daily Limit:    1600
Status:         Within Limit ✅
🧩 Code Overview
Section	Description
Setup & Intro	Prints welcome message
Data Collection	Uses a Python dictionary to store meal data
Calculations	Computes total and average calories
Limit Checker	Compares total with daily calorie goal
Summary Output	Displays a formatted results table
Save Option	Saves results to a timestamped text file

🪄 Example Use Case
Want to keep track of your meals daily without installing heavy apps?
Run this script once a day and generate a clean report in seconds.

🧑‍💻 License
This project is open-source and available for educational and personal use.
Feel free to modify, enhance, or extend it to suit your needs.

💡 Pro Tip
Want to make it even better?
Add features like:

🔁 Weekly calorie averages

📊 CSV or JSON exports

🧮 Calorie goal progress tracking

Made with ❤️ in Python
