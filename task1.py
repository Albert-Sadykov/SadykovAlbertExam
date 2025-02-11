def group_words_by_first_letter(file_path):
    words_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                first_letter = word[0].lower()
                if first_letter in words_dict:
                    if word in words_dict[first_letter]:
                        continue
                    words_dict[first_letter].append(word)
                else:
                    words_dict[first_letter] = [word]
    return words_dict

file_path = 'task2.py'
words_by_letter = group_words_by_first_letter(file_path)

for letter, words in words_by_letter.items():
    print(f"{letter}: {words}")
