# Ask the user for the math expression 
expression = input("Expression: ").strip()

# Split the string at the spaces into 3 variables: x (1st number), y (operator), z (2nd number)
x, y, z = expression.split(" ")

# Convert x and z from text strings into decimal numbers 
x = float(x)
z = float(z)

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
# final answer 
print(f"{result:.1f}")