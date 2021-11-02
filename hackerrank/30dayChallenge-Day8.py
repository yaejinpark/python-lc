# Enter your code here. Read input from STDIN. Print output to STDOUT

x = int(input())
phoneNum = []
phoneBook = {}

for num in range(x):
    phoneNum.append(input().split())

for name,num in phoneNum:
    phoneBook[name] = num

while True:
    try:
        inputName = input()
        if inputName in phoneBook:
            print(inputName+"="+phoneBook[inputName])
        else:
            print("Not found")
    except:
        break
