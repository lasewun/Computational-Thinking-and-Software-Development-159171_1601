#Tutorial 5 Part 2B - Roger Gilbertson - Student ID: 14292284 - 22.04.16


mathStudents = ['Audrey', 'Ben', 'Julia', 'Paul', 'Gerry', 'Sue', 'Helena', 'Harry', 'Marco', 'Rachel', 'Tina', 'Mark',
                'Jackson']
csStudents   = ['William', 'Aroha', 'Melissa', 'Sue', 'Ben', 'Audrey', 'Susan', 'Mark', 'Hemi', 'Brendan', 'Paul',
                'Barry', 'Julia']
def enrolCheck():
    index = 0
    for m in mathStudents:
        for cs in csStudents:
            if m == cs:
                (print('Student: ', m, 'is enrolled in both classes.'))
                index += 1
    print(index, 'student are enrolled in Computer Science and Maths.')


enrolCheck()
