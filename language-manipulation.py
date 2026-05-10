from collections import Counter
from string import count
import numpy as np
import matplotlib.pyplot as plt



a = 'I I am am the the alpha alpha alpha and and the the omega omega'
words = a.lower().split()

wordCount = Counter(words)


#print wordCount
#print("\n".join(wordCount))
#print result
file = open('montecristo.txt', "r")
a = file.read()


words = a.lower().split()
wordCount = Counter(words)



author_names = wordCount.keys()
author_counts = wordCount.values()

# Plot histogram using matplotlib bar().
indexes = np.arange(len(author_names))
width = 0.7
plt.bar(indexes, author_counts, width)
plt.xticks(indexes + width * 0.3, author_names, rotation='vertical')
plt.show()
