email = input("What is your email address?:" ).strip()
user_name = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
res = f"Your username is '{user_name}' and your domain name is '{domain_name}'"
print(res)
