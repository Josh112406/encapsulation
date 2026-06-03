from car import Car
def main():

    my_car = Car(2026, "Toyota")
    
    #test acceleration
    for i in range(5):
        my_car.accelerate()
        print("Accelerating...")
        print(f"Current speed: {my_car.get_speed()} mph")
    print("\nTesting Braking:")

    #test breaking
    for i in range(5):
        my_car.brake()
        print(f"Braking...")
        print(f"Current speed: {my_car.get_speed()} mph")

if __name__ == "__main__":
    main()