a = 0
t = 0
f = 0
for i in range(1000):
  if i % 3 == 0:
      a += 1
      t += 1
  if i % 5 == 0:
      a += 1
      f += 1

print(f"sum: {a} five: {f} Tree: {t}")
