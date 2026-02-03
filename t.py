def user(name, age):
    print(name, age)

data = {
    "name": "Om",
    "age": 20
}
user(**data)

a = {"x": 1}
b = {"y": 2}

c = {**a, **b}

print(c)