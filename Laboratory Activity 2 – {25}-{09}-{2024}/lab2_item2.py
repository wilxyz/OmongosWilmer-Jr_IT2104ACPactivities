def calculate_discount(purchase_amount):
    if purchase_amount > 5000:
        discount = 0.10
    else:
        discount = 0.05
    
    discount_amount = purchase_amount * discount
    final_price = purchase_amount - discount_amount
    
    print(f"Initial Purchase Amount: {purchase_amount:.2f}")
    print(f"Discount: {discount_amount:.2f}")
    print(f"Final Price: {final_price:.2f}")
    
def main():
    while True:
       
        purchase_amount = float(input("Enter the total purchase amount: "))
        
        calculate_discount(purchase_amount)
        
        try_again = input("Do you want to try again? (yes/no): ").lower()
        if try_again != "yes":
            print("Thank you!")
            break

main()