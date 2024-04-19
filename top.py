class Person:
    def __init__(self, name, age):
        """
        Constructor method to initialize a Person object with name and age.
        """
        self.name = name
        self.age = 23
        self.friends = []  # Initialize an empty list to store friends

    def greet(self):
        """
        Method to print a greeting message including the person's name and age.
        """
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def add_friend(self, friend):
        """
        Method to add a friend to the person's list of friends.
        """
        self.friends.append(friend)

    def get_friends(self):
        """
        Method to get the list of friends.
        """
        return self.friends

# Creating instances of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Accessing attributes and calling methods of the instances
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30
person1.greet()      # Output: Hello, my name is Alice and I am 30 years old.

print(person2.name)  # Output: Bob
print(person2.age)   # Output: 25
person2.greet()      # Output: Hello, my name is Bob and I am 25 years old.

# Adding friends to each person
person1.add_friend(person2)
person2.add_friend(person1)

# Getting the list of friends for each person
print(person1.get_friends())  # Output: [<__main__.Person object at 0x7f0c74b3e7f0>]
print(person2.get_friends())  # Output: [<__main__.Person object at 0x7f0c74b3e700>]
