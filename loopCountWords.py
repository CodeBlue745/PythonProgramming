''' Type your code here. '''
lineofText = input()

countWords = 0
wordwasCounted = False
strippedText = lineofText.strip()
for i in strippedText:
    if i == ' ':
        wordwasCounted = False
    elif ord(i) in range(65, 122) and wordwasCounted == False:
        countWords += 1
        wordwasCounted = True
    else:
        pass
        
print(countWords)