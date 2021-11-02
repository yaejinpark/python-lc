import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.queue = []
        self.stack = []
    
    def pushCharacter(self, char):
        self.stack.append(char)
    
    def popCharacter(self):
        return self.stack.pop()
    
    def enqueueCharacter(self, char):
        #if I use append, the character will go to the end instead of the beginning
        self.queue.insert(0, char)
    
    def dequeueCharacter(self):
        return self.queue.pop()
