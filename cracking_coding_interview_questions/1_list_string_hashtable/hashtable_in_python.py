# value = hash_key
# 10 = a
# 11 = b
# 12 = c
# 13 = [d, d1, d2]
# 14 = e


class HashTable(object):
    table = [None] * 256

    @staticmethod
    def get_value(key):
        total = 0
        for i in range(len(key)):
            total += ord(key[i]) * (7**i)
        return (len(key) * total) % 256

    def insert(self, key):
        val = self.get_value(key)
        if self.table[val] is None:
            self.table[val] = key
        else:
            if type(self.table[val]) == list:
                self.table[val].append(key)
            else:
                self.table[val] = [self.table[val], key]

    def delete(self, key):
        val = self.get_value(key)
        if self.table[val] is not None:
            if type(self.table[val]) == list:
                i = self.table[val].index(key)
                self.table[val][i] = None
                self.table[val].remove(None)
            else:
                self.table[val] = None
        else:
            KeyError()

    def lookup(self, key):
        val = self.get_value(key)
        if type(self.table[val]) == list:
            found = key in self.table[val]
        else:
            found = self.table[val] == key
        return found


h = HashTable()
h.insert("abc")
h.insert("xyz")
h.insert("abc")
print(h.table)
h.lookup("abc")
h.delete("xyz")
print(h.table)
h.delete("abc")
print(h.table)
