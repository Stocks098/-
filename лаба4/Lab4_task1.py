# TODO решите задачу

def task() -> float:
    summa = 0
    s1 = 0
    s2 = 0
    f = open("input.json", "r")
    a = f.readlines()
    for i in range(len(a)):
        if a[i].find("score") != -1:
            s1 = float(a[i][((a[i].find("score"))+8):len(a[i])-2])
        elif (a[i].find("weight")) != -1:
            s2 = float(a[i][((a[i].find("weight"))+9):len(a[i])-1])
        if(s1 != 0) and (s2 != 0):
            summa += s1*s2
            s1, s2 = 0, 0
    f.close()
    return round(summa, 3)

print(task())


