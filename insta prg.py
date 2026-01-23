insta_accounts = {
    "neela_123": "123",
    "user202": "57",
    "priya_20": "2005",
    "arun_ig": "29@0",
    "dev_02": "56*"
}
name = input("Enter ID: ")
if name in insta_accounts:
    print("ID matched ")
    pass_id = input("Enter password: ")

    if pass_id == insta_accounts[name]:
        print("Password matched")
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("ID not found")
    print("Create an account")
























"""
insta_ids = ["neela_123", "user202", "priya_20","arun_ig","dev_02"]
password = ["123","57","2005","29@0","56*"]
name = input("enter ID:")
pass_id = input("enter password:")
if name in insta_ids:
    print("name matched")
elif pass_id in password:
    print("password matched")
else:
    print("ID not found")
    print("create an account")
"""