import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.match(pattern, email):
        return "Valid Email ✅"
    else:
        return "Invalid Email ❌"


while True:
    email = input("Enter email (or type 'exit' to quit): ")
    
    if email.lower() == "exit":
        print("Program ended.")
        break
    
    result = validate_email(email)
    print(result)

    