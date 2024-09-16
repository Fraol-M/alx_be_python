single_task = input("Enter your task: ")

while True:
    priority_level = input("Priority (high/medium/low): ").lower()
    if priority_level in ["high", "medium", "low"]:
        break
    else:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

while True:
    time_sensitive = input("Is it time-bound? (yes/no): ").lower()
    if time_sensitive in ["yes", "no"]:
        break
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")

match priority_level:
    case "high":
        if time_sensitive == "yes":
            print(f"Reminder: '{single_task}' is a high priority task that requires immediate attention today!") 
        else:
            print(f"Note: '{single_task}' is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if time_sensitive == "yes":
            print(f"Reminder: '{single_task}' is a medium priority task that requires some attention!") 
        else:
            print(f"Note: '{single_task}' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if time_sensitive == "yes":
            print(f"Reminder: '{single_task}' is a low priority task.") 
        else:
            print(f"Note: '{single_task}' is a low priority task. Consider completing it when you have free time.")
