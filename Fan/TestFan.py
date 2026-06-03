from fan import Fan

fan1 = Fan(Fan.FAST, 10.0, "yellow", True)
fan2 = Fan(Fan.MEDIUM, 5.0, "blue", False)

#fan1 set values
fan1.set_speed(Fan.FAST)
fan1.set_radius(10.0)
fan1.set_color("yellow")
fan1.set_is_on(True)

#fan1 properties
print(f"fan1 Speed: {fan1.get_speed()}")
print(f"fan1 Radius: {fan1.get_radius()}")
print(f"fan1 Color: {fan1.get_color()}")
print(f"fan1 State: {fan1.get_is_on()}")

#fan 2 set values
fan2.set_speed(Fan.MEDIUM)
fan2.set_radius(5.0)
fan2.set_color("blue")
fan2.set_is_on(False)

#fan2 properties
print(f"fan1 Speed: {fan2.get_speed()}")
print(f"fan1 Radius: {fan2.get_radius()}")
print(f"fan1 Color: {fan2.get_color()}")
print(f"fan1 State: {fan2.get_is_on()}")