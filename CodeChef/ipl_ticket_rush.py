test_cases = int(input())

for x in range(test_cases):
    students_and_tickets = input().split()
    students = int(students_and_tickets[0])
    tickets = int(students_and_tickets[1])
    if tickets > students:
        print(0) # all the students will be able to see the math
    elif students > tickets:
        print(students - tickets ) # Only the number of students that are equal to the number of tickets will be able to see the match
    else:
        print(0) # if the number of tickets is equal to number of students then 0 students will not be able to see the match.