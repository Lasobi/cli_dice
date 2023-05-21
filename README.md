# Dice Roller
This is a simple Python script that simulates rolling a die (or multiple dice) a certain number of times.

## Requirements
* Python 3.6 or higher
* [PyInstaller](https://pyinstaller.org/en/stable/) for creating standalone executable

## Installation
You can install PyInstaller with pip:

    pip install pyinstaller


## Usage
Command line arguments:

-d, --num_sides: number of sides on the dice (default: 6)
-n, --num_rolls: number of times to roll the dice (default: 1)
Example:

    python dice_roller.py -d 6 -n 3

This command will simulate rolling a 6-sided die 3 times.

## Creating an Executable
You can create a standalone executable using PyInstaller. Run the following command:

    pyinstaller --onefile dice_roller.py

This will create a dist directory containing the dice_roller executable. You can run this executable without needing Python installed.

Example:

    ./dist/dice_roller -d 6 -n 3

## Output
The script will print the result of each die roll to the console. For example:

    Roll 1: 4
    Roll 2: 6
    Roll 3: 2

In this example, a 6-sided die was rolled 3 times. The results of the rolls were 4, 6, and 2.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
