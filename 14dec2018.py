import data_14dec2018
from math import floor

data = data_14dec2018.data


# Given an integer returns a list containing its digits in the same order
def int2digits(n):
    if n == 0:
        return [0]

    digits = []
    while n > 0:
        digits.insert(0, n % 10)
        n = floor(n / 10)

    return digits


# Given the current recipes returns the updated scores and the new recipes
def combine_recipes(scores, current_recipes, current_length):
    # Compute score associated with the current recipes
    sum_recipes_scores = sum([scores[recipe] for recipe in current_recipes])

    # Add newly created recipes
    append_scores = int2digits(sum_recipes_scores)
    start = current_length
    end = current_length + len(append_scores)
    new_scores = scores
    new_scores[start:end] = append_scores
    new_current_length = current_length + len(append_scores)

    # Compute new elves recipes
    new_current_recipes = []
    for recipe in current_recipes:
        new_recipe = (recipe + new_scores[recipe] + 1) % new_current_length
        new_current_recipes.append(new_recipe)

    return new_scores, new_current_recipes, new_current_length


# Number of elves
n_elves = 2

# Output info
start_point = data
length = 10
end_point = start_point + length

# Initial recipe for each elf
current_recipes = list(range(0, n_elves))

# Initial scores from data
scores = int2digits(37) + ([None] * (start_point + length))
current_length = 2

##############
### Part 1 ###
##############

# Run game for n_turns
while current_length < end_point:
    # Combine current recipes
    scores, current_recipes, current_length = combine_recipes(scores,
                                                              current_recipes,
                                                              current_length)

# Print output for part 1
print('Scores = ' + ''.join([str(d) for d in scores[start_point:end_point]]))

##############
### Part 2 ###
##############

# String to match
match = data
match = int2digits(match)
nn = len(match)

# Re-initialize
preallocate = int(2.5e7)
current_recipes = list(range(0, n_elves))
current_length = 2
scores = [None] * (preallocate + current_length)
scores[0:current_length] = int2digits(37)

# Run game until match appears
while current_length < preallocate:
    # Combine current recipes
    scores, current_recipes, current_length = combine_recipes(scores,
                                                              current_recipes,
                                                              current_length)
    if current_length >= nn:
        if scores[current_length-nn:current_length] == match:
            found = True
            print('Matched after ' + str(current_length-nn) + ' recipes')
            break
        elif scores[current_length-nn-1:current_length-1] == match:
            found = True
            print('Matched after ' + str(current_length-nn-1) + ' recipes')
            break
        else:
            found = False
            continue

if not found:
    print('Not found...')
