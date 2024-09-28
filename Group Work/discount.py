import datetime

def get_day_of_week():
    return datetime.datetime.now().strftime("%A")

def apply_discount(subtotal, day_of_week):
    discount = 0
    if day_of_week in ["Tuesday", "Wednesday"] and subtotal >= 50:
        discount = 0.10 * subtotal
        subtotal -= discount
    return subtotal, discount

def calculate_sales_tax(subtotal, tax_rate=0.06):
    return subtotal * tax_rate

def main():
    subtotal = float(input("Please enter the subtotal: "))
    
    # Get the current day of the week
    day_of_week = get_day_of_week()
    
    # Apply discount if applicable
    updated_subtotal, discount = apply_discount(subtotal, day_of_week)
    
    # Calculate sales tax and total
    sales_tax = calculate_sales_tax(updated_subtotal)
    total_due = updated_subtotal + sales_tax
    
    # Output the results
    if discount > 0:
        print(f"Discount amount: ${discount:.2f}")
    print(f"Sales tax: ${sales_tax:.2f}")
    print(f"Total amount due: ${total_due:.2f}")
    
    # Stretch challenge: If it's Tuesday or Wednesday, inform the customer how much more they need to spend for the discount
    if day_of_week in ["Tuesday", "Wednesday"] and subtotal < 50:
        amount_needed = 50 - subtotal
        print(f"You need to spend ${amount_needed:.2f} more to qualify for a discount.")

# Stretch Challenge: Allow repeated inputs to compute subtotal from multiple items
def calculate_subtotal_from_items():
    subtotal = 0
    while True:
        price = float(input("Enter the price of the item (or 0 to finish): "))
        if price == 0:
            break
        quantity = int(input("Enter the quantity of the item: "))
        subtotal += price * quantity
    return subtotal

if __name__ == "__main__":
    # Uncomment below line for the stretch challenge
    subtotal = calculate_subtotal_from_items()

    main()
