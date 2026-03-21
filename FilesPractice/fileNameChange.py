'''
A photographer is organizing a photo collection about the national parks in the US and would like to annotate the information about each of the photos into a separate set of files. Write a program that reads the name of a text file containing a list of photo file names. The program then reads the photo file names from the text file, replaces the "_photo.jpg" portion of the file names with "_info.txt", and outputs the modified file names.

Assume the unchanged portion of the photo file names contains only letters and numbers, and the text file stores one photo file name per line. If the text file is empty, the program produces no output.
'''

getFileName = input()#txtFiles/ParkPhotos.txt

with open(getFileName, 'r') as file:
    for line in file:
        line = line.strip()#remove leading and trailing whitespace characters
        if line.endswith('_photo.jpg'):
            modified_name = line.replace('_photo.jpg', '_info.txt')
            print(modified_name)