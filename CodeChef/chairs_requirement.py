num_tests = int(input())

for x in range(num_tests):
    new_chairs = 0
    students_and_chairs = input().split()
    num_students = int(students_and_chairs[0])
    num_chairs = int(students_and_chairs[1])
    if num_students > num_chairs:
        new_chairs = num_students - num_chairs
    print(new_chairs)