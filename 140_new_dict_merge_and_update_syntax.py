print("----------- merge and update dicts before 3.9 ------------")
d1 = dict(a="a", b="b")
d2 = dict(b="B", c="C")
print(f"{d1=}")
print(f"{d2=}")

# Merging
d3 = {**d1, **d2}  # d2 is the one that should have priority in terms of values
print(f"after merged. {d3=}")

# Updating
d1.update(d2)
print(f"after d1 updated. {d1=}")


print("----------- merge and update dicts in 3.9 ------------")
d1 = dict(a="a", b="b")
d2 = dict(b="B", c="C")
print(f"{d1=}")
print(f"{d2=}")

# Merging
d3 = d1 | d2  # d2 is the one that should have priority in terms of values
print(f"after merged. {d3=}")

# Updating
d1 |= d2
print(f"after d1 updated. {d1=}")