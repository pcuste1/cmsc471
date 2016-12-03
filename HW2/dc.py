""" CMSC471 02 hw2 spring 2016
    Patrick Custer, pcuste1, LY60654

    No comments needed??? I don't think we have to comment our code????
"""    
#import time
import aima.search as a       # AIMA module for search problems

dict_file = "words34.txt"

dictionary = {}

# Thank you for using global variables. Coding standards would be proud.
for line in open(dict_file):
    word, n = line.strip().split('\t')
    dictionary[word] = float(n)

class DC(a.Problem):

    # This was basically all given to us. 
    def __init__(self, initial='dog', goal='cat', cost='steps'):
        self.initial = initial
        self.goal = goal
        self.cost = cost

    # Check every possible combination of letters in the word. EZPZ 201
    def actions(self, state):
        """ returns new word to be used"""
        alph = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(state)):
            hold = list(state)
            for let in alph:
                hold[i] = let
                word = "".join(hold)
                if word in dictionary:
                    yield [i,let]

    # Preeeety basic conversion. Return action as a fake tuple because lazy
    def result(self, state, action):
        state = list(state)
        state[action[0]] = action[1]
        return "".join(state)
    
    # More string comparision. What is this 201?
    def goal_test(self, state):
        g = self.goal
        #print(g, " != ", state)
        for i in range(len(g)):
            if g[i] != state[i]:
                return False
        return True

    def path_cost(self, c, state1, action, state2):
        if self.cost == "steps":
            return  c + 1
        # This is gross I'm sorry. Gross but it works.
        elif self.cost == "scrabble":
            let = action[1]
            if let in "aeioulnstr":
                return c + 1
            elif let in "dg":
                return c + 2
            elif let in "bcmp":
                return c + 3
            elif let in "fhvwy":
                return c + 4
            elif let in "k":
                return c + 5
            elif let in "jx":
                return c + 6
            else:
                return c + 10
        # God Bless Dictionaries. Thank you based god
        else:
            return c + dictionary[state2]
        return c

    def __repr__(self):
        """ returns a string to represent a dc problem """
        # Not 100% if this is working. Never seems to output this exactly
        return "DC({},{})".format(self.initial,self.goal)

    def h(self, node):
        """Heuristic: returns number of letters different """
        # EZ PZ string comparision
        c = 0
        g = self.goal
        n = node.state
        for i in range(len(g)-1):
            if g[i] !=  n[i]:
                c += 1
        return c
    
# add more functions here as needed

    



