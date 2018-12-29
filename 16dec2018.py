import data_16dec2018

# Puzzle input
test_samples = data_16dec2018.test_samples
test_program = data_16dec2018.test_program

# Set of instructions to match
opcode_to_match = {
    'addr',
    'addi',
    'mulr',
    'muli',
    'banr',
    'bani',
    'borr',
    'bori',
    'setr',
    'seti',
    'gtir',
    'gtri',
    'gtrr',
    'eqir',
    'eqri',
    'eqrr'
}

# Instructions set
instructions_set = [None] * len(opcode_to_match)


def execute(name, input_register, operand):
    # Get inputs
    A = operand[0]
    B = operand[1]
    C = operand[2]

    register = list(input_register)

    # Execute instruction
    if name == 'addr':
        register[C] = register[A] + register[B]
    elif name == 'addi':
        register[C] = register[A] + B
    elif name == 'mulr':
        register[C] = register[A] * register[B]
    elif name == 'muli':
        register[C] = register[A] * B
    elif name == 'banr':
        register[C] = register[A] & register[B]
    elif name == 'bani':
        register[C] = register[A] & B
    elif name == 'borr':
        register[C] = register[A] | register[B]
    elif name == 'bori':
        register[C] = register[A] | B
    elif name == 'setr':
        register[C] = register[A]
    elif name == 'seti':
        register[C] = A
    elif name == 'gtir':
        register[C] = int(A > register[B])
    elif name == 'gtri':
        register[C] = int(register[A] > B)
    elif name == 'gtrr':
        register[C] = int(register[A] > register[B])
    elif name == 'eqir':
        register[C] = int(A == register[B])
    elif name == 'eqri':
        register[C] = int(register[A] == B)
    elif name == 'eqrr':
        register[C] = int(register[A] == register[B])
    else:
        raise ValueError('Instruction not found', name)

    # Return updated register
    return tuple(register)


def testSample(sample):
    # Initialize list of possible instructions
    possible_instructions = []

    # Get sample data
    registerBefore = sample['before']
    instruction = sample['instruction']
    registerAfter = sample['after']

    # Test sample
    for k in opcode_to_match:
        # Execute instruction k
        updatedRegister = execute(k, registerBefore, instruction[1:])

        # Check whether it fits the given output register
        if updatedRegister == registerAfter:
            possible_instructions.append(k)

    # Return list of possible instructions matching the sample
    return possible_instructions


##############
### Part 1 ###
##############
idx = 0
number_of_fits = [-1] * len(test_samples)
for sample in test_samples:
    # Count how many instructions fit the sample
    number_of_fits[idx] = len(testSample(sample))
    idx += 1

print('Number of samples with three or more fits: ' +
      str(sum([int(n_fits >= 3) for n_fits in number_of_fits])))

##############
### Part 2 ###
##############
# Match each instruction with its respective opcode
while len(opcode_to_match) > 0:
    for sample in test_samples:
        # List all instructions that fit the sample
        possible_instructions = testSample(sample)

        # If its just one instruction then perform the match
        if len(possible_instructions) == 1:
            # Get instruction
            instruction = possible_instructions[0]

            # Perform the match
            instructions_set[sample['instruction'][0]] = instruction

            # Remove the instruction from the set of those to be matched
            opcode_to_match = opcode_to_match.difference({instruction})

# Run test program
register = (0, 0, 0, 0)
for instruction in test_program:
    opcode = instruction[0]
    operand = instruction[1:]
    register = execute(instructions_set[opcode], register, operand)

print('Value of register 0 at the end of the test program: ' +
      str(register[0]))
