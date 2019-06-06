# opening input file wordcount.txt in readable format
file = open("wordcount.txt","r+")
# creating a dictionary  to store Words and count (key, value)
wordcount = {}
# splitting words in each line and counting each occurance of a word.. this loop repeat untill end of a file
for word in file.read().split():
    # if word occurs 1st time,assigning 1 and if word repeats incrementing count each tome
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for item in wordcount.items():
    # printing output in console
    print("{}\t{}".format(*item))
    # storing output to a file named output.txt
    print("{}\t{}".format(*item),file=open("output.txt", "a"))
file.close();