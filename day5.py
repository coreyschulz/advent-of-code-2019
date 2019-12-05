import copy 

inputString = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,6,23,27,1,5,27,31,1,10,31,35,2,10,35,39,1,39,5,43,2,43,6,47,2,9,47,51,1,51,5,55,1,5,55,59,2,10,59,63,1,5,63,67,1,67,10,71,2,6,71,75,2,6,75,79,1,5,79,83,2,6,83,87,2,13,87,91,1,91,6,95,2,13,95,99,1,99,5,103,2,103,10,107,1,9,107,111,1,111,6,115,1,115,2,119,1,119,10,0,99,2,14,0,0"


prog  = [int(i) for i in inputString.split(',')]

def runProgram(origProgram, value1, value2):
    notDone = True
    i = 0
    
    program = copy.deepcopy(origProgram)
    program[1] = value1
    program[2] = value2
    
    while(notDone):
        opcode = program[i]

        if opcode == 1:
            program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
            i += 4
            continue 

        elif opcode == 2:
            program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
            i += 4
            continue

        elif opcode == 3:
            program[program[i+1]] = program[program[i+1]]
            i += 2
            continue

        elif opcode == 4:
            print(program[program[i + 1]])
            i += 2
            continue 

        elif opcode == 99:
            notDone = False
            continue


    return program[0 : 3] 


for r in range(100):
    for c in range(100):
        temp = runProgram(prog, r, c)
        if temp[0] == 19690720:
            print("arg1: ", r, " arg2: ", c)
            print("Key: ", 100 * r + c) 
            break 
