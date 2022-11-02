# 1

def hello():
    print("Hello World!")


hello()

# 2


def pack(a, b, c):
    return [a, b, c]


print(pack("a", "b", "c"))

# 3


def eat_lunch(food):
    if len(food) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(food)):
            if i == 0:
                print(f"First I eat {food[0]}")
            else:
                print(f"Next I eat {food[i]}")


eat_lunch(["burger", "tacos", "noodles", "fruits"])
