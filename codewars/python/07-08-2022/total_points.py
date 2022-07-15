"""
Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.

For example: ["3:1", "2:2", "0:1", ...]

Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:

if x > y: 3 points
if x < y: 0 point
if x = y: 1 point
Notes:

there are 10 matches in the championship
0 <= x <= 4
0 <= y <= 4
"""
def points(games):
    current_points = 0
    
    for score in games:
        if score[0] > score[2]:
            current_points += 3
        elif score[0] == score[2]:
            current_points += 1
    return current_points

# Smarter solution
def points2(a):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))

"""
for x, y in (s.split(":") for s in a) - this iterates over scores array taking each team's number of goals as x and y:

["1:1", "1:2", "2:1"] =>
  x = "1", y = "1"
  x = "1", y = "2"
  x = "2", y = "1"
(x >= y) + 2 * (x > y) - this compares scores (alphabetically, but that's okay with current constraints):

if x is less than y, this becomes 0 + 2 * 0 => 0
if x is greater or equal to y, this becomes 1 + 2 * 0 => 1
and if x is strictly greater than y, this becomes 1 + 2 * 1 => 3
This can also be rewritten as 0 if x < y else 1 if x == y else 3 if x > y, but that's a lot longer isn't it?

In the end all values are summed up.

"""