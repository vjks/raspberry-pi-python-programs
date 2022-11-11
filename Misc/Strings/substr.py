def highlight_word(sentence, word):

	return(sentence[0:sentence.index(word)] + word.upper() + sentence[sentence.index(word)+len(word):len(sentence)])

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
