rooms = int(input())
roomAccommodate = []
count = 0

for i in range(rooms):
    people, accommodate = map(int, input().split())
    roomAccommodate.append(accommodate - people)

    if roomAccommodate[i] >= 2:
        count += 1

print(count)