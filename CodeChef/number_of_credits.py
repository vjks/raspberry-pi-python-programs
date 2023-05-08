num_tests = int(input())

for x in range(num_tests):
    courses = input().split()
    x_courses = int(courses[0])
    y_courses = int(courses[1])
    z_courses = int(courses[2])
    print( 4 * x_courses + 2 * y_courses)