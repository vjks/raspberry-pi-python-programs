text_file = open("./election_strategy_signups.txt", encoding="utf8")
#read whole file to a string
data = text_file.read()
#close file
text_file.close()

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~+=’'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                       "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                       "they", "them", \
                       "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                       "been", "being", \
                       "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                       "where", "how", \
                       "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can",
                       "will", "1", "2", "0", "4", "5", "6", "7", "8", "9"]
word_dictionary = {}
word_list = data.split()
for word in word_list:
    word_no_punc = ""
    for character in word:
        if character not in punctuations:
            word_no_punc += character  # remove all punctuation from a word
    word_no_punc = word_no_punc.lower()
    if word_no_punc not in uninteresting_words and len(word_no_punc) > 3:
        if word_no_punc not in word_dictionary:
            word_dictionary[word_no_punc] = 1
        else:
            word_dictionary[word_no_punc] += 1

wd = (sorted(word_dictionary.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
for key, value in wd:
    if value > 500:
        print(key, value, end=", ")
