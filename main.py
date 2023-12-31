import random

class KamalGame:
    def __init__(self):
        self.points = 0
        self.goal = random.randint(1, 100)

    def start(self):
        print("Welcome to the Kamal Game!")
        print(f"Your goal is to score {self.goal} points.")
        self.play()

    def play(self):
        while self.points < self.goal:
            points_scored = self.ask_for_points()
            self.points += points_scored
            print(f"Your total points are now {self.points}.")
            if self.points >= self.goal:
                print(f"Congratulations! You scored {self.points} points and reached your goal!")

    def ask_for_points(self):
        while True:
            try:
                points = int(input("Enter the number of points you scored (0 or positive number): "))
                if points >= 0:
                    return points
                else:
                    print("Invalid input. Please enter a positive number or 0.")
            except ValueError:
                print("Invalid input. Please enter a positive number or 0.")

game = KamalGame()
game.start()