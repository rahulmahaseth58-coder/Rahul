#QN.1

# while True:
#     user_input = input("Enter your age: ")
#     if user_input =='stop':
#         print("program terminated.")
#         break  
#     age = int(user_input)
#     if age < 18:
#         print("you are a minor")
#     elif 18 <= age < 60:
#         print("You are an adult.")
#     else:
#         print("You are a senior citizen.")



    
#QN.2
    
# while(user_input:=input('enter a input:')!='bus'):
#     print('waiting')
# else:
#     print('wait is over')

#QN.3

# while  (user_input:=input('enter a fruit name:')) != 'apple':
#     print('try again')
# else:
#     print('you got it!')    

#QN.5

# ratings=['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
# content_ratings={}
# i=0
# while i < len(ratings):
    
#     if ratings[i] in content_ratings:
#         content_ratings[ratings[i]]=content_ratings.get(ratings[i],0)+1
#     else:
#         content_ratings[ratings[i]]=1
#     i+=1
# print(content_ratings)

#QN.6

# import random
# rn=random.randint(1,10)
# while True:
#     user=int(input('enter a number:'))
#     if rn==user:
#         print('congrats')
#         break
#     elif rn>user:
#         print('go higher')
#     else:
#         print('go lower')
        
        
#QN.7

# username = 'admin'
# password = '1234'
# count = 3
# while True:
#     user_input = input('enter your user name : ')
#     password_input = input('enter your password : ')

#     if count == 0:
#         print('your attempt is over ')
#         break
#     else:
#         if username == user_input and password == password_input:
#             print('login sucessful')
#             break
#         else:
#             count -=1
#             print(f'your password or user name is worng, attemped left {count}')
         

#QN.8


# from random import *

# a = randrange(1,11)

# while True:
#     user_guess = int(input('enter a number : '))
#     if( a ==  user_guess):
#         print('correct guess')
#         break
#     elif a < user_guess:
#         print('your guess is higher')
#     elif a > user_guess:
#         print('your guess in lower')

#QN.9


# while True:
#     user_num = input("Enter a number to check prime or 'exit' to stop: ")
    
#     if user_num.lower() == 'exit':
#         break
    
#     elif user_num.isdigit():
#         num = int(user_num)
        
#         if num <= 1:
#             print("Not prime")
#         else:
#             i = 2
#             while i < num:
#                 if num % i == 0:
#                     print("It is not prime")
#                     break
#                 i += 1
#             else:
#                 print("It is prime")
                
#     else:
#         print("Please enter properly")

#QN.10

# secret_word = 'python'

# while (user_input := input('guess the predefine word : ')) != 'quit':
#     if user_input != secret_word:
#         print('Incorrect, try again')
#     else:
#         print('Congratulations, you guessed the word!')
#         print('enter \'quit\'  if you want to exist')




#QN.11

# count = 0
# while True:
    
#     user_input = input('Enter your name : ').lower()
#     if user_input == 'good luck':
#         count+=1
#     if count == 3:
#         print(f'You typed the same word {count} times.')
#         break

#QN.12

floor = 1
while True:
    user_wants = input('Enter a floor number to want to go : ')
    if user_wants.isdigit():
        if int(user_wants) == 0:
            print('goodbye')
            break
        elif floor == int(user_wants):
            print('You are already here')
        elif floor < int(user_wants):
            print('going up')
            floor = int(user_wants)
        elif floor > int(user_wants):
            print('going down')
            floor = int(user_wants)
    else:
        print('enter a proper number')
