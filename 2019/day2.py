import sys
import math
import copy

# Intercode
def part_one(Intercode, noun=12, verb=2):
    code = copy.deepcopy(Intercode)  # do not modify original
    code[1] = noun
    code[2] = verb
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
    for i in range(0,100):
        noun = i
        for j in range(0,100):
            verb = j
            if part_one(Intercode, noun , verb) == 19690720:
                return 100 * noun + verb
    

    
        
if __name__ == '__main__':
    data = [int(i) for i in input().split(',')]
    print (f"THIS IS NUBER ONE {part_one(data)}")
    print (f"THIS IS NUMBER TWO {part_two(data)}")
    

