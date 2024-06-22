# Password Checker

password = "Secure3pass"

if len(password) < 6:
  strength = "Weak"
elif len(password) <= 10:
  strength = "Medium"
else:
  strength = "Strong"

print("Password strength is ", strength)