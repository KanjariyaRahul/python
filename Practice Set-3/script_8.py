#  An online selling app wants to develop a application to calculate shipping charges on the
# purchase. Accept amount from the user and calculate the shipping charges.
# The shipping charges are as below:
# Shopping amount less than 1500 – The shipping charges is Rs. 100/-
# --Type the message: Please purchase (1500-amount) to avail shipping charge of Rs. 80/-
# --Please pay (amount+100)
# Shopping amount more than 1500 and less than 3000 – The shipping charges is Rs. 70/-
# --Type the message: Please purchase (3000-amount) to avail shipping charge of Rs. 50/-
# --Please pay (amount+70)
# Shopping amount more than 3000 – Free shipping + 7% discount on amount
# --Type a message: You saved (amount*7/100)
# --Please pay (amount – discount)

amount = float(input("Enter the shopping amount: "))

if amount < 1500:
    shipping_charge = 100
    print(f"Please purchase ",1500 - amount," more to avail shipping charge of Rs. 80/-")
    total_amount = amount + shipping_charge
elif amount < 3000:
    shipping_charge = 70
    print(f"Please purchase ",3000 - amount," more to avail shipping charge of Rs. 50/-")
    total_amount = amount + shipping_charge
else:
    shipping_charge = 0
    discount = amount * .07
    print(f"You saved Rs. ",discount)
    total_amount = amount - discount

print(f"Shipping charge: Rs." ,shipping_charge)
print(f"Total amount to pay: Rs.", total_amount)

