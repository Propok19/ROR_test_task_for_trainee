import re
from collections import defaultdict

word_count = defaultdict(int) # setting a counter for our words
freq_words = [] # future list of repeated words

def word_search(text):
    if not re.search('[a-zA-Z]', text): # checking on not English letters
        print("I don't know this language!")
    else:
        clean_text = re.sub("[\W]+'[\W]+", ' ', text) # deleting commas, dots etc. (excluding apostrophies)
        split_text = clean_text.split()
        for word in split_text:
            word_count[word] += 1
        if len(list(word_count.keys())[list(word_count.values()).index(1)]) <= 3: # if number of unique words is less than 3, than output is an empty array
            freq_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True) # sorting list in descending order
            print(list((w.lower(), v) for w,v in freq_words[0:3]))# changing case of words on lowercase
        else: 
            freq_words = []
            print (freq_words)
    

word_search("Jin, JK, Jin, Me, JK, JK, A, JK, A, A, A, A, don't don't don't don't")