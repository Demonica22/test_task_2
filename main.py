"""
Есть массив объектов, которые имеют поля id и parent, через которые их можно связать в дерево и некоторые произвольные поля.

Нужно написать класс, который принимает в конструктор массив этих объектов и реализует 4 метода:
#  - getAll() Должен возвращать изначальный массив элементов.
#  - getItem(id) Принимает id элемента и возвращает сам объект элемента;
#  - getChildren(id) Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента,
# чей id получен в аргументе. Если у элемента нет дочерних, то должен возвращаться пустой массив;
#  - getAllParents(id) Принимает id элемента и возвращает массив из цепочки родительских элементов,
# начиная от самого элемента, чей id был передан в аргументе и до корневого элемента,
# т.е. должен получиться путь элемента наверх дерева через цепочку родителей к корню дерева. Порядок элементов важен!

Требования: максимальное быстродействие, следовательно, минимальное количество обходов массива при операциях,
 в идеале, прямой доступ к элементам без поиска их в массиве.

"""


class TreeStore:
    def __init__(self, items):
        self.storage = {elem["id"]: elem for elem in items}

    def getAll(self):
        return list(self.storage.values())

    def getItem(self, id):
        return self.storage[id]

    def getChildren(self, id):
        return list(filter(lambda elem: elem['parent'] == id, self.storage.values()))

    def getAllParents(self, id):
        all_parents = []
        while self.storage[id]['parent'] != 'root':
            all_parents.append(self.storage[self.storage[id]['parent']])
            id = self.storage[id]['parent']
        return all_parents


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

ts = TreeStore(items)

assert ts.getAll() == [{'id': 1, 'parent': 'root'}, {'id': 2, 'parent': 1, 'type': 'test'},
                       {'id': 3, 'parent': 1, 'type': 'test'}, {'id': 4, 'parent': 2, 'type': 'test'},
                       {'id': 5, 'parent': 2, 'type': 'test'}, {'id': 6, 'parent': 2, 'type': 'test'},
                       {'id': 7, 'parent': 4, 'type': None}, {'id': 8, 'parent': 4, 'type': None}]

assert ts.getItem(7) == {'id': 7, 'parent': 4, 'type': None}
assert ts.getChildren(4) == [{'id': 7, 'parent': 4, 'type': None}, {'id': 8, 'parent': 4, 'type': None}]
assert ts.getChildren(5) == []
assert ts.getAllParents(7) == [{"id": 4, "parent": 2, "type": "test"}, {"id": 2, "parent": 1, "type": "test"},
                               {"id": 1, "parent": "root"}]
