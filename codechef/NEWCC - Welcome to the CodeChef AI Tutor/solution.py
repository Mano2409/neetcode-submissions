# cook your dish here
x, y = map(int, input().split())
if x < y:
    print("Old")
elif y < x:
    print("New")
else:
    print("Same")