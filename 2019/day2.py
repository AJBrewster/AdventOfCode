import sys
import math

# Intercode
def part_one(code):
    code[1] = 12
    code[2] = 2
    for i in range(0 ,len(code), 4):
        p_one = code[i+1] 
        p_two = code[i+2]
        replace = code[i+3]  
        if code[i] == 99:
            break
        if code[i] == 1:
            #do adding 
            code[replace] = code[p_one] + code[p_two] 
        if code[i] == 2:
            #do mutiplying 
            code[replace] = code[p_one] * code[p_two]
    return code[0]


def part_two(Intercode):
    return Intercode
    
        
if __name__ == '__main__':
    data = [int(i) for i in input().split(',')]
    print ("THIS IS NUBER ONE")
    print(part_one(data))
    print ("THIS IS NUMBER TWO")
    print(part_two(data))

