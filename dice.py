import random
import argparse

def roll_dice(num_sides, num_rolls):
    results = []
    for i in range(num_rolls):
        roll = random.randint(1, num_sides)
        results.append(roll)
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Roll a dice of d sides n amount of times.")
    parser.add_argument("-d", "--num_sides", type=int, default=6, help="number of sides on the dice (default: 6)")
    parser.add_argument("-n", "--num_rolls", type=int, default=1, help="number of times to roll the dice (default: 1)")
    args = parser.parse_args()

    if args.num_sides < 2:
        raise ValueError("Number of sides must be at least 2.")
        exit(1)

    if args.num_rolls < 1:
        raise ValueError("Number of rolls must be at least 1.")
        exit(1)

    rolls = roll_dice(args.num_sides, args.num_rolls)
    for i, roll in enumerate(rolls, start=1):
        print(f"Roll {i}: {roll}")
