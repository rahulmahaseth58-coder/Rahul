# st_name=[1,2,3,4,5]
# f=fliter(lambda x:x+2==,st_name)
# print(list(f))



# items = ['sql', '123', 'python']
# result = list(filter(lambda x: x.isalpha(), items))
# print(result)

#Q N.1
# items = ['sql', '123', 'python']

# result = list(filter(lambda x: x.isalpha(), items))
# print(result)

#Q N.2 
# products = [{'id': 1, 'name': 'laptop', 'category': 'electronics', 'price': 1200, 'instock': True},
#     {'id': 2, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock': False}]

# instock_products = list(filter(lambda p: p['instock'] == True, products))
# print(instock_products)


#Q N.3
# course = [{'title': 'Ancient Civilizations', 'genre': 'history'},
#           {'title': 'Corporate Finance', 'genre': 'commerce'},
#           {'title': 'Modern World History', 'genre': 'history'}]

# history_courses = list(filter(lambda c: c['genre'] == 'history', course))
# print(history_courses)

#Q N.4

# emails = [
#     'ram.sharma@gmail.com',
#     'spam@hooya.com',
#     'virus@malware.net',
#     'shyam.kumar@workcorp.com'
# ]

# blacklist = ('@hooya.com', '@malware.net')

# spam_emails = list(filter(lambda e: e.endswith(blacklist), emails))
# print(spam_emails)

#Q N.5

# price = [100, 50, 200, 75]

# discounted_price = list(map(lambda p: p * 0.8, price))
# print(discounted_price)

#Q N.6

# def skip_two(lst):
#     return lst[1:12:3]

# print(skip_two([1,2,3,4,5,6,7,8,9,10,11,12,13]))

#Q N.7

# def remove_at_idx(lst, idx):
#     return lst[:idx] + lst[idx+1:]

# print(remove_at_idx([10, 20, 30, 40], 2))


#Q N.8

# text = input("Enter a string: ")

# cleaned = ''.join(ch if ch.isalnum() else '#' for ch in text)
# print(cleaned)


#Q N.9 

# users_db = {}

# def register_user(username, password, email):
#     if username in users_db:
#         return "Username already exists"
#     users_db[username] = {'password': password, 'email': email}
#     return f"Registration successful for {username}"

# def login_user(username, password):
#     if username not in users_db:
#         return "User not found"
#     if users_db[username]['password'] != password:
#         return "Incorrect password"
#     return f"Welcome back, {username}"

# print(register_user('ram', 'ram123', 'ram@email.com'))
# print(register_user('shyam', 'shyam456', 'shyam@email.com'))
# print(register_user('hari', 'hari231', 'hari@email.com'))

# print(login_user('ram', 'ram123'))

#Q N.10

# inventory = [{'name': 'Laptop', 'price': 50000, 'quantity': 5}]

# total_value = sum(item['price'] * item['quantity'] for item in inventory)
# print("Total Inventory Value:", total_value)

#Q N.11

contacts = [{'name': 'Ram kc', 'phone': '9801234567', 'email': 'ram@email.com'}]

def valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def valid_email(email):
    return '@' in email and '.' in email

print(contacts)


