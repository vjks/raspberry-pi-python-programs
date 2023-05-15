num_tests = int(input())

for x in range(num_tests):
    a_marks, b_marks, c_marks = map(int, input().split())
    total_marks = a_marks + b_marks + c_marks
    if total_marks >= 100:
        if a_marks >= 10 and b_marks >= 10 and c_marks >= 10:
            print("PASS")
        else:
            print("FAIL")
    else:
        print("FAIL")