def field(items, *args):

    for item in items:
        result = {}
        for key in args:
            if key in item:
                result[key] = item[key]
        if result:
            yield result if len(args) > 1 else list(result.values())[0]

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black', 'price': 5300}
]

for item in field(goods, 'title', 'price'):
    print(item)