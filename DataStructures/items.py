items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 11)
]

items.sort(key=lambda item: item[1])
print(items)
