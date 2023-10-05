class MyHashMap:

    def __init__(self):
        self.l = []

    def put(self, key: int, value: int) -> None:
        
        if len(self.l) == 0:
            x = [key, value]
            self.l.append(x)
        else:
            found = False
            for sublist in self.l:
                if sublist[0] == key:
                    sublist[1] = value
                    found = True
                    break
                
            if not found:
                    x = [key, value]
                    self.l.append(x)

    def get(self, key: int) -> int:
        if len(self.l) > 0:
            for sublist in self.l:
                if sublist[0] == key:
                    return sublist[1]       
        return -1

    def remove(self, key: int) -> None:
        if len(self.l) > 0:
            for sublist in self.l:
                if sublist[0] == key:
                    self.l.remove(sublist)
        return -1