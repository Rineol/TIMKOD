import random
import numpy as np

def generate_single_word(letters_source):
    word = ''
    while True:
        char = np.random.choice(letters_source)
        if char == ' ':
            break
        else:
            word += char
    return word


def generator_zero(size):
    alphabet = list('qwertyuiopasdfghjklzxcvbnm ')
    length = 0
    for i in range(size):
        word = generate_single_word(alphabet)
        length += len(word)
    return length/size

if __name__ == "__main__":
    print(generator_zero(10))