def word_count(s):
    # Your code here
    
    # remove the key:
    '''
    " : ; , . - + = / \ | [ ] { } ( ) * ^ &
    '''

    table = {ord(i): None for i in '":;,.-+=/\|[]{}()*^&'}
    # print(table)
    # s = s.lower()
    filteredString = s.lower().translate({ord(i): None for i in '":;,.-+=/\|[]{}()*^&'})

    # case is ignored so change to lowercase
    wordCount = {}
    if filteredString == "":
        return wordCount
    else:
        # split on white spaces
        arrString = filteredString.split()

        # count the arrString and place in dict
        for x in arrString:
            if x in wordCount:
                wordCount[x] += 1
            else:
                wordCount[x] = 1

        return wordCount





if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))