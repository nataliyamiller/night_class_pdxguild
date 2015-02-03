# adding the letter + 'ya'
print "Welcome to the weird world!"
pig = "ya"

# word = 'hi'
# word = raw_input("Type any word: ")

"""
def weird_world(word):
	while not word or word.isdigit():
		word = raw_input("Your string must be not empty and not be a digit!")


	print word[1:].lower() + word[0].lower() + pig

weird_world(word)
"""

def weird_world():
	word = raw_input("please type a word (please no numbers): ")
	word = word.lower()
	for letter in word:
		if letter.isalpha():
			continue
		else:
			weird_world()
			
	print word[1:] + word[0] + pig
	print "Welcome to the Weird World"

weird_world()