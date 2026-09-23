def main():
    # Prompt the user for input
    user_input = input("Enter text: ")
    
    # Replace all spaces with three periods
    slowed_down = user_input.replace(" ", "...")
    
    # Output the modified string
    print(slowed_down)

if __name__ == "__main__":
    main()