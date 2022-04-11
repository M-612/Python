bag = {
  "brand": "Wildcraft",
  "model": "Schoolbag",
  "year": 1832
}
bag.clear()
print(bag)
bag = {
  "brand": "Wildcraft",
  "model": "Schoolbag",
  "year": 1832
}
x = bag.copy()
print(x)

x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

bag = {
  "brand": "Wildcraft",
  "model": "Schoolbag",
  "year": 1832
}
x = bag.get("model")
print(x)

bag = {
  "brand": "Wildcraft",
  "model": "Schoolbag",
  "year": 1832
}
x = bag.items()
print(x)

bag = {
  "brand": "Wildcraft",
  "model": "Schoolbag",
  "year": 1832
}
x = bag.keys()
print(x)

bag = {
  "brand": "Wildcraft",
  "model": "Schoolbag",
  "year": 1832
}
bag.pop("model")
print(bag)

bag = {
  "brand": "Wildcraft",
  "model": "Schoolbag",
  "year": 1832
}
bag.popitem()
print(bag)

bag = {
  "brand": "Wildcraft",
  "model": "Schoolbag",
  "year": 1832
}
x = bag.setdefault("model", "Bronco")
print(x)

bag = {
  "brand": "Wildcraft",
  "model": "Schoolbag",
  "year": 1832
}
bag.update({"color": "White"})
print(bag)

bag = {
  "brand": "Wildcraft",
  "model": "Schoolbag",
  "year": 1832
}
x = bag.values()
print(x)


