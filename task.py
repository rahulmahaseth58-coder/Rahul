# Q no 1
# num1=int(input('enter first number'))
# num2=int(input('enter second number'))
# num3=int(input('enter third number'))
# if num1>num2 or num1>num3:
#     print('num1 is greatest')
# elif num2>num1 or num2>num3:
#     print('num2 is greatest')
# elif num3>num1 or num3>num2:
#     print('num3 is greatest')
# else:
#     print('all are equal')    
    
# Q no 2
# month = int(input("Enter month number (1-12): "))

# if month == 1:
#     print("January")
# elif month == 2:
#     print("February")
# elif month == 3:
#     print("March")
# elif month == 4:
#     print("April")
# elif month == 5:
#     print("May")
# elif month == 6:
#     print("June")
# elif month == 7:
#     print("July")
# elif month == 8:
#     print("August")
# elif month == 9:
#     print("September")
# elif month == 10:
#     print("October")
# elif month == 11:
#     print("November")
# elif month == 12:
#     print("December")
# else:
#     print("Invalid month number.")

# Q no 3
# num1=int(input('enter first number'))
# num2=int(input('enter second number'))
# num1,num2= num2,num1
# print(num1,num2)

#Q no 4
# age=int(input("enter a person age: "))
# if age<12:
#     print('ticket is free')
# elif age>=12 and age<=60:
#     membership_card=input('do the person have a member card: ')
#     if membership_card=='yes':
#         price=150
#     else:
#         price=200
#     print(price)
# else:
#     price=100
#     print(price)
    
# Q no 5
# unit=int(input("enter unit used"))
# if unit < 100:
#     usage=unit*5
# elif unit<=300:
#     first100=100*5
#     next_unit=(unit-100)*8
#     usage=first100 + next_unit
# else:
#     frist_100=100*5
#     next_200=200*8
#     nextunit=(unit-300)*10
#     usage=nextunit+next_200+frist_100
# print("the total amount of units is",usage)
# output: The total amount of units is <calculated_amount>ems={'shyam',1,'ram'}

# Q no 6
# user_1=input("user 1 : Enter rock, paper or scissor: ").lower()
# user_2=input("user 2: Enter rock, paper or scissor: ").lower()
# if user_1==user_2:
#     print("draw")
# else:
#     if user_1=="rock":
#         if user_2=="scissor":
#             print("user1 wins")
#         else:                                                                          

#             print("user2 wins")
#     else:
#         if user_1=="paper":
#             if user_2=="rock":
#                 print("user1 wins")
#             else:
#                 print("user 2 wins")

#         else:
#             if user_1=="scissor":
#                 if user_2=="paper":
#                     print("user_1 wins")
#                 else:
#                     print("user_2 wins")
#             else:
#                 print("invalid")    
                #output: invalid
                
# Q no 7
# class_a=int(input("enter number of student in class a"))                                            
# class_b=int(input("enter number of student in class b"))                                            
# class_c=int(input("enter number of student in class c"))                                            

# desk_a = (class_a+1)//2
# desk_b = (class_b + 1)//2
# desk_c= (class_c + 1) //2

# total_desk = desk_a + desk_b + desk_c
# print("total number of desk is : ",total_desk)

#Q no 8

# lift = 5
# floor = int(input('enter a floor number to move lift : '))
# if(0<=floor<lift):
#     print('lift will go down')
# elif(floor>lift):
#     print('lift will go up')
# else:
#     print('enter proper number ')
    
#Q no 9
# num=int(input("enter a number"))
# if num>=0:
#     if num%2==0:
#         print('even')
#     else:
#         print("odd")

# elif num<0:
#     print("negative number")
# else:
#     print("zero")

#Q no 10

# if num1==num2:
#     print("equal")
#     if num1>0:
#         print("positive")
#     elif num1<0:
#         print("negative")
#     else:
#         print("zero")
# elif num1>num2:
#     print("num1 is greater")
# else:
#     print("num2 is grater")
    
