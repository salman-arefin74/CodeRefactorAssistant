# code_smells_example.py

def function_a():
    # Function with a line count of 40 (no complex logic)
    print("Line 1")
    print("Line 2")
    print("Line 3")
    print("Line 4")
    print("Line 5")
    print("Line 6")
    print("Line 7")
    print("Line 8")
    print("Line 9")
    print("Line 10")
    print("Line 11")
    print("Line 12")
    print("Line 13")
    print("Line 14")
    print("Line 15")
    print("Line 16")
    print("Line 17")
    print("Line 18")
    print("Line 19")
    print("Line 20")
    print("Line 21")
    print("Line 22")
    print("Line 23")
    print("Line 24")
    print("Line 25")
    print("Line 26")
    print("Line 27")
    print("Line 28")
    print("Line 29")
    print("Line 30")
    print("Line 31")
    print("Line 32")
    print("Line 33")
    print("Line 34")
    print("Line 35")
    print("Line 36")
    print("Line 37")
    print("Line 38")
    print("Line 39")
    print("Line 40")

def function_b():
    # Function with high cyclomatic complexity (15)
    x = 0
    if x == 1:
        print("Branch 1")
    elif x == 2:
        print("Branch 2")
    elif x == 3:
        print("Branch 3")
    elif x == 4:
        print("Branch 4")
    elif x == 5:
        print("Branch 5")
    elif x == 6:
        print("Branch 6")
    elif x == 7:
        print("Branch 7")
    elif x == 8:
        print("Branch 8")
    elif x == 9:
        print("Branch 9")
    elif x == 10:
        print("Branch 10")
    elif x == 11:
        print("Branch 11")
    elif x == 12:
        print("Branch 12")
    elif x == 13:
        print("Branch 13")
    elif x == 14:
        print("Branch 14")
    else:
        print("Branch 15")

def function_c():
    # Simple function with 3 lines of code and no complexity
    x = 1
    y = 2
    print("Sum:", x + y)

def process_user_data(users):
    for user in users:
        if user["is_active"]:
            print(f"Processing active user: {user['name']}")
            if "address" in user:
                print(f"Address found: {user['address']}")
            else:
                print("Address not found")
            if user["role"] == "admin":
                print(f"Granting admin privileges to {user['name']}")
                # Simulate granting privileges
            elif user["role"] == "user":
                print(f"Granting user privileges to {user['name']}")
                # Simulate granting privileges
            else:
                print(f"Unknown role for {user['name']}")
            print(f"Email sent to {user['email']}")
        else:
            print(f"Skipping inactive user: {user['name']}")