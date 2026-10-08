# Get the greeting from the user, remove leading/trailing spaces, and convert to lowercase
greeting = input("Greeting: ").strip().lower()

# First, check if the greeting starts with the full word "hello"
if greeting.startswith("hello"):
    # Output $0 as promised by the bank
    print("$0")
# If it didn't start with "hello", check if it still starts with the letter "h"
elif greeting.startswith("h"):
    # Output $20 for greetings like "hey" or "howdy"
    print("$20")
# If it starts with anything else
else:
    # Output $100
    print("$100")