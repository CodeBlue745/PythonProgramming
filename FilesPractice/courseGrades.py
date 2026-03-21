'''
Write a program that reads the student information from a tab separated values (tsv) file. The program then creates a text file that records the course grades of the students. Each row of the tsv file contains the Last Name, First Name, Midterm1 score, Midterm2 score, and the Final score of a student. A sample of the student information is provided in StudentInfo.tsv. Assume the number of students is at least 1 and at most 20. Assume also the last names and first names do not contain whitespaces.

The program performs the following tasks:

Read the file name of the tsv file from the user.
Open the tsv file and read the student information.
Compute the average exam score of each student.
Assign a letter grade to each student based on the average exam score in the following scale:
A: 90 =< x
B: 80 =< x < 90
C: 70 =< x < 80
D: 60 =< x < 70
F: x < 60
Compute the average of each exam.
Output the last names, first names, exam scores, and letter grades of the students into a text file named report.txt. Output one student per row and separate the values with a tab character.
Output the average of each exam, with two digits after the decimal point, at the end of report.txt. Hint: Use the format specification to set the precision of the output.

'''

# TODO: Declare any necessary variables here. 

reportFileName = "txtFiles/report.txt"
letterGrade = []
midterm1Score = 0
midterm2Score = 0
finalexamScore = 0
# TODO: Read a file name from the user and read the tsv file here. 
studentInfoFileName = input()#"txtFiles/StudentInfo.tsv"
with open(studentInfoFileName, 'r') as studentInfoFile:
    studentInfoList = studentInfoFile.readlines()
    for i in range(len(studentInfoList)):#number of students
        averageExamScore = 0
        
        for k in range(3):# 3 exams
            averageExamScore += float(studentInfoList[i].split('\t')[k + 2])# +2 because the first two columns are last name and first name
        averageExamScore /= 3
        if averageExamScore >= 90:
            letterGrade.append('A')
        elif averageExamScore >= 80 and averageExamScore < 90:
            letterGrade.append('B')
        elif averageExamScore >= 70 and averageExamScore < 80:
            letterGrade.append('C')
        elif averageExamScore >= 60 and averageExamScore < 70:
            letterGrade.append('D')
        else:
            letterGrade.append('F')
        midterm1Score += float(studentInfoList[i].split('\t')[2])
        midterm2Score += float(studentInfoList[i].split('\t')[3])
        finalexamScore += float(studentInfoList[i].split('\t')[4])
    midterm1Score /= len(studentInfoList)
    midterm2Score /= len(studentInfoList)
    finalexamScore /= len(studentInfoList)


# TODO: Compute student grades and exam averages, then output results to a text file here. 
with open(reportFileName, 'w') as reportFile:
    for i in range(len(studentInfoList)):
        reportFile.write(studentInfoList[i].strip() + '\t' + letterGrade[i] + '\n')
    reportFile.write('\nAverages: midterm1 ' + format(midterm1Score, '.2f') + ', midterm2 ' + format(midterm2Score, '.2f') + ', final ' + format(finalexamScore, '.2f') + '\n')