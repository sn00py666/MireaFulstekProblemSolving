class Node:
    def __init__(self, data):
        self.data = data  # Данные узла
        self.next = None  # Ссылка на следующий узел (изначально None)


"""класс работает в формате[ключ, значение, значене...] """
class HashTable:
    def __init__(self, arr=None):
        if arr == None:
            self.buckets_count = 128
            self.hash_table = [None] * self.buckets_count
            self.items_count = 0
            return
        self.buckets_count = len(arr) * 2
        self.hash_table = [None] * self.buckets_count
        self.items_count = 0
        for elem in arr:
            self.add(elem)

    def add(self, key_elem):
        if self.items_count / self.buckets_count >= 0.75:
            self.re_creation_hash_table()
        hash_key_value = hash(key_elem[0]) % self.buckets_count
        new_node = Node(key_elem)
        if self.hash_table[hash_key_value] is None:
            self.hash_table[hash_key_value] = new_node
            self.items_count += 1
            return
        
        last_node = self.hash_table[hash_key_value]
        if last_node.data[0] == key_elem[0]:
            last_node.data.append(key_elem[-1])
            return
        while last_node.next:
            last_node = last_node.next
            if last_node.data[0] == key_elem[0]:
                last_node.data.append(key_elem[-1])
                return
        last_node.next = new_node
        self.items_count += 1

    def re_creation_hash_table(self):
        old_hash_table = self.hash_table
        self.buckets_count = self.buckets_count * 2
        self.items_count = 0
        self.hash_table = [None] * self.buckets_count
        for elem in old_hash_table:
            if elem is None:
                pass
            else:
                while elem:
                    self.add(elem.data)
                    elem = elem.next
        del old_hash_table

    def remove(self, key_values):
        hash_key_value = hash(key_values[0]) % self.buckets_count
        node = self.hash_table[hash_key_value]
        
        if node is None:
            return "Нет такого ключа"
        
        # Если первый узел содержит нужный ключ
        if node.data[0] == key_values[0]:
            if len(node.data) > 2:
                # Если в списке несколько значений для одного ключа
                node.data.remove(key_values[1])
            else:
                # Если только одно значение и нужно удалить сам узел
                self.hash_table[hash_key_value] = node.next
            self.items_count -= 1
            return
        
        # Поиск ключа в цепочке
        prev_node = None
        while node:
            if node.data[0] == key_values[0]:
                if len(node.data) > 2:
                    # Удаляем только значение, если для одного ключа несколько значений
                    node.data.remove(key_values[1])
                else:
                    # Удаляем весь узел
                    prev_node.next = node.next
                self.items_count -= 1
                return
            prev_node = node
            node = node.next
        
        return "Нет такого ключа"

    def search(self, key):
        hash_key_value = hash(key) % self.buckets_count
        if self.hash_table[hash_key_value] is None:
            return "Нет такого ключа"
        
        node = self.hash_table[hash_key_value]
        if node.data[0] == key:
            return node.data[1:]
        while node.data[0] and node.next:
            node = node.next
            if node.data[0] == key:
                res = str(node.data[1]) if len(node.data[1:]) == 1 else node.data[1:]
                return res
        else: return "Нет такого ключа"

    def desplay(self, visibility=0):
        for elem in self.hash_table:
            if elem is None:
                if visibility == 1:
                    print(None)
            else:
                while elem:
                    print(str(elem.data[0]) + ": " + ", ".join(elem.data[1:]))
                    elem = elem.next
                

test = HashTable(arr=[[1,"1"],[2,"2"],[3,"3"],[4,"4"], [12,"12"]])
test.desplay()

print()
phone_book = HashTable(arr=[["Иванов", "123-456-789"], ["Петров", "987-654-321"]])

phone_book.add(["Сидоров", "555-555-555"])
phone_book.add(["Иванов", "111-222-333"])
phone_book.desplay()
print()
print("Иванов:", phone_book.search("Иванов"))
phone_book.remove(["Иванов", "123-456-789"])
print("Иванов после удаления:", phone_book.search("Иванов"))

