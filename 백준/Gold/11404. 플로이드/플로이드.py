city_cnt = int(input())
bus_cnt = int(input())

distances = [[float('inf')] * (city_cnt+1) for _ in range(city_cnt+1)]

for _ in range(bus_cnt):
    start_city, end_city, cost = map(int, input().split())
    distances[start_city][end_city] = min(cost, distances[start_city][end_city])

for start in range(1, city_cnt+1):
    for end in range(1, city_cnt+1):
        if start == end:
            distances[start][end] = 0

for thru in range(1, city_cnt+1):
    for start in range(1, city_cnt+1):
        for end in range(1, city_cnt+1):
            distances[start][end] = min(distances[start][end], distances[start][thru] + distances[thru][end])

for start in range(1, city_cnt+1):
    for end in range(1, city_cnt+1):
        dist = distances[start][end]
        if dist == float('inf'):
            print("0", end=' ')
        else:
            print(dist, end=' ')
    print()