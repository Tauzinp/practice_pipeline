class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " years old")

    def birthday(self):
        self.age += 1

    def setBuddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self


jina = dog("Jina", 10)
jina.name
jina.doginfo()

veve = dog("Vévé", 2)
veve.age
veve.doginfo()
veve.birthday()
veve.doginfo()

jina.setBuddy(veve)
jina.buddy.name
veve.buddy.name
jina.birthday()
veve.buddy.age

veve.buddy.doginfo()
