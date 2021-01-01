if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

for name in student_marks:
    new_mark = sum(student_marks[name])/len(student_marks[name])
    student_marks[name] = new_mark

print("{:.2f}".format(student_marks[query_name]))