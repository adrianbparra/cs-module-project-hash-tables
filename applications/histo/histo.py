# Your code here

with open('robin.txt') as f:

    words = f.read()

    wordsArray = words.split()


    wordCount = {}

    # sepereate each word on how many times it is repeated
    for word in wordsArray:
        filteredWord = word.lower().translate({ord(i): None for i in '":;,.-+=/\|[]{}()*^&?'})
        # print(filteredWord)

        if filteredWord in wordCount:
            wordCount[filteredWord] += 1
        else:
            wordCount[filteredWord] = 1

    # display words on times it repeats
    # sort first
    # print values and skip the ones

    wordSorted = sorted(wordCount.items(),key= lambda x: x[1],reverse = True)

    # print(dict(wordSorted))

    for k,v in wordSorted:

        if v > 1:
            print("{:15s}".format(k),end=" ")
            print(f'{"#" * v} ')
            
        else:
            break

    f.close()