#Q no 11

# num1=int(input("enter a number"))
# if num1%3==0 and num1%5==0:
#     print("Fizz Buzz")
# elif num1%3==0 and num1%5!=0:
#     print("Fizz")
# elif num1%3!=0 and num1%5==0:
#     print("Buzz")
# else:
#     print(num1)

#Q no 12


# import random 

# fact= random.randint(0,5)

# if fact ==0:
#     print("Flamingos turn pink from eating shrimp")

# elif fact == 1:
#     print("The only food that doesn't spoil is honey.")
# elif fact == 2:
#     print("Shrimp can only swim backwards.")
# elif fact == 3:
#     print("A taste bud's life span is about 10 days.")
# elif fact == 4:
#     print("It is impossible to sneeze while sleeping.")
# else: 
#     print("It is illegal to sing off-key in North Carolina.")
    
# Q no 13

# amount = float(input("Enter the total purchase amount: "))
# membership = input("Are you a member? (yes/no): ").lower()

# if membership == "yes":
#     ismember = True
# elif membership == "no":
#     ismember = False
# else:
#     print("for member only")
#     ismember = False

# if amount > 1000:
#     if ismember:
#         discount = amount * 0.20
#         finalamount = amount - discount
#         print(f"Member discount applied: 20%  {discount:.2f}")
#     else:

#         discount = amount * 0.10
#         finalamount = amount - discount
#         print(f"Non-member discount applied: 10% {discount:.2f}")
# else:
#     final_amount = amount
#     print("No discount applicable (purchase amount ≤  1000)")

# print(f"Final amount to pay:  {final_amount:.2f}")

# Q no 14

# earth_weight = float(input("What is your Earth weight? "))
# planet = int(input("Enter planet number from 1-7: "))


# if planet == 1:
#     relative_gravity = 0.38
#     planet_name = "Mercury"
# elif planet == 2:
#     relative_gravity = 0.91
#     planet_name = "Venus"
# elif planet == 3:
#     relative_gravity = 0.38
#     planet_name = "Mars"
# elif planet == 4:
#     relative_gravity = 2.53
#     planet_name = "Jupiter"
# elif planet == 5:
#     relative_gravity = 1.07
#     planet_name = "Saturn"
# elif planet == 6:
#     relative_gravity = 0.89
#     planet_name = "Uranus"
# elif planet == 7:
#     relative_gravity = 1.14
#     planet_name = "Neptune"
# else:

#     print("Invalid planet number")
    


# destination_weight = earth_weight * relative_gravity

# print(f"Your weight on {planet_name} would be {destination_weight}")

# Q no 15

# num1 = float(input('enter marks of 1st subject : '))
# num2 = float(input('enter marks of 2nd subject : '))
# num3 = float(input('enter marks of 3rd subject : '))
# num4 = float(input('enter marks of 4th subject : '))

# marks = num1+num2+num3+num4
# if 0>marks>100:
#     print('mark is invalid')
# elif(90<=marks<=100):
#     print('Grade is A+')
# elif(80<=marks<=89):
#     print('Grade is A')
# elif(70<=marks<=79):
#     print('Grade is B+')
# elif(60<=marks<=69):
#     print('Grade is B')
# elif(50<=marks<=59):
#     print('Grade is C+')
# elif(40<=marks<=49):
#     print('Grade is c')
# else:
#     print('grade is fail')

# Q no 16

# from random import *

# price = randrange(40000,500000)
# print(price)

# if price>100000 :
#     print(f'road tax is 15% so rs {price*15/100} is tax')
# elif 50000< price <=100000:
#     print(f'road tax is 10% so rs {price*10/100} is tax')
# elif(price<50000):
#     print(f'road tax is 5% so rs {price*5/100} is tax')

#Q no 17

# from random import *

# time = randint(1,15)
# print(time)

# if time>10 :
#     print('bonus is 10%')
# elif 6<=time<=10:
#     print('bonus is 8%')
# elif time<6:
#     print('bonus is 5%')

