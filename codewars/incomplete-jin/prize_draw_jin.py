# https://www.codewars.com/kata/5616868c81a0f281e500005c
def rank(st, we, n):
    names = [name for name in st.split(",")] # list of names

    # cases for not having enough participants
    if len(st) == 0:
        return "No participants"
    if n > len(names):
        return "Not enough participants"

    winning_numbers = []

    for i in range(0,len(names)):
        som = 0 # set som to 0 initially and reset after each name iteration
        for char in names[i].lower():
            som += (ord(char) - 96) # ord(char) - 96 gives the number of the order the alphabet is in
        som += len(names[i])
        winning_numbers.append(som*we[i])

    # zip names and winning number into list of tuples and order them by number descending
    participants = sorted(zip(names,winning_numbers), key=lambda x:x[1],reverse=True)
    final_participants = [i for i in participants[i][0]]
    print(final_participants)
    return participants[n-1][0]

rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4)
rank("Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden", [1, 3, 5, 5, 3, 6], 2)
rank("Aubrey,Olivai,Abigail,Chloe,Andrew,Elizabeth", [3, 1, 4, 4, 3, 2], 4)
rank("Lagon,Lily", [1, 5], 2)