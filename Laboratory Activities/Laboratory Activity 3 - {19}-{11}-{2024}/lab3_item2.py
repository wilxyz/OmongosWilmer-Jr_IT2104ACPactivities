def is_perfect_number(n):
    """
    Check if a number is a perfect number.
    A perfect number is a number that is equal to the sum of its proper divisors (excluding itself).
    """
    if n <= 1:
        return False  # 1 and any negative number are not perfect numbers

    # Find divisors and check if their sum equals n
    divisors_sum = sum(i for i in range(1, n // 2 + 1) if n % i == 0)

    return divisors_sum == n

def main():
    try:
        num = int(input("Enter a number: "))
        
        if num <= 0:
            print("Please enter a positive integer.")
        else:
            result = "is" if is_perfect_number(num) else "is not"
            print(f"{num} {result} a perfect number.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
