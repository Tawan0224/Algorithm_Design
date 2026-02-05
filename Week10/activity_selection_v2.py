#Soe Min Min Latt
#6611938
#541

#Earliest start time first
n = int(input())
activities = []

for _ in range(n):
    s, t = map(int, input().split())
    activities.append((s, t))

def activity_selection_earliest_start(activities):
    activities.sort(key=lambda x: x[0])

    count = 0
    last_finish = -1

    for start, finish in activities:
        if start > last_finish:
            count += 1
            last_finish = finish

    return count

result = activity_selection_earliest_start(activities)
print(result)
