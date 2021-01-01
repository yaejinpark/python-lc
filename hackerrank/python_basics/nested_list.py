#Given the names and grades for each student in a Physics class of  students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

res = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    res.append([name, score])

wanted_score = sorted(set([score for name, score in res]))[1]
# The reason why set is used is because set doesn't allow duplicates.
# This method guarantees to find the second lowest score.

print(('\n').join([name for name, score in sorted(res) if score == wanted_score]))

#When a list is nested and I use sorting,
# sorting will be done with the leftmost elements of the nested list within the list.