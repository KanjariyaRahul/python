
yearly_income = float(input("Enter the yearly income earned by the taxpayer (in lakhs): "))


if yearly_income <= 8:
    tax = 0
    print("Tax to be paid: ₹", tax, " lakhs")

elif yearly_income > 8 and yearly_income <= 10:
    tax = 0.15 * yearly_income
    print("Tax to be paid: ₹", tax, " lakhs")
    
elif yearly_income > 10 and yearly_income <= 20:
    tax = 0.20 * yearly_income
    print("Tax to be paid: ₹", tax, " lakhs")
    
else:
    tax = 0.30 * yearly_income
    print("Tax to be paid: ₹", tax, " lakhs")
