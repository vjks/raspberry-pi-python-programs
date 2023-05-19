num_tests = int(input())

for x in range(num_tests):
    journey_length, song_duration = map(int, input().split())
    print(journey_length // (3 * song_duration))