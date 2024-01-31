class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

    def display_info(self):
        return f"Dog's Name: {self.name}, Breed: {self.breed}"

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def meow(self):
        return f"{self.name} says Meow!"

    def display_info(self):
        return f"Cat's Name: {self.name}, Breed: {self.breed}"

def main():
    # Creating a dog and a cat
    my_dog = Dog("Maya", "Pomchi")
    my_cat = Cat("Whiskers", "Siamese")

    while True:
        # User chooses to interact with Dog or Cat
        choice = input("Do you want to interact with a Dog or a Cat? (Enter 'Dog' or 'Cat', or 'exit' to quit): ").lower()
        if choice == 'exit':
            break

        if choice == 'dog':
            action = input("Choose an action for the dog - 'bark' or 'display info': ").lower()
            if action == 'bark':
                print(my_dog.bark())
            elif action == 'display info':
                print(my_dog.display_info())
            else:
                print("Invalid action for dog.")

        elif choice == 'cat':
            action = input("Choose an action for the cat - 'meow' or 'display info': ").lower()
            if action == 'meow':
                print(my_cat.meow())
            elif action == 'display info':
                print(my_cat.display_info())
            else:
                print("Invalid action for cat.")

        else:
            print("Please enter a valid choice ('Dog', 'Cat', or 'exit').")

if __name__ == "__main__":
    main()
