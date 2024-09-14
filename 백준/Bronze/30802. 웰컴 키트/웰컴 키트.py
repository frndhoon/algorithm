N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

shirt_bundle = 0
for size in sizes:
  if size == 0:
    continue
  elif size <= T:
    shirt_bundle += 1
  elif size % T == 0:
    shirt_bundle += (size // T)
  else:
    shirt_bundle += (size // T) + 1

print(shirt_bundle)
print(N//P, N%P)