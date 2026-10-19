word = input("введите слово: ")

word_list = list(word)
reverse_word = word_list[::-1]

if word_list == reverse_word:
    print(f"это палиндром")
else:
    print(f"не палиндром")