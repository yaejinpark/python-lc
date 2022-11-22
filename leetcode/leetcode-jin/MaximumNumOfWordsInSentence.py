"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.

 

Example 1:

Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
Explanation: 
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
Example 2:

Input: sentences = ["please wait", "continue to fight", "continue to win"]
Output: 3
Explanation: It is possible that multiple sentences contain the same number of words. 
In this example, the second and third sentences (underlined) have the same number of words.
"""

# Brute Force Attempt
 def mostWordsFound(self, sentences: List[str]) -> int:
    max_num_words = 0
    
    for s in sentences:
        space_num = 0 # Counter for number of spaces in a sentence
        for c in s:
            if c == ' ':
                space_num += 1
            if space_num >= max_num_words:
                max_num_words = space_num + 1
            
    return max_num_words

# Attempt 2 - Without a nested for loop
def mostWordsFound(self, sentences: List[str]) -> int:
    max_num_words = 0
    
    for s in sentences:
        space_num = s.count(" ") # Counter for number of spaces in a sentence
        
        if space_num >= max_num_words:
            max_num_words = space_num + 1
        
        space_num = 0
            
    return max_num_words

# Some one-liner solution
def mostWordsFound(self, sentences: List[str]) -> int:
    return max(len(s.split()) for s in sentences)

"""
Notes:

I would use either Attempt 2 or the one-liner but there are pros and cons.

Attempt 2:
Pros - Don't have memory waste from producing a new list from the sentence unlike .split()
     - Code is easy to read
Cons - What if the words were separated by more than one space? That would give the wrong space count.

One-liner:
Pros - Reduces a task into a single line, code is still easy to read
Cons - Might be slower because .split() creates an array and len() then measures then length of the new array.
     - Might also take up more memory
"""
