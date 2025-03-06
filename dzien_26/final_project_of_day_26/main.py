import pandas

nato_phonetic_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
letter_list = nato_phonetic_alphabet["letter"].to_list()
codes_list = nato_phonetic_alphabet["code"].to_list()
nato_phonetic_alphabet_dict = {letter : code for letter,code in zip(letter_list, codes_list)}

user_word = input("Enter a word: ")
answer = [f'{letter.title()} for {nato_phonetic_alphabet_dict[letter.upper()].title()}' for letter in user_word]
print(answer)