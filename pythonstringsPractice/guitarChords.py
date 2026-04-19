user_chord = input()

''' Type your code here. '''
if user_chord == 'G':
    print('e|-3-\nB|-0-\nG|-0-\nD|-0-\nA|-2-\nE|-3-')
elif user_chord == 'C':
    print('e|-0-\nB|-1-\nG|-0-\nD|-2-\nA|-3-\nE|---')
elif user_chord == 'D':
    print('e|-2-\nB|-3-\nG|-2-\nD|-0-\nA|---\nE|---')
else:
    print(f'{user_chord} is not a supported chord.')


