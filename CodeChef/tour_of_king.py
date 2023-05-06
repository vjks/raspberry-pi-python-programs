num_cases = int(input())

for x in range(num_cases):
    seats = input().split()
    n_cars = int(seats[0])
    m_cars = int(seats[1])
    print(n_cars * 5 + m_cars * 7)