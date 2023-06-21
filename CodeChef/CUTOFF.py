tests = int(input())

for test in range(tests):
    num_students, students_passed = map(int, input().split())
    list_students = list(map(int, input().split()))

    list_students.sort(reverse = True)
    
    print(list_students[students_passed - 1] - 1)
    