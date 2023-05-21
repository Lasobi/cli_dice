import random
import argparse

def roll_dice(num_sides, num_rolls):
    for i in range(num_rolls):
        roll = random.randint(1, num_sides)
        print(f"Roll {i+1}: {roll}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Roll a dice of x sides x amount of times.")
    parser.add_argument("-d", "--num_sides", type=int, default=6, help="number of sides on the dice (default: 6)")
    parser.add_argument("-n", "--num_rolls", type=int, default=1, help="number of times to roll the dice (default: 1)")
    args = parser.parse_args()

    roll_dice(args.num_sides, args.num_rolls)
