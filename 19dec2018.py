from data_19dec2018 import ip_reg, program


# Implement instructions set
def execute_instruction(name, input_register, operand):
    # Get inputs
    A = operand[0]
    B = operand[1]
    C = operand[2]

    # Create a copy of the input registers
    reg = list(input_register)

    # Execute instruction
    if name == 'addr':
        reg[C] = reg[A] + reg[B]
    elif name == 'addi':
        reg[C] = reg[A] + B
    elif name == 'mulr':
        reg[C] = reg[A] * reg[B]
    elif name == 'muli':
        reg[C] = reg[A] * B
    elif name == 'banr':
        reg[C] = reg[A] & reg[B]
    elif name == 'bani':
        reg[C] = reg[A] & B
    elif name == 'borr':
        reg[C] = reg[A] | reg[B]
    elif name == 'bori':
        reg[C] = reg[A] | B
    elif name == 'setr':
        reg[C] = reg[A]
    elif name == 'seti':
        reg[C] = A
    elif name == 'gtir':
        reg[C] = int(A > reg[B])
    elif name == 'gtri':
        reg[C] = int(reg[A] > B)
    elif name == 'gtrr':
        reg[C] = int(reg[A] > reg[B])
    elif name == 'eqir':
        reg[C] = int(A == reg[B])
    elif name == 'eqri':
        reg[C] = int(reg[A] == B)
    elif name == 'eqrr':
        reg[C] = int(reg[A] == reg[B])
    else:
        raise ValueError('Instruction not found', name)

    # Increment the instruction pointer
    reg[ip_reg] += 1

    # Return updated register
    return tuple(reg)


def run_program(reg):
    # Run program
    k = 0
    while True:
        # Set instruction pointer
        ip = reg[ip_reg]

        # Try to read the next instruction
        try:
            next_instruction = program[ip]
        except IndexError:
            return reg

        # Execute the instruction
        reg = execute_instruction(
            next_instruction[0], reg, next_instruction[1:]
        )

        if k == 0:
            print(ip, next_instruction, reg)
        k = (k + 1) % 1000003


######################################################################
### SMART WAY
######################################################################

##############
### Part 1 ###
##############
import numpy as np
n = 876
numbers = np.arange(1, n+1)
is_divisor = (n % numbers) == 0
divisors = numbers[is_divisor]
print('The answer of part 1 is: ' + str(sum(divisors)))

##############
### Part 2 ###
##############
n = 10551276
numbers = np.arange(1, n+1)
is_divisor = (n % numbers) == 0
divisors = numbers[is_divisor]
print('The answer of part 2 is: ' + str(sum(divisors)))


######################################################################
### DUMB WAY
######################################################################
key = input('\nPress c and enter to exit or hit enter to run the dumb solution\n')
if key == 'c':
    raise KeyboardInterrupt

##############
### Part 1 ###
##############

# Initialize registers and run program
register = (0, 0, 0, 0, 0, 0)
register = run_program(register)
print('')
print('Program 1 halted!')
print('Registers:\t' + str(register))
print('IP:\t' + str(register[ip_reg]))
print('')
print('')

##############
### Part 2 ###
##############

# Initialize registers and run program
register = (1, 0, 0, 0, 0, 0)
run_program(register)
print('')
print('Program 2 halted!')
print('Registers:\t' + str(register))
print('IP:\t' + str(register[ip_reg]))
print('')
print('')
