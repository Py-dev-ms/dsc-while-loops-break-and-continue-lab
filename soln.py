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

hungry_patrons = line_of_hungry_patrons
print("Fed Patrons:", fed_patrons)
print("Hungry Patrons:", hungry_patrons)


