print("----- Example 1 -----")
num = [1, 2, 3, 4, 5]
if ((size := len(num)) < 10):
    print(f"Length of list is small, {size=}")

print("----- Example 2 -----")
with open("simple.txt") as f:
    while (line := f.readline()) != "end":
        print(f"{line=}")

print("----- Example 3 -----")
data = [1, 2, 3, 4]
result = [y for x in data if (y := x % 3) != 0]
print(f"{result=}")
