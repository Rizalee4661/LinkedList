

class Antrian:
    def __init__(self, val = None):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.main_value = None

    def masukan_antrian_pertama(self, new_value):
        new_antrian = Antrian(new_value)
        new_antrian .next = self.main_value
        self.main_value  = new_antrian

    def masukan_antrian_terakhir(self, new_value):
        new_antrian = Antrian(new_value)
        last_antrian= self.main_value
        while last_antrian.next:
            last_antrian = last_antrian.next

        last_antrian.next = new_antrian

    def awal(self):
        dataku = self.main_value
        while dataku is not None:
            print(dataku.val)
            dataku = dataku.next

myList = MyLinkedList()
myList.main_value = Antrian(1)

n2 = Antrian(2)
n3 = Antrian(3)

myList.main_value.next = n2
n2.next = n3

print("Antrian Awalnya")
myList.awal()
print("Antrian Setelahnya")
myList.awal()