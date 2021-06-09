import os
import sys
import math


def main():
    print("Enter values for point A")
    x1, y1, z1 = input("Enter values x1, y1 and z1 separated by a comma and space: ").split(", ")

    print("Enter values for point B")
    x2, y2, z2 = input("Enter values x2, y2 and z2 separated by a comma and space: ").split(", ")

    x1 = float(x1)
    y1 = float(y1)
    z1 = float(z1)

    x2 = float(x2)
    y2 = float(y2)
    z2 = float(z2)

    x = (x1 - x2) ** 2
    y = (y1 - y2) ** 2
    z = (z1 - z2) ** 2

    d = math.sqrt(x + y + z)

    print(f"a. The distance between point A{x1, y1, z1} and B{x2, y2, z2} is: {d}")

    # Distance between points and origin
    x = (0 - x1) ** 2
    y = (0 - y1) ** 2
    z = (0 - z1) ** 2

    d_a = math.sqrt(x + y + z)
    print(f"b.1 . Distance between point A{x1, y1, z1} and origin(0, 0, 0) is: {d_a}")

    x = (0 - x2) ** 2
    y = (0 - y2) ** 2
    z = (0 - z2) ** 2

    d_b = math.sqrt(x + y + z)
    print(f"b.2 . Distance between point B{x2, y2, z2} and origin(0, 0, 0) is: {d_b}")

    # Use cosine rule to compute internal angles
    a = d_a
    b = d_b
    c = d
    cos_d = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
    angle_d = math.degrees(math.acos(cos_d))
    print(f"Angle D, at origin, (in degrees) is: {angle_d}")

    a = d
    b = d_b
    c = d_a
    cos_d = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
    angle_da = math.degrees(math.acos(cos_d))
    print(f"Angle A (in degrees) is: {angle_da}")

    a = d
    b = d_a
    c = d_b
    cos_d = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
    angle_db = math.degrees(math.acos(cos_d))
    print(f"Angle B (in degrees) is: {angle_db}")

    print(f"Check if the three angles add up to 180 degrees: "
          f"{angle_d + angle_da + angle_db == 180.0}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
