def dictionary_input_1d(n):
    d1 = {}
    for i in range(n):
        a = input().split()
        if a[0] == 'name':
            d1[a[0]] = a[1] + a[2]
        else:
            d1[a[0]] = list(map(int,a[1: :1]))
    return d1

def get_avg(marks):
    total = float(sum(marks))
    return total/len(marks)
def total_avg(students):
    assignment = get_avg(students['assignment'])
    test = get_avg(students['test'])
    lab = get_avg(students['lab'])
    return (0.1 * assignment + 0.7 * test + 0.2 * lab)
def grade(score):
    if score >= 90 :
        return "A"
    elif score >= 80 :
        return "B"
    elif score >= 70 :
        return "C"
    elif score >= 60 :
        return "D"
    else:
        return "E"
def class_avg(students):
    resut = []
    for student in students:
        stud_avg = total_avg(student)
        resut.append(stud_avg)
        return get_avg(resut)
if __name__ =="__main__":
    jack = dictionary_input_1d(4)
    james = dictionary_input_1d(4)
    dylan = dictionary_input_1d(4)
    jess = dictionary_input_1d(4)
    tom = dictionary_input_1d(4)
    students = [jack, james, dylan, jess, tom]
    for i in students:
        print(f"{i['name']}\nAverage marks {i['name']}is {total_avg(i)}")
        print(f"Letter grade {i['name']}is {grade(total_avg(i))}")
        print()
    class_av = class_avg(students)
    print(f"class avg is{class_av}\nletter grade of class is{grade(class_av)}")