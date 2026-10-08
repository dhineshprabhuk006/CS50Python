# Ask the user for input, remove extra spaces around it (.strip), and make it all lowercase (.lower)
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

# Check if the cleaned input matches any of the three valid answers
if answer == "42" or answer == "forty-two" or answer == "forty two":
    # If it matches at least one, print Yes
    print("Yes")
# Otherwise, for any other input
else:
    # Print No
    print("No")