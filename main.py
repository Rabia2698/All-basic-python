def tabel_final_list(subject_list, no_of_student, mark_list, grade_list, pngk_result, username_list):
    long_dash = '-'* ((len(f'{"No.":<5}{"Name":<15}{"PNGK":<10}'))+ (len(subject_list) * 10))
    print(long_dash)
    print(f'{"No.":<5}{"Name":<15}', end='')
    for subj in subject_list:
        print(f'{subj.title():<11}', end='')
    print(f'{"PNGK":<10}')
    print(long_dash)

    for i in range(no_of_student):
        print(f'{i + 1:<5}{username_list[i].title():<15}', end='')
        for subj in subject_list:
            print(f'{mark_list[subj][i]:<3}{grade_list[subj][i]:<8}', end='')
        print(f'{pngk_result[i]:<10}')
    print(long_dash)

def check_pngk(grade):
    if grade == 'A':
        return 4.0
    elif grade == 'B':
        return 3.0
    elif grade == 'C':
        return 2.0
    elif grade == 'D':
        return 1.0
    elif grade == 'F':
        return 0.0
    else:
        return 0.0

def total_pngk(no_of_student, subject_list, grade_list):
    pngk_result = []
    for i in range(no_of_student):
        total_pngk = 0
        for subj in subject_list:
            pngk_value = check_pngk(grade_list[subj][i])
            total_pngk = total_pngk + pngk_value
        pngk_result.append(total_pngk/len(subject_list))
    return pngk_result

def grade(marks):
    if marks >= 80 and marks <= 100:
        return "A"
    elif marks >= 70 and marks < 80:
        return "B"
    elif marks >= 60 and marks < 70:
        return "C"
    elif marks >= 50 and marks < 60:
        return "D"
    elif marks > 100 or marks < 0:
        return "invalid"
    else:
        return "F"

def mark_subject(subject_list, no_of_student):
    username_list = []
    mark_list = {subj: [] for subj in subject_list}
    grade_list = {subj: [] for subj in subject_list}  # Dictionary for subject grades

    for i in range(no_of_student):
        username = input(f'Enter student name {i +1}: ')
        username_list.append(username)
        for subj in subject_list:
            mark = int(input(f'Enter {subj} mark for {username}: '))
            grade_result = grade(mark)
            if grade_result == 'invalid':
                print("Invalid marks entered. Please enter valid marks.")
                mark = int(input(f'Enter valid marks: '))
                grade_result = grade(mark)
            mark_list[subj].append(mark)
            grade_list[subj].append(grade_result)
    return mark_list, grade_list, username_list

def main():
    subject_list = []
    no_of_subject = int(input('Enter number of subject: '))
    no_of_student = int(input('Enter number of student: '))
    
    for i in range(no_of_subject):
        subject = input(f'Enter your subject {i + 1}: ')
        subject_list.append(subject)
    
    mark_list, grade_list, username_list = mark_subject(subject_list, no_of_student)
    pngk_result = total_pngk(no_of_student, subject_list, grade_list)
    tabel_final_list(subject_list, no_of_student, mark_list, grade_list, pngk_result, username_list)

if __name__ == "__main__":
    main()

