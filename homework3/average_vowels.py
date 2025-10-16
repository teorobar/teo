# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

def counting_vowels_and_consonants(str):
	vow=0
	con=0
	for char in str:
		if char.isalpha():
			if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
				vow+=1
			else:
				con+=1
	return(vow, con)

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(str):
	sentences=0
	for char in str:
		if char=="." or char=="!" or char=="?":
			sentences+=1
	return(sentences, counting_vowels_and_consonants(str)[0]/sentences, counting_vowels_and_consonants(str)[1]/sentences)

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

print(
	f"The average number of vowels per sentence in this paragraph is {average_vowels_and_consonants(paragraph)[1]} "
    f"and the average number of consonants is {average_vowels_and_consonants(paragraph)[2]}"
)