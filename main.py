import re
import os
from pprint import pprint

def tabulate_file():
    # Open the file
    with open(file_name, 'r') as f:
        # Read the file
        data = f.read()
        # Split the file by line
        data = data.splitlines()
        # Create the dictionary
        dict = {}
        # Loop through the lines
        for i, line in enumerate(data):
            # Split the line by spaces
            line = line.split(' ')
            # Loop through the words
            for j, word in enumerate(line):
                # Remove any special characters
                word = re.sub('[^A-Za-z0-9]+', '', word)
                word = word.lower()
                # If the word is not in the dictionary, add it
                if word not in dict:
                    dict[word] = {}
                # If the index is not in the dictionary, add it
                if i not in dict[word]:
                    dict[word][i] = j

        print('*******Dictionary*******')
        # pprint(dict)
        for key, value in dict.items():
            line_num = ""
            word_num = ""
            for i in value.keys():
                line_num += f"{i}, "
            for i in value.values():
                word_num += f"{i}, "

            line_num = line_num[:-2]
            word_num = word_num[:-2]
                
            print(f'Word: "{key}" | Line Number: {line_num} | Word Number: {word_num} | Occurences: {len(value)}')

        return dict

def reconstruct(dct):
    line_passed = False

    # Create a list to hold the sentences
    sentences = []
    # Loop through the dictionary
    for key, value in dct.items():
        # Loop through the values
        for k, v in value.items():
            # If the sentence is not in the list, add it
            if k >= len(sentences):
                # Add empty lists to the sentences list until the line index is in range
                for i in range(len(sentences), k+1):
                    sentences.append([])
            # Add the word to the sentence
            sentences[k].append(key)
    
    

    while line_passed == False:
        tgt_line = int(input("Enter the line number to reconstruct: "))
        if tgt_line > len(sentences):
            print(f"The line number {tgt_line} is out of range. Please try again.")
        else:
            line_passed = True

    # Loop through the sentences
    for i, sentence in enumerate(sentences):
        if i == tgt_line - 1:
        # Create a list to hold the words
            words = []
            # Loop through the words
            for j, word in enumerate(sentence):
                # Add the word to the list
                words.append(word)
            # Sort the words by the index
            words.sort(key=lambda x: dct[x][i])
            # Join the words into a sentence and capitalize the first word
            sentences[i] = ' '.join(words).capitalize()
            break

    print()
    print('******Reconstructed*****')
    # for sentence in sentences:
    print(sentences[i])
    
    return sentences

if __name__ == '__main__':
    file_passed = False
    file_name = ""

    while file_passed == False:
        file_name = input("Enter the file name (with the .txt extension): ")
        if not os.path.exists(file_name):
            print(f"The {file_name} file does not exist. Please try again.")
        else:
            file_passed = True

    dct = tabulate_file()
    reconstruct(dct)