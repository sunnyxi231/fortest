import sys
while True:
    try:
        n,m = map(int,sys.stdin.readline().strip().split())
        student_score = list(map(int,sys.stdin.readline().strip().split()))
        for i in range(m):
            line = input().split()
            A = int(line[1])
            B = int(line[2])
            C = line[0]
            if C =="Q":
                start,end = sorted([A,B])
                Amax = max(student_score[start-1:end])
                print(Amax)
            else: student_score[A-1] = B
    except:
        break
'''while True:
    try:
        a, b = map(int, input().split())
        grades = list(map(int, input().split()))
        for i in range(b):
            command = input().split()
            if command[0] == "Q":
                start, end = sorted([int(command[1]), int(command[2])])
                print(max(grades[start - 1:end]))
            else: grades[int(command[1]) - 1] = int(command[2])
    except:
        break'''







