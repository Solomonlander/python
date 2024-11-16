# Creativity used is to ask the user, if the child is under 18 by using boolean. if the user input yes, it will displayed "True", and also ask the user the age of the child and adult 
# the creativity used was to add the currency symbol to displayed in all the computed values
child_meal = float(input("what is the price of a child's meal?: $"))
adult_meal = float(input("what is the price of a adult's meal?: $"))
num_of_children = int(input("How many children are there?: $"))
num_of_adult = int(input("How many adult are there?: $"))
tax_rate = float(input("What is the sales tax rate?: $"))
sub_total = num_of_children * child_meal + num_of_adult * adult_meal
sales_tax = sub_total * tax_rate /100
total = sub_total + sales_tax
payment_amount = float(input("What is the payment amount?: $"))
change = payment_amount = total

# the age of the child and the age of the adult.
age_of_child = int(input("What are the age of the child? "))
age_of_adult = int(input("What are the age of the adult? "))

# asking the user, if the child is under age and if the adult is up to adult age.
are_there_under_18 = bool(input("Are there under 18: "))
are_there_of_adult_age = bool(input("Are there up to adult age: "))

print((f"The age of the child is between: {age_of_child}"))
print((f"The age of adult is between: {age_of_adult}"))
print((f"are there under 18: {are_there_under_18}"))
print((f"are there of adult age: {are_there_of_adult_age}"))
print((f"Subtotal is: ${sub_total}"))
print((f"Sales Tax is: ${sales_tax}"))
print((f"Total is: ${total}"))
print((f"Change is: ${change}"))