# !/usr/bin/env python3

# Created by: Ahmad El-khawaldeh
# Created on: Dec 2020
# This program calculates the area of tringle


print(" calculate the area of a trapzoid ")

def calculate_area_of_trapziod(Base1_string, Base2_string, Height_string):

    Base1 = int(Base1_string)
    Base2 = int(Base2_string)
    Height = int(Height_string)
    area = 0.5 * (Base1 + Base2) * Height
    print("The area of the trapezoid is {0} cm² ".format(area)) 
  
def main():
    try:
        Base1_string = input('Enter the base1(cm): ')
        Base2_string = input('Enter Base2(cm): ')
        Height_string = input('Enter the height(cm): ')
  

        calculate_area_of_trapziod(Base1_string, Base2_string, Height_string)

    except Exception:
        print("This is not a number")

if __name__ == "__main__":
    main()