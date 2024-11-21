def roman_to_integer(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    roman = roman.upper()
    total = 0
    prev_value = 0

    for char in roman:
        current_value = roman_values.get(char)
        if current_value is None:
            return None  # Return None if invalid character is found
        
        if current_value > prev_value:
            total += current_value - 2 * prev_value  # Adjust total for cases like IV, IX
        else:
            total += current_value

        prev_value = current_value

    return total

def main():
    roman = input("Enter a Roman numeral: ").strip()
    result = roman_to_integer(roman)
    
    if result is None:
        print("Invalid Roman numeral entered.")
    else:
        print(f"The integer value of '{roman.upper()}' is: {result}")

if __name__ == "__main__":
    main()