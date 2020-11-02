from spellchecker import SpellChecker
from PyDictionary import PyDictionary
import time


def define(word):

	word = word.split(" ")[1]

	spell = SpellChecker()
	correct_spelling = spell.correction(word)

	response = ""

	if correct_spelling != word:
		response = "Did you mean " + correct_spelling + "? : "

	dictionary = PyDictionary()

	try:
		response += dictionary.meaning(correct_spelling)['Noun'][0].capitalize()

		time.sleep(1)
		return response
	except:
		pass