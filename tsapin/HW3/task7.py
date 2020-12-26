# HW3_Task 7
# Please suggest your option of situation where different data types are used for saving the information (describe situation like in previous task).

""" 
* Answer *

In previous task I suggested to save the information as list of tuples (in case where we allow dublicates). Please see below:

cats = ('Description',('mar1', 'mark2' ..))         # tuple, inside - string and tuple
cars = ('Description',('mar1', 'mark2' ..))         # tuple, inside - string and tuple
elephants = ('Description',('mar1', 'mark2' ..))    # tuple, inside - string and tuple
collections = [cats, cars, elephants]               # list of tuples

Of course, we can use another data types to save the information:
- List of marks (('mar1', 'mark2' ..)) in each collection should be only TUPLE
for not allowing the exchange by single marks. 
- Separate collections (cats, cars, elephant) could be any of the following - TUPLE (our case), LIST, SET or DICT.

cats = ('Description',('mar1', 'mark2' ..))     # tuple
cats = ['Description',('mar1', 'mark2' ..)]     # list
cats = {'Description',('mar1', 'mark2' ..)}     # set
cats = {'Des': 'Description', 'marks': ('mar1', 'mark2' ..)}    # dict

- Aggregated "collections" could be alternativelly represented as a SET or DICTIONARY. Please see below.

collections = {cats, cars, elephants}   # set of tuples
collections = {"collection 1": cats, "collection 2": cars, "collection 3": elephants}   # dictionary with tuples as values

"""