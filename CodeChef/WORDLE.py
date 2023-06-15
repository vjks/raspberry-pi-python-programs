tests = int(input())

for _ in range(tests):
    hidden_word = input()
    guess_word = input()
    m_string = ""
    for i in range(len(hidden_word)):
        if hidden_word[i] == guess_word[i]:
            m_string += "G"
        else:
            m_string += "B"
    print(m_string)
    