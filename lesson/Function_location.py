a_list = ["aaa", 'bb', 'cc', 'd']

# if any(a_list):
#     print(list(filter(None, a_list)))
#     print([i for i in a_list if i])

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Cat {self.name=}, {self.age=}'

if __name__ == '__main__':
    cats = [Cat('Tom', 3), Cat('Angela', 4), Cat('Peanut', 11)]
    # print(max(cats, key=lambda cat: cat.age))
    # print(min(cats, key=lambda cat: cat.age))
    # for line in iter(input, 'end'):
    #     print(line.upper())
    ints = [int(i) for i in iter(input, '')]
    print(ints)
    # print(max(a_list, key=len))
    # print(bool(a_list))
    # print(all(a_list))
    # print(any(a_list))
