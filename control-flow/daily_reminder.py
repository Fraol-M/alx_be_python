single_task = input("Enter your task: ")

while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    else:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ["yes", "no"]:
        break
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{single_task}' is a high priority task that requires immediate attention today!") 
        else:
            print(f"Note: '{single_task}' is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{single_task}' is a medium priority task that requires some attention!") 
        else:
            print(f"Note: '{single_task}' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{single_task}' is a low priority task.") 
        else:
            print(f"Note: '{single_task}' is a low priority task. Consider completing it when you have free time.")
