# Movie Ticket Pricing
age = int(input("Your age in years"))
day = input("Is today Wednesday y/n")

ticket_price = 12 if age >= 18 else 8


if day == "yes" or day == "y":
  # ticket_price = ticket_price - 2
  ticket_price -= 2

print("Your ticket price is $", ticket_price)