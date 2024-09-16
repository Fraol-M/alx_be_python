task_d = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

if task_priority == "high":
    if time == "yes":
        print(f"Reminder: '{task_d}' is a high priority task that requires immediate attention today!") 
    else:
        print(f"Note: '{task_d}' is a high priority task. Consider completing it when you have free time.")
elif task_priority == "medium":
    if time == "yes":
        print(f"Reminder: '{task_d}' is a medium priority task that requires some attention!") 
    else:
        print(f"Note: '{task_d}' is a medium priority task. Consider completing it when you have free time.")
else:
    if time == "yes":
        print(f"Reminder: '{task_d}' is a low priority task.") 
    else:
        print(f"Note: '{task_d}' is a low priority task. Consider completing it when you have free time.")