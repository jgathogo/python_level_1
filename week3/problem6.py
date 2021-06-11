import os
import sys
import math

"""
Notes:
- Excellent job! I'm glad that you figured out the correct equations to compute
the internal angles. I see that this has also forced you to read up on 
Python math library. This is exactly the kind of activity by which someone 
grows, not just attending class but solving problems in increasing difficulty. 
- Remember to run 'clean' often to make sure that the correct number of spaces
between functions etc. This habit will come in handy when we start writing classes
since quite often we want to fold code and make sure we have enough space
between methods.
-  I see you have 'reused' x, y, and z. Try and avoid that. It's innocent acts like
these that lead to very hard to track down bugs.
- I hope it's also becoming apparent how linear code quickly begins to clutter your module.
Once we get into functions our code can get a whole lot cleaner. But for now this 
is perfectly OK because we are concentrating on other constructs.
- [DONE] Trivial point: in terms of presentation of floating point numbers, one can use
round() to clean things up. Typically, 4 decimal places is sufficient.
- Read the scoring notes in scores.txt 
"""


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

    # If we strive that our code only always ever refer to a and b
    # then we can never be confused.
    # This is the power of good variable naming to be in line with the
    # domain application. I call this 'avoiding logical tension'.
    # Try and imagine how mind-scrambling it gets when you start dealing
    # with an application spanning 5 packages each with 10 modules with
    # each module extending to over 2000 lines of code (LOC).
    # Variable names matter a lot! ;-)
    # o = (0, 0, 0)
    # a = (x1, y1, z1)
    # b = (x2, y2, z2)
    # d_ab = round(math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)), 4)
    # d_ao = round(math.sqrt((a[0]-o[0])**2 + (a[1]-o[1])**2 + (a[2]-o[2])**2)), 4)
    # d_bo = round(math.sqrt((b[0]-o[0])**2 + (b[1]-o[1])**2 + (b[2]-o[2])**2)), 4)
    # angle_o = math.acos(math.degrees((d_ao ** 2 + d_bo ** 2 - d_ab ** 2) / (2*d_ao * d_bo)))
    # ...
    d_ab = round(math.sqrt(x + y + z), 4)

    print(f"a. The distance between point A{x1, y1, z1} and B{x2, y2, z2} is: {d_ab}")

    # Distance between points and origin
    m = (0 - x1) ** 2
    n = (0 - y1) ** 2
    o = (0 - z1) ** 2

    d_ao = round(math.sqrt(m + n + o), 4)
    print(f"b.1 . Distance between point A{x1, y1, z1} and origin(0, 0, 0) is: {d_ao}")

    r = (0 - x2) ** 2
    s = (0 - y2) ** 2
    t = (0 - z2) ** 2

    d_bo = round(math.sqrt(r + s + t), 4)
    print(f"b.2 . Distance between point B{x2, y2, z2} and origin(0, 0, 0) is: {d_bo}")

    # Use cosine rule to compute internal angles
    a = d_ao
    b = d_bo
    c = d_ab
    cos_d = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
    angle_d = round(math.degrees(math.acos(cos_d)), 4)
    print(f"Angle D, at origin, (in degrees) is: {angle_d}")

    a = d_ab
    b = d_bo
    c = d_ao
    cos_d = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
    angle_da = round(math.degrees(math.acos(cos_d)), 4)
    print(f"Angle A (in degrees) is: {angle_da}")

    a = d_ab
    b = d_ao
    c = d_bo
    cos_d = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
    angle_db = round(math.degrees(math.acos(cos_d)), 4)
    print(f"Angle B (in degrees) is: {angle_db}")

    print(f"Check if the three angles add up to 180 degrees: "
          f"{angle_d + angle_da + angle_db == 180.0}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
