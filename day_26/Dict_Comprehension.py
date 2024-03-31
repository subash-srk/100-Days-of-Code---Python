sentence = input()

list = sentence.split(' ')
dict = {word:len(word) for word in list}
print(dict)
