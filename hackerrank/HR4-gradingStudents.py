if __name__ == '__main__':

    n = int(input())
    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    for grade in grades:
        rounded = grade
        if grade < 38:
            grade = grade
        while rounded % 5 != 0 :
            rounded += 1
        if rounded - grade < 3 and grade >= 38:
            grade = rounded
        print(grade)