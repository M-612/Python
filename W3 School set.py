toys = {"gun", "ball", "bat"}
toys.add("Teddy")
print(toys)

toys = {"gun", "ball", "bat"}
toys.clear()
print(toys)

toys= {"gun", "ball", "bat"}
x = toys.copy()
print(x)

x = {"gun", "ball", "bat"}
y = {"AC", "cooler", "fan"}
z = x.difference(y)
print(z)

toys = {"gun", "ball", "bat"}
toys.discard("ball")
print(toys)

x = {"gun", "ball", "bat"}
y = {"AC", "cooler", "fan"}
z = x.intersection(y)
print(z)

x = {"gun", "ball", "bat"}
y = {"AC", "cooler", "fan"}
x.intersection_update(y)
print(x)

x = {"gun", "ball", "bat"}
y = {"AC", "cooler", "fan"}
z = x.isdisjoint(y)
print(z)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

toys = {"ball", "bat", "gun"}
toys.pop()
print(toys)

toys = {"ball", "bat", "gun"}
toys.remove("gun")
print(toys)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

x = {"gun", "ball", "bat"}
y = {"AC", "cooler", "fan"}
x.symmetric_difference_update(y)
print(x)


x = {"gun", "ball", "bat"}
y = {"AC", "cooler", "fan"}
z = x.union(y)
print(z)


x = {"gun", "ball", "bat"}
y = {"AC", "cooler", "fan"}
x.update(y)
print(x)



