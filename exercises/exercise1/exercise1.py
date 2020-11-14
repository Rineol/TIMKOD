import numpy as np
import operator


def generate_single_word(letters_source, probabilities):
    word = ''
    while True:
        char = np.random.choice(letters_source, p=probabilities)
        if char == ' ':
            break
        else:
            word += char
    return word


def generator_zero(size):
    alphabet = list('qwertyuiopasdfghjklzxcvbnm ')
    length = 0
    probabilities = [1/len(alphabet)]*len(alphabet)
    #print(probabilities)
    for i in range(size):
        word = generate_single_word(alphabet, probabilities)
        length += len(word)
    return length/size


def read_file(name):
    file = open(name, 'r')
    return file.read()


def calc_frequency(filepath):
    counter = 0
    alphabet = list('qwertyuiopasdfghjklzxcvbnm ')
    alphabet_dict = dict(zip(alphabet, [0] * len(alphabet)))
    file = read_file(filepath)
    text = list(file)
    for word in text:
        letters = list(word)
        for letter in letters:
            alphabet_dict[letter] += 1
            counter += 1
    freq_dict = {k: v / counter for k, v in alphabet_dict.items()}
    return freq_dict


def generator_first(size, probabilities):
    alphabet = list('qwertyuiopasdfghjklzxcvbnm ')
    length = 0
    print("PROB", probabilities)
    for i in range(size):
        word = generate_single_word(alphabet, list(probabilities.values()))
        length += len(word)
    return length/size


def cond_probabilities(dictionary):
    sorted_dict = sorted(dictionary.items(), key=operator.itemgetter(1))
    first_letter = sorted_dict.pop()[0]
    second_letter = sorted_dict.pop()[0]
    print(first_letter)
    print(second_letter)
    return


if __name__ == "__main__":
    #EXERCISE1: generate words and calculate average length
    print(generator_zero(10))
    #EXERCISE2: read file and calculate frequency of words (read included in calc)
    probabilities = calc_frequency('norm_hamlet.txt')
    #EXERCISE3: use calculated frequency for next task
    print(generator_first(10, probabilities))
    #EXERCISE4: conditional probability
    cond_probabilities(probabilities)

