import string
# Bryce Beeskow
# Assignment 5
# 12/1/2024
# CSC115
# I certify, that this computer program submitted by me is all of my own work. Signed: Bryce Beeskow

#Read the file containing the tuples, insert the entries into the dictionary and return the dictionary object.
def load_dictionary(filename):
    openfile = open(filename)
    words = dict()
    for line in openfile.readlines():
        f = line.strip().split(',')
        if len(f)==3:
            hmong_words = f[1].lower()
            english_words = f[2].lower()
            words[english_words] = hmong_words
    openfile.close()
    return words

#Take a sentence in English and return a sentence in English.
def translate(sentence):
    list_of_words = load_dictionary('Hmongwords.txt')
    translate = ''
    for words in sentence.split():
        if words in list_of_words:
            translate += list_of_words[words] + ' '
        else:
            translate +='? '
    return translate.strip()        
#Print the frequency of English words that were translated.
def print_word_frequency(dictionary):
    frequent_words = dict()
    for words in dictionary.split():
        if words in frequent_words:
            frequent_words[words] += 1
        else:
            frequent_words[words] = 1
    for words in frequent_words:
        print('{:10s} {:10d}'.format(words,frequent_words[words]))  
    return
    
#The main logic loop.    
def main():
    go = True
    newtext = ''
    while go:
        sentence = input("Type your English sentence: ")
        sentence = sentence.lower()
        for i in string.punctuation:
            sentence = sentence.replace(i,' ')
        hmongtext = translate(sentence)
        print('Hmong: ',hmongtext)
        newtext += sentence + ' '
        go = input("Another translation (Y/N): ").lower()=='y'
    print('{:15s} {:10s}'.format('Word', 'Frequency'))
    print_word_frequency(newtext)
main() 


