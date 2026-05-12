user_rows = int(input())
user_cols = int(input())

''' Type your code here. '''
print('<table>')
for i in range(user_rows):
    print('<tr> ', end='')
    for j in range(user_cols):
        print('<td> c </td> ', end='')
    print('</tr>')
print('</table>')