# This line imports the Calculator class from another file.
# Think of it as bringing in a reusable tool that can run the calculator REPL.
from app.calculator import Calculator

# This part of the code is super important! It checks if this file is being run directly by the computer.
# Let me explain: when we write Python programs, sometimes we want to run them directly,
# and other times we just want to use parts of the program inside other programs.
# The "__name__" is a special word in Python. It tells us if we are running the program directly.
# "__main__" is what Python calls this program when we run it directly.

# So, what this line means is: "If you're running this program directly
# (not as part of another program), then start the calculator."
if __name__ == "__main__":
    # Create the calculator and run the REPL.
    Calculator().run()
