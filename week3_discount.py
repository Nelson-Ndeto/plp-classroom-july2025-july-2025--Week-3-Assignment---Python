
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If discount_percent is 20% or higher, apply the discount,
    otherwise return the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price


# --- Main program ---
try:
    # Get input from the user
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(original_price, discount_percent)

    # Output result
    print(f"\nFinal Price: {final_price:.2f}")

except ValueError:
    print("❌ Please enter valid numeric values for price and discount percentage.")
