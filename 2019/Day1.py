import sys
import math

# sum of masses
def part_one(masses):
    total_fuel = 0
    for mass in masses:
        i = math.floor(mass/3)-2   
        total_fuel = total_fuel + i
    return total_fuel


def part_two(masses):
    total = 0
    for mass in masses:
        total += do_math(mass)
    return total
    
def do_math(mass):
    mass_fuel = 0
    while mass > 0:
        mass = math.floor(mass/3)-2
        if mass < 0:
             break
        mass_fuel += mass
    return mass_fuel

        


if __name__ == '__main__':
    data = [int(l.strip()) for l in sys.stdin.readlines()]
    print ("THIS IS NUBER ONE")
    print(part_one(data))
    print ("THIS IS NUMBER TWO")
    print(part_two(data))

