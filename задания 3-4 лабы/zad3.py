class Unique:
    def __init__(self, items, ignore_case=False):
        self.items = iter(items)
        self.found = set()
        self.ignore_case = ignore_case

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                item = next(self.items)
                key = item.lower() if self.ignore_case and isinstance(item, str) else item
                if key not in self.found:
                    self.found.add(key)
                    return item
            except StopIteration:
                raise StopIteration

data = [1, 1, 1, 2, 2, 3, 'a', 'A', 'b']

# Уникальные элементы без учета регистра
for item in Unique(data, ignore_case=True):
    print(item)

# Уникальные элементы с учетом регистра
for item in Unique(data):
    print(item)