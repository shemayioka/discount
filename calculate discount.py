def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    :param price: Original price of the item.
    :param discount_percent: Discount percentage to be applied.
    :return: Final price after discount if applicable, otherwise the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount_percent)
    
    print(f"The final price after applying the discount is: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")
