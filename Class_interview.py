# Design a class
# Inserting a value (no duplicates)
# Removing a value
# GetRandom a value that is already inserted (with eaual probality)
    # random.choice(list)
# values are integers
# Inserting amount : milions
# They will be an equal proportion of inserting and remobing

import random 
import collections

class store:
    def __init__(self):
        self.map = collections.defaultdict(set)
        self.values = []
        
    def insert_element(self, value):
        if value in self.values:
            print('the number is already in the array')
        else:
            self.values.append(value)
            self.map[value].add(len(self.values)-1)
        
        
    def remove_element(self, value):
        if value not in self.map:
            return 
        
        index = self.map[value].iterator().next() # get the index of the value
        last_value = self.values[-1]
        self.values[-1] = value
        self.values[index] = last_value 
        self.map[last_value].add(index)
        self.values.pop()
        
        self.map[value].remove(index)
        
        
    def get_Random(self):
        return random.choice(self.values)
    
    def show(self):
        print(self.values)

game = store()


while True:
    choic = input("Do you want to add, remove, show or get random value : ('add','remove', 'show', 'random' ) ")
    if choic == 'add':
        number = int(input('Type a number : '))
        game.insert_element(number)
    elif choic == 'remove':
        number = int(input('Type a number : '))
        game.remove_element(number)
    elif choic == 'random':
        print(game.get_Random())
    elif choic == 'show':
        game.show()
    elif choic == 'end':
        break
    
     