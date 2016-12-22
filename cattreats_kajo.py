'''cattreats.py
This simple script finds the location of a selected cat's name in one list and
its favorite treat at the corresponding location in another. Both items are
printed to the screen afterward.
Limitations:
This code will not work if the cat's name is not in list of cat names.
Usage: ./cattreats.py
Mira Kajo - 21.12.2016
'''

# Create and fill lists of cats and treats
# as I understood the exercise - every cat has their own favorate treat that is 'assigned' to that particular cat,
# therefore, the treats list is missing one value, 'Snowball II'. I set his treat to be 'Dust'. 
Cats = ['Garfield', 'Nermal', 'Tom Cat', 'Puss in Boots', 'Hobbes', 'Stimpy', 'Snowball II']
Treats = ['Lasagne', 'Praise', 'Mice', 'Power', 'Calvin', 'Fresh kitty litter']
Treats.append('Dust')
print(Treats)
print(len(Cats))

# Set the selected cat
# to find the location of selected cat's name from Cats list.
# Originally this variable was assigned number 7. But we have to tell Python from what list we want to draw info,
# and the location of the wanted value.  
SelectedCat = Cats[0]

# Find location of selected cat
CatIndex = Cats.index(SelectedCat)

# Print cat name and favorit treat on screen
# originally, Treats was assigned the SelectedCat variable that contains the name of the cat in Cats -list.
# This variable assigned a string to Treats and not a number. By changing the variable to CatIndex (variable that was given the number of Cats-list index),
# we are able to tell Python the location of the cat in Treats -list. 
print("The favorite treat of", SelectedCat, "is", Treats[CatIndex])