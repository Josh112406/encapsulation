from fan import Fan

class TestFan:
    def test():
        fan1 = Fan()

        #fan1 set values
        fan1.set_speed(Fan.FAST)
        fan1.set_radius(10.0)
        fan1.set_color("yellow")
        fan1.set_is_on(True)

        #fan1 properties
        print("fan1 properties:")
        print(f"fan1 Speed: {fan1.get_speed()}")
        print(f"fan1 Radius: {fan1.get_radius()}")
        print(f"fan1 Color: {fan1.get_color()}")
        print(f"fan1 State: {fan1.get_is_on()}")

        fan2 = Fan()
        
        #fan 2 set values
        fan2.set_speed(Fan.MEDIUM)
        fan2.set_radius(5.0)
        fan2.set_color("blue")
        fan2.set_is_on(False)

        #fan2 properties
        print("\nfan2 properties:")
        print(f"fan2 Speed: {fan2.get_speed()}")
        print(f"fan2 Radius: {fan2.get_radius()}")
        print(f"fan2 Color: {fan2.get_color()}")
        print(f"fan2 State: {fan2.get_is_on()}")
        
if __name__ == "__main__":
    TestFan.test()