# Q no 18

# score = float(input('enter the subject score : '))

# if score>90:
#     print('congratulation')
# elif 50<=score<=90:
#     print('nexttime you will do it better with hardwork.')
# else:
#     print('you should take retake')

# Q no 19
# age = int(input('enter your age : '))

# if age>=18:
#     degree = input('do you have degree (yes/no) : ')
#     if degree == 'yes':
#         experience = int(input('any work exprience? say in time : '))
#         if experience > 3:
#             print('highly egligible')
#         elif(1<=experience<=3):
#             print('eligible')
#         else:
#             print('under review')
        
#     elif degree == 'no':
#         print('degree is needed')
#     else:
#         print('enter yes or no')
# else:
#     print('your age is not egible')

# Q no 20

# age = int(input('enter your age : '))

# if 18<=age<30:
#     gender = input('enter your gender (Male/Female): ').lower()
#     days = int(input('enter your worked : '))

#     if gender[0] == 'm':
#         wage = 700
#         print(f'your work days wage is 700 so you\'ll get {wage*days}')
#     elif gender[0] == 'f':
#         wage = 750
#         print(f'your work days wage is 750 so you\'ll get {wage*days}')
#     else:
#         print('enter male or female')
# elif 30<=age<=40:
#     gender = input('enter your gender (Male/Female): ').lower()
#     days = int(input('enter your worked : '))

#     if gender[0] == 'm':
#         wage = 800
#         print(f'your work days wage is 800 so you\'ll get {wage*days}')
#     elif gender[0] == 'f':
#         wage = 850
#         print(f'your work days wage is 850 so you\'ll get {wage*days}')
#     else:
#         print('enter male or female')

# else:
#     print('enter your age properly')

# Q no 21

# balance = 50000
# pin = 123

# print('card is vallid : ')
# enter_pin= int(input('enter pin : '))

# if pin == 123:
#     print('(1) withdraw\n(2) check balance\n(3) exit')

#     wants = int(input('press number what you want to do : '))
#     if wants == 1 :
#         withdraw = float(input('how much you want to with draw : '))
#         if(withdraw <= balance):
#             print(f'heres yours your money and your balance is {balance - withdraw}')
#         else:
#             print('you don\'t have enough balance')
#     if wants == 2 :
#         print(f'your balance is {balance}')
#     if wants == 3 :
#         print('thanks for visiting')
# else:
#     print('pin is invalid')

# Q no 22

# print("Welcome to the Magic Forest")

# choice1 = input("Do you want to go 'north' or 'south'? : ").lower()
# if choice1 == "south":
#     print("Game Over")
# elif choice1 == "north":
#     choice2 = input("Do you want to 'cross the river' or 'follow the path'? : ").lower()
#     if choice2 == "cross the river":
#         print("Game Over")
#     elif choice2 == "follow the path":
#         choice3 = input("Choose 'fairy', 'ogre', or 'elf': ").lower()
#         if choice3 == "elf":
#             print("You Win")
#         elif choice3 == "fairy" or choice3 == "ogre":
#             print("Game Over")
#         else:
#             print("Invalid choice")
#     else:
#         print("Invalid choice")
# else:
#     print("Invalid choice")

# Q no 23

print("Welcome to the Haunted House")

choice1 = input("Do you want to go 'upstairs' or 'downstairs'? : ").lower()

if choice1 == "downstairs":
    print("Game Over")

elif choice1 == "upstairs":
    choice2 = input("Do you want to 'enter the room' or 'stay outside'? : ").lower()

    if choice2 == "enter the room":
        print("Game Over")

    elif choice2 == "stay outside":
        choice3 = input("Choose 'ghost', 'vampire', or 'werewolf': ").lower()

        if choice3 == "werewolf":
            print("You Win")
        elif choice3 == "ghost" or choice3 == "vampire":
            print("Game Over")
        else:
            print("Invalid choice")

    else:
        print("Invalid choice")

else:
    print("Invalid choice")