# HW3_Task6

# Part 1
# Suppose that you are a philatelist. You have three collections of marks. The first one contains marks 
# dedicated to cats, the second one holds cars and the third one has elephants. You can exchange by your 
# collections with another philatelists, but only entire collections (for example, change cars on bicycles), 
# but not the single marks. 
# Also you want to have short description of each collection.
# Please suggest the most appropriate way of saving information about collections, marks they consist 
# of and their descriptions.

""" 
* Answer *

The most appropriate way of saving information about collections is to save all collections in list of tuples. This allows 
us to exchange only by collections but not the single marks. Each separate marks collection is a tuple, consising 
i) collection description (string value) and ii) list of marks (tuple). Saving list of marks as a tuple give do allow us to exchange by the single marks. 

Please see the code below as an example.

"""

# collection 1 - cats
cats_des = "Collection of marks dedicated to cats. Marks in collection - 10. Collection value - $10k."
cats_marks = ("mark1", "mark2", "mark3", "...")   # type tuple/immutable to exchange only by collection not single marks.
cats = (cats_des, cats_marks)   

# collection 2 - cars
cars_des = "Collection of marks dedicated to cars. Marks in collection - 20. Collection value - $5k."
cars_marks = ("mark1", "mark2", "mark3", "...")    # type tuple/immutable to exchange only by collection not single marks.
cars = (cars_des, cars_marks)   

# collection 3 - elephants
elephants_des = "Collection of marks dedicated to cats. Marks in collection - 30. Collection value - $2.5k."
elephants_marks = ("mark1", "mark2", "mark3", "...")    # type tuple/immutable to exchange only by collection not single marks.
elephants = (elephants_des, elephants_marks)   

# save all collection in one and print the result
collections = [cats, cars, elephants] # type list/muttable in order to allow exchange by collections
print(collections)


# Part 2
# Suppose you have equal marks in collection  with cats and you want to hold information only about 
# unique ones. How would you save this information?

""" 
* Answer *

We have two options to save the information: 
1) as a set - mutable, unordered, UNIDEXED, NO DUBLICATES
2) as a dictionaty (dict) - mutable, unordered, INDEXED, NO DUBLICATES

"""