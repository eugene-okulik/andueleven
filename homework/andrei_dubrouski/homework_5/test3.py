students = ['Ivanov', 'Petrov', 'Sidorov']

<<<<<<< HEAD
subjects = ['math', 'biology', 'geography']

surname1, surname2, surname3 = students

subject1, subject2, subject3 = subjects

my_text = f'Students {surname1}, {surname2}, {surname3} study these subjects: {subject1}, {subject2}, {subject3}'

print(my_text)
=======
text1 = str(', '.join(students))

subjects = ['math', 'biology', 'geography']

text2 = str(', '.join(subjects))

print(f'Students {text1} study these subjects: {text2}')
>>>>>>> 4a4b8f47735cb2a44624295b1ac7f19ca9465666
