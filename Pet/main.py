from pet import Pet

def main():
    my_pet = Pet()

    name_input = input("Enter your pet's name: ")
    type_input = input("Enter your pet's type (e.g., Dog, Cat, Bird): ")
    age_input = int(input("Enter your pet's age: "))

    my_pet.set_name(name_input)
    my_pet.set_animal_type(type_input)
    my_pet.set_age(age_input)

    print("\n--- Pet Information ---")
    print(f"Pet Name:    {my_pet.get_name()}")
    print(f"Animal Type: {my_pet.get_animal_type()}")
    print(f"Pet Age:     {my_pet.get_age()} years old")

if __name__ == "__main__":
    main()