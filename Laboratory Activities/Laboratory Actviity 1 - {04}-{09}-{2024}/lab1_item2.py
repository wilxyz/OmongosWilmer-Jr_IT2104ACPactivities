char1, char2 = input("Enter two space-separated characters: ").split()

large_char = max(char1, char2)

print("-----------------------------------------")
print(f"The character with greater value is: {large_char}")
print("-----------------------------------------")
print("This part is optional to include.")

asciiVal1 = ord(char1)
asciiVal2 = ord(char2)

print("Showing ASCII Values: ")
print(f"{char1} : {asciiVal1}")
print(f"{char2} : {asciiVal2}")
