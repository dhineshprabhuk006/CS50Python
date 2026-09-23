def main():
    # Prompt the user for mass as an integer
    m = int(input("m: "))
    
    # Speed of light in meters per second
    c = 300000000
    
    # Calculate energy in Joules (E = mc^2)
    E = m * (c ** 2)
    
    # Output the calculated energy
    print("E:", E)

if __name__ == "__main__":
    main()