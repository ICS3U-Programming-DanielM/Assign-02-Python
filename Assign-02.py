# #!/usr/bin/env python3
# Created by: Daniel Momoh
# Created on: Oct 1, 2022
# Python3 program to find the Surface Area and Volume of Hexagonal Prism.
import math
 
 
def main():
    # input
    print("We are calculating the Surface Area and")
    print("volume of a Hexagonal Prism")
    base = int(input("Enter the base (cm) : "))
    height = int(input("Enter the height (cm): "))
 
    # process1
    SurfaceArea = 6 * base * height + 3 * math.sqrt(3) * base * base
    Volume = 3 * math.sqrt(3) * base * base * height / 2
 
    # output
    print("")
    print("SurfaceArea = {:,.2f} cm^2".format(SurfaceArea))
    print("Volume =, {:,.2f} cm^3".format(Volume))
 
 
if __name__ == "__main__":
    main()