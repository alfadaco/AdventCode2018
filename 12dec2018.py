import data_12dec2018
import re

initial_state = data_12dec2018.initial_state
rules = data_12dec2018.rules

#n_generation = 20
n_generation = 50*1000*1000*1000


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

    for p in range(min(old_plants) - rule_halflength, max(old_plants) + rule_halflength + 1):
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
    print('epoch 0')
    # print(gen_syntax(pot_status))
    for t in range(1, max_time + 1):
        # Check growing pattern
        new_plant_index = check_rule(plant_index, grow_rules)
        removed_plant_index = check_rule(plant_index, destroy_rules)

        plant_index.difference_update(removed_plant_index)
        plant_index = plant_index.union(new_plant_index)

        if t%1000 == 0:
            print('epoch ' + str(t))
            # print(gen_syntax(pot_status))

    score = 0
    for p in plant_index:
        score += p
    print('score = ' + str(score))
