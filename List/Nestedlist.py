'''
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
[['Tina', 37.2], ['Harry', 37.21], ['Berry', 37.21], ['Harsh', 39.0], ['Akriti', 41.0]]
'''
def sort_score(marksheet):
    return marksheet[1]
marksheet = [[input(),float(input())]for _ in range(int(input()))]
marksheet.sort(key=sort_score)
l = []
for i in range(1,len(marksheet)):
    if i>=1 and i<len(marksheet)-1:
        if marksheet[i][1] == marksheet[i+1][1]:
            l.append(marksheet[i][0])
            l.append(marksheet[i+1][0])
    else :
        break
l.sort()
print(l)
'''
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students = sorted(students, key = lambda x: x[1])
    #print(students)
    #second_lowest_score = students[1][1]
    second_lowest_score = sorted(list(set([x[1] for x in students])))[1]
    desired_students = []
    for stu in students:
        if stu[1] == second_lowest_score:
            desired_students.append(stu[0])
    print("\n".join(sorted(desired_students)))'''