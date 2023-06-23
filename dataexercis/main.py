# numbers = str(input("Please enter two numbers "))
#
# number1 = int(numbers[0])
# number2 = int(numbers[1])
#
# sum_of_numbers = int(number1 + number2)
#
# print(sum_of_numbers)
#To round a number you use the round function
# in python which is an in-built library
# in python that helps to ease the rounding
# of numbers

#+= takes the previous value of a variable
#and print out the result

#FORMAT STRING here you easily concatinate
#a different dataypes to ease development
# name_of_school = "good"
# print(f'Your school is {name_of_school}')
# #print(round(2/3, 4))

#The program here tells you how many days,
#weeks and months you are lefft to live if
# you are supposed to live for 90 years
# based on your current age

#
# current_age = int(input("Please enter your current age \n"))
# number_of_years_left_to_live = 90-current_age
# number_of_months_left_to_live = number_of_years_left_to_live*12
# number_of_weeks_left_to_live = number_of_months_left_to_live*4
# number_of_days_left_to_live = number_of_weeks_left_to_live*7
#
# print(f"You are left with {number_of_years_left_to_live} years if you want to live for 90 years, \n"
#       f" You are let with {number_of_months_left_to_live} months if you are to live for 90 years\n"
#       f"You are left with {number_of_weeks_left_to_live} weeks if you are to live for 90 years\n"
#       f"You are left with {number_of_days_left_to_live} days if you are to live for 90 years")


# Tip calculator

# print("Welcome to the tip calculator. \n")
#
# Total_bill = int(input("What was the total bill? $"))
#
# percentage_tip = int(input(f"What percentage tip would you like to give? {10}, {12} or {15}? "))
#
# number_of_people = int(input("How many people to slit the bill? "))
#
# if percentage_tip == 10:
#     person_person = ((Total_bill)*(1/10))
#     bill_per_person = Total_bill/number_of_people
#     print(f"Each person has to pay: ${bill_per_person} and the tip {person_person} ")
# elif percentage_tip == 12:
#     person_pay = ((Total_bill)*(3/25))
#     bill_per_person = Total_bill/number_of_people
#     print(f"Each person has to pay: ${bill_per_person}  and the tip {person_pay}")
# elif percentage_tip ==15:
#     amount_to_pay = ((Total_bill)*(3/20))
#     bill_per_person = Total_bill/number_of_people
#     print(f"Each person has to pay: ${bill_per_person}  and the tip {amount_to_pay} ")
# else:
#     print("Please enter a logical input")


#Vitual hourse program

# import random
# print("\t\t\t\t\t\t\t|-------------------------------------------------------------------------------|")
# print("\t\t\t\t\t\t\t|                                                                               |")
# print("\t\t\t\t\t\t\t|   ------------Head or tail based on the random number generator-----------   |")
# print("\t\t\t\t\t\t\t|                                                                               |")
# print("\t\t\t\t\t\t\t|-------------------------------------------------------------------------------|")
# min_val = int(input("\t\t\t\t\t\t\t\t\t\t\tEnter your min_val\n"))
# max_val = int(input("\t\t\t\t\t\t\t\t\t\t\tEnter your max_val\n"))
#
# random_number =random.randint(min_val, max_val)
#
# print("\t\t\t\t\t\t\t\t\t\t\tThe random number is:", random_number)
#
# if max_val < 4 and min_val > 4:
#     print("\t\t\t\t\t\t\t\t\t\t\tYou are out of range")
#
# elif  random_number == 4:
#     print("\t\t\t\t\t\t\t\t\t\t\tHead")
# else:
#     print("\t\t\t\t\t\t\t\t\t\


