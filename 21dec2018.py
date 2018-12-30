from data_21dec2018 import ip_reg, program


# Implement instructions set
def execute_instruction(name, input_register, operand):
    # Get inputs
    A = operand[0]
    B = operand[1]
    C = operand[2]

    # Create a copy of the input registers
    reg = input_register.copy()

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
    return reg


##############
### Part 1 ###
##############

# Initialize registers
register = [0, 0, 0, 0, 0, 0]

# Run program
k = 0
while register[ip_reg] < len(program):
    # Set instruction pointer
    ip = register[ip_reg]

    # Load the next instruction
    next_instruction = program[ip]

    # Print instruction that reads from register 0
    if ip == 28:
        register[0] = register[2]

    # Execute the instruction
    register = execute_instruction(
        next_instruction[0], register, next_instruction[1:]
    )

    # Update instruction counter
    k += 1

# Print output
print('\nPart 1')
print('Value of register[0]: ' + str(register[0]))
print('\n')


##############
### Part 2 ###
##############

# Initialize registers
register = [0, 0, 0, 0, 0, 0]

# Run program
k = 0
numbers = set()
last_number = 0
while register[ip_reg] < len(program):
    # Set instruction pointer
    ip = register[ip_reg]

    # Load the next instruction
    next_instruction = program[ip]

    # Print instruction that reads from register 0
    if ip == 28:
        if register[2] in numbers:
            break
        else:
            last_number = register[2]
            numbers.add(register[2])

    # Execute the instruction
    register = execute_instruction(
        next_instruction[0], register, next_instruction[1:]
    )

    # Update instruction counter
    k += 1

# Print output
print('\nPart 2')
print('Value of register[0]: ' + str(last_number))
print('\n')
