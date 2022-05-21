import random
import string

order = list(string.ascii_lowercase)
random.shuffle(order)
print(order)

words = ["banana","mango","strawberry","apple","dragonfruit","fashionfruit","mandarin","grape"]
#print([order.index(c) for word in words for c in word])
words.sort(key=lambda x : print([order.index(c) for c in x]))
print(words)