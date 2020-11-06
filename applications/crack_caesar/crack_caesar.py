# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# go trough the txt file and create a dictinary of the alphabet and add 
# for total for each char occurance

# sort analysis in dict

# run trough the txt and decode the file with the dict taht was analized

with open('ciphertext.txt') as f:
    
    words = f.read()

    decypher = { }
    # letters = words.split()
    for letter in words:

        if letter.isalpha():
            # print(letter)
            
            if letter in decypher:

                decypher[letter] += 1
            else:
                decypher[letter] = 1
            
    
    decypher = dict(sorted(decypher.items(),key= lambda word: word[1], reverse = True))
        
    
    
    # print(decypher)

    alpha = ['E','T','A','O','H','N','R','I','S','D','L','W','U','G','F','B','M','Y','C','P','K','V','Q','J','X','Z']

    # loop over decypher to update the values

    idx = 0

    for i, v in decypher.items():

        if idx < 26:

            decypher[i] = alpha[idx]
            # print(i,v)
            idx += 1

    print(decypher)

    newText = ""
    
    for letter in words:

        if letter.isalpha():
            
            newText += str(decypher[letter])

        else:

            newText += str(letter)

    print(newText)

    f.close()
