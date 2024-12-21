# Personal Daily Reminder
task = input("Enter your task:")
priority_level = input("Priority (high,medium,low):").lower()
time_sensitivity = input("Is it time-bound? (yes/no):").lower()
match priority_level:
    case "high": 
        print(f"Reminder: {task} is a high priority task!", end=" ")
    case "medium":
        print(f"Reminder: {task} is a medium priority task", end=" ")
    case "low":
        print(f"Reminder: {task} is a low priority task.", end=" ")
if time_sensitivity == "yes":
    print("that requires immediate attention today!")
else:
    print("Consider completing it when you have free time.")

