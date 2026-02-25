from os import name


class dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " years")

    def birthday(self):
        self.age += 1


jina = dog("jina", 10)
print(jina.age)
print(jina.name)
jina.name

jina.doginfo()

filou = dog("Filou", 2)
veve = dog("Veve", 3)

filou.doginfo()
veve.doginfo()

jina.age = 11

jina.doginfo()

jina.birthday()
jina.doginfo()
jina.birthday()
jina.doginfo()
