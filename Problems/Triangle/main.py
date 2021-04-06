n = int(input())

ch = "#"

for i in range(1, 2 * n, 2):
    print((ch * i).center(2 * n - 1))
