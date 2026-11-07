# sketch of the study app
import time

tasks = []

while True:
    print("\n1. Add Task  2. See Tasks  3. Start Timer  4. Exit")
    choice = input("Pick: ")

    if choice == "1":
        tasks.append(input("Task: "))
        print("Added!")

    elif choice == "2":
        print(tasks if tasks else "No task yet")

    elif choice == "3":
        mins = int(input("How many minutes? "))
        print("Go study! No phone...")
        time.sleep(mins * 60)
        print("Done! Take break 🎉")

    elif choice == "4":
        break

