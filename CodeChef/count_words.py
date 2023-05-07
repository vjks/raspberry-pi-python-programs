num_cases = int(input())

for x in range(num_cases):
    words = input().split()
    num_words_per_page = int(words[1])
    num_pages = int(words[0])
    print( num_pages * num_words_per_page )