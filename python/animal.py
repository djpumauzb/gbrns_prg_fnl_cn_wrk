# Родительский класс
class Animal:
    def __init__(self, name, animal_type, commands, birthday):
        self.__name = name
        self.__type = animal_type
        self.__commands = commands
        self.__birthday = birthday

    def get_info(self):
        return {
            "Name": self.__name,
            "Type": self.__type,
            "Commands": self.__commands,
            "Birthday": self.__birthday
        }

    def add_command(self, command):
        self.__commands.append(command)

# Дочерний класс для домашних животных
class Pet(Animal):
    pass

# Дочерний класс для вьючных животных
class PackAnimal(Animal):
    pass