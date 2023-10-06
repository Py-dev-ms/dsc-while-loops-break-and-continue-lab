slices_of_pie = 6
slices_eaten = 0

# for slice in range(slices_of_pie):
#     print('Another slice eaten!')
#     slices_eaten += 1
#     print('Now eaten {} slices!'.format(slices_eaten))

# while slices_eaten < len(range(0, slices_of_pie)):
#     print('Another slice eaten!')
#     slices_eaten += 1
#     print('Now eaten {} slices!'.format(slices_eaten))


time_for_breakfast = 1468 # in seconds
number_of_cooked_pancakes = 0

# write your while loop here

# use a while loop to make 5 pancakes for breakfast
# each pancake takes 27 seconds to cook on each side
# it takes an average of 5 seconds to flip a pancake, add or remove a pancake from the pan.
# you must decrease the time_for_breakfast each time you 
# add a pancake to the skillet (frying pan) or flip a pancake (i.e. 2 times per pancake)
# there is only room for one pancake at a time

# while time_for_breakfast > 0 and number_of_cooked_pancakes  <5:
#     print("Add a pancake to the pan")
#     time_for_breakfast -= 27
#     print("Flip the pancake")
#     time_for_breakfast -= 2.5
#     print("Cook on other side")
#     time_for_breakfast -= 27
#     print("Remove from pan")
#     time_for_breakfast -= 2.5
#     number_of_cooked_pancakes += 1
#     print('Now cooked {} pancakes!\n'.format(number_of_cooked_pancakes))
    

# print(time_for_breakfast)


line_of_hungry_patrons = list(range(0,30))
patron = 0
fed_patrons = []
hungry_patrons = []

# use a for or while loop to feed the hungry patrons who have an even number
# add the patrons with an even number to the fed_patrons list
# then remove the even numbered patrons from the line_of_hungry_patrons
# each list should contain 15 elements

# for patron in line_of_hungry_patrons:
#     if patron % 2 == 0:
#         fed_patrons.append(patron)
#         line_of_hungry_patrons.remove(patron)


index = 0

while index < len(line_of_hungry_patrons):
    patron = line_of_hungry_patrons[index]
    
    if patron % 2 == 0:
        fed_patrons.append(patron)
        line_of_hungry_patrons.remove(patron)
    else:
        index += 1

# hungry_patrons = line_of_hungry_patrons
# print("Fed Patrons:", fed_patrons)
# print("Hungry Patrons:", hungry_patrons)


# Agnes decides that she wants to start creating targeted advertisements for people. Here is a list of customer objects with information about their name, age, job, pet, and pet name. You'll use loops to find people that meet certain requirements for Agnes' targeted marketing. Write `for` loops with conditional statements in conjunction with `break` and `continue` to get the desired output.

people = [
    {'name': "Daniel", 'age': 29, 'job': "Engineer", 'pet': "Cat", 'pet_name': "Gato"}, 
    {'name': "Katie", 'age': 30, 'job': "Teacher", 'pet': "Dog", 'pet_name': "Frank"},
    {'name': "Owen", 'age': 26, 'job': "Sales person", 'pet': "Cat", 'pet_name': "Cosmo"},
    {'name': "Josh", 'age': 22, 'job': "Student", 'pet': "Cat", 'pet_name': "Chat"},
    {'name': "Estelle", 'age': 35, 'job': "French Diplomat", 'pet': "Dog", 'pet_name': "Gabby"},
    {'name': "Gustav", 'age': 24, 'job': "Brewer", 'pet': "Dog", 'pet_name': "Helen"}
]

# Use a `for` loop to find the first person in the list of people that has a dog as their pet. The iteration count shouldn't exceed 2. In your loop add a print statement that says: "{person} has a dog! Had to check {number} of records to find a dog owner."

first_dog_person = None
iteration_count = 0
for person in people:
    iteration_count += 1
    if person['pet'] == 'Dog':
        first_dog_person = person['name']
        # print(f'{person["name"]} has a dog! Had to check {iteration_count} of records to find a dog owner.')
        break
    else:
        if iteration_count > 2:
            break


# Now, use a `for` loop to create a list of all the cat owners who are under the age of 28.
cat_owners = []

for person in people:
    if person["pet"] == "Cat" and person["age"] < 28:
        cat_owners.append(person['name'])

# print(cat_owners)


# Use a `for` loop to find the first person who is above 29 years old. Use a print statement to state their name and how old they are.

thirty_something_yr_old = None
for person in people:
    if person['age'] > 29:
        thirty_something_yr_old = person['name']
        # print(f'This is {person["name"]}, and they\'re {person["age"]} years old.')
        break


# Use a `for` loop to create a list of people's names and another list of pet names for all the **dog owners**.

dog_owner_names = []
dog_names = []
for person in people:
    if person['pet'] == 'Dog':
        dog_owner_names.append(person['name'])
        dog_names.append(person['pet_name'])

# print(dog_owner_names)
# print(dog_names)

## Level Up 
# Use a `for` loop to create a list of odd numbers from the list of numbers from 0 to 100. Each time there is an odd number, add 10 to it and append it to `list_of_odd_numbers_plus_ten`. Stop adding numbers to the list when there are 35 numbers in it. Once you have reached 35 numbers, return the sum of the new list of numbers.


list_of_numbers = list(range(0, 100))
list_of_odd_numbers_plus_ten = []
counter = 0

# use a for loop to create a list of odd numbers from the list of numbers from 0 to 100
# each time there is an odd number, add 10 to it and append it to the list_of_odd_numbers_plus_ten
# stop adding numbers to the list when there are 35 numbers
# use break and continue statements in your code
# for number in list_of_numbers:
#     if number % 2 == 1 and counter < 35:
#         number += 10
#         list_of_odd_numbers_plus_ten.append(number)
#         counter += 1
#     else:
#         continue

# new_sum = sum(list_of_odd_numbers_plus_ten)
# print(list_of_odd_numbers_plus_ten, "Sum = " f'{new_sum}')      

## Alternative:
# for number in list_of_numbers:
#     if number % 2 != 0:
#         new_number = number + 10
#         list_of_odd_numbers_plus_ten.append(new_number)

#         if len(list_of_odd_numbers_plus_ten) == 35:
#             break

# sum_of_numbers = sum(list_of_odd_numbers_plus_ten)
# print(list_of_odd_numbers_plus_ten, "Sum = " f'{sum_of_numbers}')

##Alternative #2
for number in list_of_numbers:
    if number % 2 == 0:
        continue
    elif len(list_of_odd_numbers_plus_ten) == 35:
        print(sum(list_of_odd_numbers_plus_ten))
        break
    else:
        number += 10
        list_of_odd_numbers_plus_ten.append(number)


