import numpy as np
import pylab as pl


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", ",", ";", "-", "_", "+"]

# This functon takes a list and a string of characters, it calculates how often a certain character appears
# Then it returns a list with character and frequency
def frequencies(string,letters):
    list_frequencies = []
    for letter in letters:
        freq = 0
        for i in string:
            if i == letter:
                freq += 1
        if freq != 0:
            list_frequencies.append(letter)
            list_frequencies.append(freq)
    return list_frequencies


# This function returns a list containing 2 lists with letter and frequencies
def fix_lists_letter(list_1):
    list_letters = []
    list_freq = []
    list_letters.append(list_1[0])
    for i in range(1,len(list_1)):
        if i % 2 == 0:
            list_letters.append(list_1[i])
        else:
            list_freq.append(list_1[i])
    if len(list_letters) != len(list_freq):
        return "Some error occurred"
    else:
        final_list = [list_letters,list_freq]
        return final_list


#The following function sorts the letters and frequencies in descending order.
def sort_all(c):
    letters = c[0]
    freq = c[1]
    final_letter = []
    final_freq = []
    for i in range(0,len(letters)):
        maximum = max(freq)
        ind = freq.index(maximum)
        final_freq.append(freq[ind])
        final_letter.append(letters[ind])
        letters.remove(letters[ind])
        freq.remove(freq[ind])
    sorted_output = [final_letter,final_freq]
    return sorted_output


# Relative frequencies
def get_rel_freq(list_1):
    list_to_return = []
    total = float(sum(j for j in list_1))
    for i in list_1:
        #print i, total, (i/total)
        list_to_return.append(i/total)
    return list_to_return


# ===== here is where the action happens =====

#read the text and create a string
with open('theprince.txt','r') as mytext:
    string1 = mytext.read()
    #string1 = string1.lower()

# calculate frequencies
first_count = frequencies(string1,alphabet)
# create the list of two lists
final = fix_lists_letter(first_count)
# define the list of letters
letter_s = final[0]
# define the list of frequencies
freq = final [1]
# add up all the frequencies - this should be the total letter count
result = sum(freq)

# print the results
print(first_count)
print("Number of character used: ", result)

# sort the results
sorted_result = sort_all(final)
letter_s = sorted_result [0]
freq = sorted_result [1]
freq = get_rel_freq(freq)
print(sorted_result)

# create the histogram
fig = pl.figure()
ax = pl.subplot(111)
width=0.8
ax.bar(range(len(letter_s)), freq, width=width)
ax.set_xticks(np.arange(len(letter_s)) + width/2)
ax.set_xticklabels(letter_s, rotation=45)
pl.show()
