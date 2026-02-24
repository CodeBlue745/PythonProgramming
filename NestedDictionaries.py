'''
Directions for NestedDictionaries
The following program uses nested dictionaries to store a small music library. Extend the program so a user can add artists, albums, and songs to the library. First, add a command that adds an artist name to the music dictionary. Then add commands for adding albums and songs. Take care to check that an artist exists in the dictionary before adding an album, and that an album exists before adding a song.
'''

'''
Example input: Metallica, Master of Puppets, Fuel
Example output: { 'Metallica': { 'Master of Puppets': { 'songs': [Fuel], 'year': '', 'platinum': '' } } }
'''

music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': [ 'Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973,
            'platinum': True
        },
        'The Wall': {
            'songs': [ 'Another Brick in the Wall', 'Mother', 'Hey you'],
            'year': 1979,
            'platinum': True
        }
    },
    'Justin Bieber': {
        'My World':{
            'songs': ['One Time', 'Bigger', 'Love Me'],
            'year': 2010,
            'platinum': True
        }
    }
}

# Get user input
userInput = input('Add an artist, album or song separated by comma: ').split(',')

# While user input != 'exit'
    # ....
while userInput != 'exit':
    if len(userInput) == 1:
        if userInput[0] in music:
            print('Artist already exists')
        else:
            music.update({
                userInput[0] : {
                    'empty Album' : {
                        'empty Song' : [],
                        'year' : '',
                        'platinum' : ''
                    }
                }
            })#add artist
    elif len(userInput) == 2:
        if userInput[0] in music and userInput[1].strip() in music[userInput[0]]:
            print('Artist and Album already exists')
            print(music[userInput[0]][userInput[1]])
        else:
            music.update({
                userInput[0] : {
                    userInput[1] : {
                        'empty Song' : [],
                        'year' : '',
                        'platinum' : ''
                    }
                }
            })#add artist and album
    elif len(userInput) == 3:
        if userInput[0] in music and userInput[1] in music[userInput[0]] and userInput[2] in music[userInput[0]][userInput[1]]['songs']:
            print('Artist, Album or Song already exists')
        else:
            music.update({
                userInput[0] : {
                    userInput[1] : {
                        'songs' : [userInput[2]],
                        'year' : '',
                        'platinum' : ''
                    }
                }
            })#add artist, album and song
    else:
        print('Invalid input, please enter artist, album or song separated by comma.')
    print(music)
    userInput = input('Add an artist, album or song separated by comma: ').split(',')