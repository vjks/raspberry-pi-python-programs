tests = int(input())

for _ in range(tests):
    packet_2, packet_4 = map(int, input().split())
    cost1 = packet_2 * 5
    cost2 = (packet_4 * 2) + packet_2
    if(cost1 < cost2):
        print(cost1)
    else:
        print(cost2)