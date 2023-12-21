import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
available_fonts = figlet.getFonts()

if len(sys.argv) > 1:
    if sys.argv[1] == "--font" or sys.argv[1] == "-f":
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage")
else:
    font = random.choice(available_fonts)

if font not in available_fonts:
    sys.exit("Invalid usage")

text = input("Input: ")

figlet.setFont(font=font)

changedtext = figlet.renderText(text)

print(f"Output: {changedtext}")
