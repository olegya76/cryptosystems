"""
Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом
тексте заменяется символом, находящимся на некотором постоянном числе позиций
левее или правее него в алфавите. Например, в шифре со сдвигом вправо на 3,
А была бы заменена на Г, Б станет Д, и так далее.
"""
from string import ascii_lowercase

def caesar_cipher_code(open_text, shift, alphabet):
    """
    Ф-ция принимающая 3 переменные: open_text - текст который хотим зашифровать
    и shift - размер сдвига при положительном числе сдвиг вправо, при
    отрицательном влево, и используемый алфавит
    """
    #alphabet = string.ascii_lowercase
    new_alphabet = ascii_lowercase[shift:] + ascii_lowercase[:shift]

    ciphertext = ""
    for letter in open_text:
        number_of_letter = alphabet.find(letter)
        #print(number_of_letter)
        if(number_of_letter != -1):
            ciphertext += new_alphabet[number_of_letter]
        else:
            ciphertext += letter
    return ciphertext

def caesar_cipher_code_v2(open_text, shift, alphabet):
    """
    Ф-ция принимающая 3 переменные: open_text - текст который хотим зашифровать
    и shift - размер сдвига при положительном числе сдвиг вправо, при
    отрицательном влево, и используемый алфавит
    """
    upper_alphabet = alphabet.upper()
    ciphertext = ""
    for letter in open_text:
        if(letter.islower()):
            number_of_letter = alphabet.find(letter)
        


#В шифре цезаря делался сдвиг на 3 вправо, но можно сделать его более гибким
#и спросить на сколько будет сдвиг

#shift - переменная хранящая сдвиг, при положительном числе сдвиг вправо,
#при отрицателном влево
shift = int(input("Введите размер сдвига: "))
#вывод начального алфавита и со сдвигом
alphabet = ascii_lowercase
print("Оригинальный алфавит:\n", ascii_lowercase)
print("Алфавит со здвигом:\n", ascii_lowercase[shift:] + ascii_lowercase[:shift])

#open_text - тест который хотим передать до зашифровки
open_text = input("Введите текст, который хотите зашифровать\n")
#шифруем текст с использованием ф-ции caesar_cipher_code
сiphertext = caesar_cipher_code(open_text, shift, alphabet)
print(сiphertext)
