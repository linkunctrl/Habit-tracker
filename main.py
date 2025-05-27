class Habit:
    def __init__(self, namep):
        self.name = namep
        self.dates = set()
        self.curr_streak = 0

    def add_activity(self, date: str):
        self.dates.add(date)
        
class HabitTracker:
    def __init__(self):
        self.habits = {}
        
    def add_habit(self, name):
        if name in self.habits:
            print(f"Habits '{name}' already exists.")
        else:
            self.habits[name] = Habit(name) # created an object of Habit and stored it in habits dictionary
            print(f"Habit '{name}' added successfully.")

    def remove_habit(self, name):
        if name not in self.habits:
            print(f"Habits '{name}' doesn't exist.")
        else:
            del self.habits[name]
            print(f"Habit '{name}' removed successfully.")

    def record_activity(self, name, date):
        if name not in self.habits:
            print(f"Habits '{name}' doesn't exist.")
        else:
            self.habits[name].add_activity(date)
            print(f"Date '{date}' added successfully for habit {name}.")


    def list_habits(self):
        if not self.habits:
            print("No habits found.")
        else:
            print("Tracked habits: ")
            for habit_name, habit_obj in self.habits.items():
                print(f" - {habit_name} , {habit_obj.dates}")


tracker = HabitTracker()
tracker.add_habit("walk")        
tracker.add_habit("pooping")
tracker.remove_habit("pooping")         
tracker.record_activity("walk", "2025-05-13")
tracker.list_habits()
tracker.add_habit("walk")