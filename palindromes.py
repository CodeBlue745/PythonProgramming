''' Enter a word or phrase and determine if it is a palindrome.
A palindrome is a word or phrase that reads the same forwards and backwards, ignoring spaces, punctuation, and capitalization. 
For example, "A man, a plan, a canal, Panama!" is a palindrome. '''
wordInput = input()
combinedForwardWord = ''
combinedReverseword = ''

strippedWord = wordInput.strip()
strippedsplitWord = wordInput.strip().split()
for i in strippedWord:
    if i == ' ':
        continue
    else:
        combinedForwardWord += i
listForward = [combinedForwardWord]
if len(strippedsplitWord) == 1:
    for i in strippedsplitWord:
        combinedReverseword = i[::-1]
elif len(strippedsplitWord) > 1:
    for i in listForward:
        combinedReverseword += i[::-1]


if combinedReverseword == combinedForwardWord:
    print(f'palindrome: {strippedWord}')
else:
    print(f'not a palindrome: {strippedWord}')

#print(combinedReverseword)