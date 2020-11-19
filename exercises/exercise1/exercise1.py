import numpy as np
import operator
import random


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
    #print("PROB", probabilities)
    for i in range(size):
        word = generate_single_word(alphabet, list(probabilities.values()))
        length += len(word)
    return length/size


def update_dictionaries(dictionary, top_key, key):
    selected = dictionary.get(top_key, {})
    value = selected.get(key, 0)
    total = selected.get("total", 0)
    selected.update({key: value + 1})
    selected.update({"total": total + 1})
    dictionary.update({top_key: selected})
    return dictionary


def cond_probabilities(dictionary, file):
    general_dict = {}
    counter = 0
    old_letter = 0
    sorted_dict = sorted(dictionary.items(), key=operator.itemgetter(1))
    first_char = sorted_dict.pop()[0]
    second_char = sorted_dict.pop()[0]
    text = read_file(file)
    for _, letter in enumerate(text):
        if old_letter != "":
            general_dict = update_dictionaries(general_dict, old_letter, letter)
            counter += 1
        old_letter = letter
    #print(general_dict)
    print("Exercise 4: ")
    for ins_dict in general_dict:
        for (key, value) in general_dict.get(ins_dict).items():
            if key != "total":
                if ins_dict == first_char or ins_dict == second_char:
                    print("\t\t", str(ins_dict) + str(key), value / counter)
    return general_dict, counter


def random_from_letters(letters, probability):
    value = random.random()
    prob_sum = 0.0
    index = 0
    for ind, val in enumerate(probability):
        prob_sum += val
        if prob_sum >= value:
            index = ind
            break
    return letters[index]


def markov_generate_source(filename, row):
    content = read_file(filename)
    dictionary = {}
    letters = []
    for _, letter in enumerate(content):
        if len(letters) > row:
            del(letters[0])
            dictionary = update_dictionaries(dictionary, ''.join(letters), letter)
        letters.append(letter)
    #print(dictionary)
    return dictionary


def markov_generator(size, probabilities_dict, starter_word, number):
    letters = list(starter_word)
    alphabet = ['qwertyuiopasdfghjklzxcvbnm ']
    result = ''
    selection = {}
    for i in range(len(letters) - number):
        del(letters[0])
    for i in range(size):
        letters_random = list()
        probability_random = list()
        selection = probabilities_dict.get(''.join(letters), {})
        total_count = selection.get("total", 1)
        for (k, v) in selection.items():
            if k != "total":
                letters_random.append(k)
                probability_random.append(v/total_count)
        if probability_random:
            char = random_from_letters(letters_random, probability_random)
        else:
            char = np.random.choice(alphabet)
        result += char
        letters.append(char)
        if len(letters) > number:
            del (letters[0])
    print(result)
    return result


if __name__ == "__main__":
    #EXERCISE1: generate words and calculate average length
    print(F"Exercise 1 avg: {generator_zero(10)}")
    #EXERCISE2: read file and calculate frequency of words (read included in calc)
    probabilities = calc_frequency('norm_hamlet.txt')
    print(f"Exercise 2 probabilities: {probabilities}")
    #EXERCISE3: use calculated frequency for next task
    print(f"Exercise 3 avg: {generator_first(10, probabilities)}")
    #EXERCISE4: conditional probability
    general_dict, counter = cond_probabilities(probabilities, 'bees.txt')
    #EXERCISE5:
    print("Exercise 5: ")
    files = ['norm_hamlet.txt',  'norm_wiki_sample.txt', 'norm_romeo.txt']
    for file in files:
        for i in range(1, 6, 2):
            last_char = ""
            words = 0
            total_length = 0
            general_dict = markov_generate_source(file, i)
            result = markov_generator(1000, general_dict, 'probability', i)
            for char in result:
                if char != " ":
                    total_length += 1
                if char == " " and last_char != " ":
                    words += 1
                last_char = char
            print(f"Row = {i} ; Average length:  {total_length / words}")