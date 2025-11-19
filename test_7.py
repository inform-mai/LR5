# Проверка, есть ли в строке гласные буквы
def vowel_letters(string):
    letters = 'AEIOUaeiou'
    f = False
    for i in string:
        if i in letters:
            f = True
        else:
            continue
    return f

def test_vowel_letters_success():
    my_string = 'Hello!'
    assert vowel_letters(my_string)


def test_vowel_letters_failure():
    my_string = 'Br Br Ptpm'
    assert vowel_letters(my_string)
