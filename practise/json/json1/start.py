# в данном примере разберём пользовательское кодирование и декодирование данных
# можно создать методы, которые будут считываться перед сериализацией и десериализацией данных


import json


class Magic(object):

    def __init__(self, name, age, power):
        self.name = name
        self.age = age
        self.power = power

    # сериализуем данные
    @staticmethod
    def get_data(self):
        return {
            "name": self.name,
            "age": self.age,
            "power": self.power
        }

    # тестовый метод класса
    @classmethod
    def get_class(cls, age):
        return cls(age, 32, 100)

    # десериализуем данные
    @staticmethod
    def des_data(data):
        return [data["name"], data["age"], data["power"]]


# сериализуем данные
mag = Magic.get_class(120)
data = json.dumps(mag, default=Magic.get_data)
print(data, type(data))


# десериализуем данные
data = json.loads(data, object_hook=Magic.des_data)
print(data, type(data))
