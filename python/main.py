from animal import Animal, Pet, PackAnimal
from counter import Counter

class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals(self):
        print("\nList of all animals:")
        for animal in self.animals:
            info = animal.get_info()
            print(f"Name: {info['Name']}, Type: {info['Type']}, Birthday: {info['Birthday']}")

    def show_commands(self, name):
        for animal in self.animals:
            if animal.get_info()["Name"] == name:
                print(f"\nCommands for {name}: {animal.get_info()['Commands']}")
                return
        print(f"\nAnimal {name} not found!")

    def teach_command(self, name, command):
        for animal in self.animals:
            if animal.get_info()["Name"] == name:
                animal.add_command(command)
                print(f"\n{command} has been taught to {name}.")
                return
        print(f"\nAnimal {name} not found!")

def main():
    registry = AnimalRegistry()

    try:
        with Counter() as counter:
            while True:
                print("\n--- Animal Registry ---")
                print("1. Add a new animal")
                print("2. List all animals")
                print("3. Show commands for an animal")
                print("4. Teach a new command")
                print("5. Exit")
                choice = input("Choose an option: ")

                if choice == "1":
                    name = input("Enter animal's name: ")
                    animal_type = input("Enter animal's type: ")
                    commands = input("Enter commands (comma-separated): ").split(", ")
                    birthday = input("Enter birthday (YYYY-MM-DD): ")
                    if animal_type in ["Dog", "Cat", "Hamster"]:
                        animal = Pet(name, animal_type, commands, birthday)
                    else:
                        animal = PackAnimal(name, animal_type, commands, birthday)
                    registry.add_animal(animal)
                    counter.add()
                    print(f"{name} has been added!")

                elif choice == "2":
                    registry.list_animals()

                elif choice == "3":
                    name = input("Enter animal's name: ")
                    registry.show_commands(name)

                elif choice == "4":
                    name = input("Enter animal's name: ")
                    command = input("Enter the new command: ")
                    registry.teach_command(name, command)

                elif choice == "5":
                    print(f"\nTotal animals added: {counter.get_count()}")
                    break

                else:
                    print("Invalid option. Please try again.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()