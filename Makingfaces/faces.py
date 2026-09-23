def main():
    # Prompt the user for input
    user_input = input("Enter text: ")
    
    # Convert the input
    converted_text = convert(user_input)
    
    # Print the result
    print(converted_text)

def convert(text):
    # Replace :) with the slightly smiling face emoji
    text = text.replace(":)", "🙂")
    
    # Replace :( with the slightly frowning face emoji
    text = text.replace(":(", "🙁")
    
    return text

if __name__ == "__main__":
    main()