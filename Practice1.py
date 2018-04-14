# Попросить пользователя ввести слово только из букв.

def enter_word():
    while True:
        s = input("Please enter an alphabetic word.\n")
        s = s.strip()
        if s.isalpha():
            return s


word = enter_word()
assert word.isalpha(), "Word is not alphabetic."
print(word)

