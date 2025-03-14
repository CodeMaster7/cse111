"""
Author: Sam Bonfanti

Purpose: This program generates simple English sentences that consist of a determiner, a noun, and a verb. The sentences can be in past, present, or future tense and can be singular or plural based on the input provided.

Problem: The Turing test, named after Alan Turing, is a test of a computer's ability to make conversation that is indistinguishable from human conversation. A computer that could pass the Turing test would need to understand sentences typed by a human and respond with sentences that make sense.

Core Requirements: generate sentences with three parts
1. a determiner (sometimes known as an article)
2. a noun
3. a verb

your program must include at least these five functions:
main
make_sentence
get_determiner
get_noun
get_verb
"""

import random
# This is the main function that will call the other functions and print the sentence
def main():
    # Call make_sentence 6 times and print each sentence
    # Generate one sentence with a single past tense
    print(make_sentence(1, "past"))

    # Generate one sentence with a plural past tense
    print(make_sentence(2, "past"))

    # Generate one sentence with a single present tense
    print(make_sentence(1, "present"))

    # Generate one sentence with a plural present tense
    print(make_sentence(2, "present"))

    # Generate one sentence with a single future tense
    print(make_sentence(1, "future"))

    # Generate one sentence with a plural future tense
    print(make_sentence(2, "future"))

# This function will call the other functions to create a sentence
def make_sentence(quantity, tense):
    """Build and return a sentence with the following structure:
    determiner noun verb.

    Parameters:
        quantity: an integer that determines if the determiner
            and noun are singular or plural
        tense: a string that determines the verb tense
            ("past", "present", or "future")
    Return: a sentence with a determiner, noun, and verb
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)

    # Create the sentence and capitalize the first letter
    sentence = f"{determiner} {noun} {verb}."
    sentence = sentence.capitalize()

    return sentence

# This function will get a random determiner
def get_determiner(quantity):
	"""Return a randomly chosen determiner. A determiner is
	a word like "the", "a", "one", "some", "many".
	If quantity is 1, this function will return either "a",
	"one", or "the". Otherwise this function will return
	either "some", "many", or "the".
	Parameter
		quantity: an integer.
			If quantity is 1, this function will return a
			determiner for a single noun. Otherwise this
			function will return a determiner for a plural
			noun.
	Return: a randomly chosen determiner.
	"""
	if quantity == 1:
		words = ["a", "one", "the"]
	else:
		words = ["some", "many", "the"]
	# Randomly choose and return a determiner.
	word = random.choice(words)
	return word

# This function will get a random noun
def get_noun(quantity):
	"""Return a randomly chosen noun.
	If quantity is 1, this function will
	return one of these ten single nouns:
		"bird", "boy", "car", "cat", "child",
		"dog", "girl", "man", "rabbit", "woman"
	Otherwise, this function will return one of
	these ten plural nouns:
		"birds", "boys", "cars", "cats", "children",
		"dogs", "girls", "men", "rabbits", "women"
	Parameter
		quantity: an integer that determines if
			the returned noun is single or plural.
	Return: a randomly chosen noun.
	"""
	if quantity == 1:
		nouns = ["bird", "boy", "car", "cat", "child",
		"dog", "girl", "man", "rabbit", "woman"]
	else:
		nouns = ["birds", "boys", "cars", "cats", "children",
		"dogs", "girls", "men", "rabbits", "women"]
	word = random.choice(nouns)
	return word

# This function will get a random verb
def get_verb(quantity, tense):
	"""Return a randomly chosen verb. If tense is "past",
	this function will return one of these ten verbs:
		"drank", "ate", "grew", "laughed", "thought",
		"ran", "slept", "talked", "walked", "wrote"
	If tense is "present" and quantity is 1, this
	function will return one of these ten verbs:
		"drinks", "eats", "grows", "laughs", "thinks",
		"runs", "sleeps", "talks", "walks", "writes"
	If tense is "present" and quantity is NOT 1,
	this function will return one of these ten verbs:
		"drink", "eat", "grow", "laugh", "think",
		"run", "sleep", "talk", "walk", "write"
	If tense is "future", this function will return one of
	these ten verbs:
		"will drink", "will eat", "will grow", "will laugh",
		"will think", "will run", "will sleep", "will talk",
		"will walk", "will write"
	Parameters
		quantity: an integer that determines if the
			returned verb is single or plural.
		tense: a string that determines the verb conjugation,
			either "past", "present" or "future".
	Return: a randomly chosen verb.
	"""
	if tense == "past":
		verbs = ["drank", "ate", "grew", "laughed", "thought",
		"ran", "slept", "talked", "walked", "wrote"]
	elif tense == "present" and quantity == 1:
		verbs = ["drinks", "eats", "grows", "laughs", "thinks",
		"runs", "sleeps", "talks", "walks", "writes"]
	elif tense == "present" and quantity != 1:
		verbs = ["drink", "eat", "grow", "laugh", "think",
		"run", "sleep", "talk", "walk", "write"]
	elif tense == "future":
		verbs = ["will drink", "will eat", "will grow", "will laugh",
		"will think", "will run", "will sleep", "will talk",
		"will walk", "will write"]
	word = random.choice(verbs)
	return word
main()