tea_type = int(input())
x = 0
inputs = input().split()
inputs = list(map(int, inputs))
for i in range(5):
    if inputs[i] == tea_type:
        x += 1

print(x)
