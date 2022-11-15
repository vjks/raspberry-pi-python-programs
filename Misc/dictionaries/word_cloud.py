import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
#import fileupload
import io
import sys

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    word_dictionary = {}
    word_list = file_contents.split()
    for word in word_list:
        word_no_punc = ""
        for character in word:
            if character not in punctuations: 
                word_no_punc += character # remove all punctuation from a word
        word_no_punc = word_no_punc.lower() # convert the word with no punctuation in it to lowercase
        #for ui_word in uninteresting_words:
            #print(ui_word + str(len(uninteresting_words)))
        if word_no_punc not in uninteresting_words:
                #print(word_no_punc + " is not equal to " + ui_word)
            if word_no_punc not in word_dictionary:
                word_dictionary.update({word_no_punc: 1})
            else:
                word_dictionary[word_no_punc] += 1

                
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_dictionary)
    return cloud.to_array()

    # Display your wordcloud image

text_file = open("d:/OneDrive/Documents/GitHub/python-programs/Misc/dictionaries/Persuasion_Jane_Austen.txt", encoding="utf8")
#read whole file to a string
data = text_file.read()
#close file
text_file.close()

myimage = calculate_frequencies(data)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()