import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
    # split txt file into array
    wordArray = words.split()

    wordTypes = {}

    startingWords = []

    # loop over array
    for i in range(len(wordArray)-1):

        # create the array of starting words
        if wordArray[i][0] in ['"', "'"] and wordArray[i][1].isupper():
            startingWords.append(wordArray[i])
        elif wordArray[i][0].isupper():
            startingWords.append(wordArray[i])

        # if word is already in dict of choices
        if wordArray[i] in wordTypes:
            
            # add the next word
            wordTypes[wordArray[i]].append(wordArray[i+1])

        else:

            # create new dict key and add the next word
            wordTypes[wordArray[i]] = [wordArray[i+1]]


    # print(wordTypes)
# TODO: construct 5 random sentences
# Your code here

    # chose random starting word

    startingWord = random.choice(startingWords)

    # print(startingWords)

    sentences = 1

    while sentences < 5:
        


        nextWord = random.choice(wordTypes[startingWord])

        # print(nextWord)
        prevChars =  nextWord[-2:]
        # prevChars = [let for let in nextWord[-2:]]

        # lastChar = nextWord[len(nextWord)-1]
        # print(prevChars)
        # check if word is a last word
        print(nextWord)
        print(prevChars[1], prevChars[0])

        startingWord = nextWord
        # print(startingWord, end=" ")

        if prevChars[1] in ['.','?','!'] or prevChars[0] in ['.','?','!'] and prevChars[1] in ["'", "'"]:
            
            # print('/n')
            sentences += 1



        pass



    f.close()
