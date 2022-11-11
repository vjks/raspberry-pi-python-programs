def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    first_char = word[0]
    piglatin_word = word[1:len(word)] + first_char + "ay" 
    # Turn the list back into a phrase
    say += piglatin_word + " "
  return say.strip()
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"