# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order.
# Sample Input: My name is Michele
# Sample Output: Michele is name My
def reverse_word_order(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)

sentence = input()
print(reverse_word_order(sentence))
