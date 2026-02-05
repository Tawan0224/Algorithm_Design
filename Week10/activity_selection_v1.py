#Soe Min Min Latt
#6611938
#541

#Earliest finish time first
n = int(input())
activities = []
for i in range(n):
    s, f = map(int, input().split())
    activities.append((s, f))


def activity_selection_v1(activities):
    activities.sort(key=lambda x: x[1])

    count = 0
    last_finish = 0
    for start, finish in activities:
        if start > last_finish:
            count += 1
            last_finish = finish

    return count

result = activity_selection_v1(activities)
print(result)