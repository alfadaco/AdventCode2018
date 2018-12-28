import data_12dec2018
import re
from matplotlib import pyplot as plt

initial_state = data_12dec2018.initial_state
rules = data_12dec2018.rules

n_generation = 120


def parse_syntax(phrase):
    parsed = []
    for c in phrase:
        if c == '#':
            parsed.append(1)
        elif c == '.':
            parsed.append(0)
    return parsed


def gen_syntax(phrase):
    parsed = ''
    for c in phrase:
        if c == 1:
            parsed += '#'
        elif c == 0:
            parsed += '.'
    return parsed


def check_presence(old_plants, r, pot_idx):
    if (r == 0 and pot_idx not in old_plants) or \
            (r == 1 and pot_idx in old_plants):
        return True
    else:
        return False


def check_rule(old_plants, rules):
    satisfiyng_rule_idx = set()
    rule_halflength = 2

    for central_pot in old_plants:
        for p in range(central_pot - 2*rule_halflength - 1,
                       central_pot + 2*rule_halflength + 2):
            if p in satisfiyng_rule_idx:
                continue

            for r in rules:
                condition = True
                for i in range(0, 2*rule_halflength + 1):
                    condition = condition and check_presence(old_plants, r[i], p - rule_halflength + i)
                    if not condition:
                        break
                if condition:
                    satisfiyng_rule_idx.add(p)
                    break
    return satisfiyng_rule_idx


if __name__ == '__main__':

    # Define pots initial state
    pot_status = parse_syntax(initial_state)
    plant_index = set()
    for p in range(0, len(pot_status)):
        if pot_status[p] == 1:
            plant_index.add(p)

    # Plot initial state
    plt.figure(1)
    plt.clf()
    plt.grid()
    plt.xlabel('Plants ids')
    plt.ylabel('Generation')
    plt.title('Puzzle 12 dec 2018')
    plt.gca().invert_yaxis()
    plt.plot(list(plant_index), [0]*len(plant_index), 'o')
    plt.show(block=False)

    # Define growing pattern
    grow_rules = []
    destroy_rules = []
    pattern = '([.#]{5})\ \=\>\ ([.#])'
    for r in rules:
        m = re.match(pattern, r)
        if m.group(2) == '#':
            grow_rules.append(parse_syntax(m.group(1)))
        elif m.group(2) == '.':
            destroy_rules.append(parse_syntax(m.group(1)))

    # Growing up
    max_time = n_generation
    print('Epoch 0')
    history = [list(plant_index)]
    # print(gen_syntax(pot_status))
    score_history = [sum(list(plant_index))]
    for t in range(1, max_time + 1):
        # Check growing pattern
        new_plant_index = check_rule(plant_index, grow_rules)

        if new_plant_index == plant_index:
            print('equal')
        plant_index = new_plant_index
        history.append(list(plant_index))
        
        score_history.append(sum(list(plant_index)))        
        
        # Save stats at iteration 102
        if t == 102:
            score_at_102 = sum(list(plant_index))
            number_of_plants_at_102 = len(plant_index)

        # Print stats
        if t % 1 == 0:
            plt.plot(list(plant_index), [t]*len(plant_index), 'o')
            plt.show(block=False)

            score = sum(list(plant_index))
            print('Epoch ' + str(t) +
                  ' len=' + str(len(plant_index)) +
                  ' score=' + str(score))
            #print(plant_index)

    # Newline
    print(' ')

    # Print last epoch
    score = sum(list(plant_index))
    print('Epoch ' + str(t) +
          ' len=' + str(len(plant_index)) +
          ' score=' + str(score))

    # Fast forward to epoch...
    n_generation = 50*1000*1000*1000
    score = score_at_102 + (n_generation-102)*number_of_plants_at_102
    print('Epoch ' + str(n_generation) +
          ' len=' + str(len(plant_index)) +
          ' score=' + str(score))

    # Plot score evolution
    plt.figure(2)
    plt.clf()
    plt.grid()
    plt.xlabel('Generation')
    plt.ylabel('Score')
    plt.title('Puzzle 12 dec 2018')
    plt.plot(range(0, max_time + 1), score_history)
    plt.show(block=False)
    
# Score is given as
# s = n_generation*46 + 6
# why???
n_generation = 50*1000*1000*1000
score = n_generation*46 + 6
print(str(n_generation) + ' score = ' + str(score))
