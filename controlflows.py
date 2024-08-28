def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if the discount is 20% or higher.
    
    :param price: Original price of the item
    :param discount_percent: Discount percentage to be applied
    :return: Final price after discount if applicable, else the original price
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user to enter the original price and discount percentage
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(price, discount_percent)

    # Print the final price or the original price
    if discount_percent >= 20:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")