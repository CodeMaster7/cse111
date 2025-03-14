"""
Author: Sam Bonfanti

Purpose: This program generates simple English sentences that consist of a determiner, a noun, and a verb. The sentences can be in past, present, or future tense and can be singular or plural based on the input provided. also add a function that will generate a sentence with a prepositional phrase.

Problem: The Turing test, named after Alan Turing, is a test of a computer's ability to make conversation that is indistinguishable from human conversation. A computer that could pass the Turing test would need to understand sentences typed by a human and respond with sentences that make sense. also add a function that will generate a sentence with a prepositional phrase.

Core Requirements: generate sentences with three parts
1. a determiner (sometimes known as an article)
2. a noun
3. a verb

final requirements: add a function that will generate a sentence with a prepositional phrase.

your program must include at least these five functions:
main
make_sentence
get_determiner
get_noun
get_verb
get_preposition
get_prepositional_phrase
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
    determiner noun verb prepositional_phrase.

    Parameters:
        quantity: an integer that determines if the determiner
            and noun are singular or plural
        tense: a string that determines the verb tense
            ("past", "present", or "future")
    Return: a sentence with a determiner, noun, verb, and prepositional phrase
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    # Get a prepositional phrase to add to the sentence
    prepositional_phrase = get_prepositional_phrase()

    # Create the sentence and capitalize the first letter
    sentence = f"{determiner} {noun} {verb} {prepositional_phrase}."
    sentence = sentence.capitalize()

    return sentence

# This function will get a random determiner
def get_determiner(quantity):
	"""Return a randomly chosen determiner based on quantity.
	For example: "a", "one", "the" for singular;
	"some", "many", "the" for plural.
	Parameter
		quantity: an integer (1 for singular, other for plural)
	Return: a determiner appropriate for the quantity.
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
	"""Return a randomly chosen noun based on quantity.
	Examples: "bird" (singular) or "birds" (plural).
	Parameter
		quantity: an integer (1 for singular, other for plural)
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
	"""Return a randomly chosen verb based on tense and quantity.
	Examples:
	- Past: "drank", "ate", "grew"
	- Present (singular): "drinks", "eats", "grows"
	- Present (plural): "drink", "eat", "grow"
	- Future: "will drink", "will eat", "will grow"

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

# This function will get a random preposition
def get_preposition():
	"""Return a randomly chosen preposition from a list of prepositions.

	Return: a randomly chosen preposition.
	"""
	prepositions = ["about", "above", "across", "after", "along",
		"around", "at", "before", "behind", "below",
		"beyond", "by", "despite", "except", "for",
		"from", "in", "into", "near", "of",
		"off", "on", "onto", "out", "over",
		"past", "to", "under", "with", "without"]

	# Randomly choose and return a preposition
	preposition = random.choice(prepositions)
	return preposition

# This function will create a prepositional phrase
def get_prepositional_phrase():
	"""Build and return a prepositional phrase with the structure:
	preposition determiner noun

	For example: "on the table", "near a dog", "with many children"

	Return: a prepositional phrase
	"""
	# Randomly choose a preposition
	preposition = get_preposition()

	# Randomly choose a quantity (1 or 2) for the determiner and noun
	quantity = random.randint(1, 2)

	# Get a determiner and noun that match the quantity
	determiner = get_determiner(quantity)
	noun = get_noun(quantity)

	# Build the prepositional phrase
	prepositional_phrase = f"{preposition} {determiner} {noun}"

	return prepositional_phrase

main()