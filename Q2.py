#sp25-bse-049
import random
import pandas as pd
import numpy as np

def water_needed(moisture, target=80):

    if moisture < target:
        return target - moisture
    else:
        return 0


for moisture in [30, 55, 85]:
    print("Water Needed:", water_needed(moisture))

print("Custom Target:", water_needed(30, 60))




random.seed(5)

tank = 30
plants_watered = 0
plant_number = 1

while tank >= 5:

    water = random.randint(2, 6)

    tank = tank - water

    plants_watered += 1

    print("Plant Number:", plant_number)
    print("Water Used:", water)
    print("Water Left:", tank)

    plant_number += 1

print("Total Plants Watered:", plants_watered)
print("Tank almost empty. Going to refill.")



class Plant:

    def __init__(self, plant_id, plant_type, moisture):

        self.plant_id = plant_id
        self.plant_type = plant_type
        self.moisture = moisture

    def needs_water(self):

        return self.moisture < 40

    def water(self):

        self.moisture = 80

    def display(self):

        print(self.plant_id, self.plant_type, self.moisture)


class WateringRobot:

    total_robots = 0

    def __init__(self, name, water=10):

        self.name = name
        self.water = water
        self.plants_watered = 0

        WateringRobot.total_robots += 1

    def water_plant(self, plant):

        if self.water < 2:

            print("Tank empty")

        elif plant.needs_water():

            plant.water()
            self.water -= 2
            self.plants_watered += 1

            print(plant.plant_id, "Watered")

        else:

            print(plant.plant_id, "does not need water")

    def show_status(self):

        print("Robot:", self.name)
        print("Water Left:", self.water)
        print("Plants Watered:", self.plants_watered)


plants_list = [
    Plant("R1-P1", "Mint", 55),
    Plant("R2-P4", "Chili", 35),
    Plant("R3-P1", "Tomato", 26),
    Plant("R1-P2", "Rose", 80)
]

robot1 = WateringRobot("Aqua-1")

robot2 = WateringRobot("Aqua-2", 3)


print("\nRobot 1")

for plant in plants_list:

    robot1.water_plant(plant)


print("\nRobot 2")

plant1 = Plant("R3-P3", "Chili", 35)
plant2 = Plant("R3-P4", "Mint", 36)

robot2.water_plant(plant1)
robot2.water_plant(plant2)


robot1.show_status()
robot2.show_status()

print("Total Robots:", WateringRobot.total_robots)




df = pd.read_csv("greenhouse_clean.csv")

df = df.sort_values(["Row", "Pot_No"])

grid = np.array(df["Soil_Moisture"]).reshape(3, 5)



class SimpleReflexRobot:

    def __init__(self):

        self.score = 0
        self.moves = 0

    def act(self, percept):

        r, p, moisture = percept

        if moisture < 40:
            return "Water"
        else:
            return "Move"


print("\nSimple Reflex Agent")

world = grid.copy()

robot = SimpleReflexRobot()

for step in range(30):

    r = (step // 5) % 3
    p = step % 5

    percept = (r + 1, p + 1, world[r, p])

    action = robot.act(percept)

    robot.score -= 1

    if action == "Water":

        world[r, p] = 80

        robot.score += 10

        print("Step:", step + 1,
              "Row:", r + 1,
              "Pot:", p + 1)

    else:

        robot.moves += 1


print("Total Moves:", robot.moves)
print("Final Score:", robot.score)




class ModelBasedRobot:

    def __init__(self):

        self.score = 0
        self.moves = 0

        self.model = np.full((3, 5), -1)

    def update_state(self, r, p):

        self.model[r, p] = 0

    def act(self, percept):

        r, p, moisture = percept

        if np.all(self.model == 0):

            return "NoOp"

        elif moisture < 40:

            return "Water"

        else:

            return "Move"


print("\nModel-Based Agent")

world = grid.copy()

robot = ModelBasedRobot()

for step in range(30):

    r = (step // 5) % 3
    p = step % 5

    percept = (r + 1, p + 1, world[r, p])

    action = robot.act(percept)

    robot.score -= 1

    if action == "NoOp":

        print("All pots visited. Robot stops.")

        break

    if action == "Water":

        world[r, p] = 80

        robot.score += 10

        print("Step:", step + 1,
              "Row:", r + 1,
              "Pot:", p + 1)

    else:

        robot.moves += 1

    robot.update_state(r, p)


print("Total Moves:", robot.moves)
print("Final Score:", robot.score)

