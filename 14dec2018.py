import data_14dec2018
from math import floor

data = data_14dec2018.data


# Given an integer returns a list containing its digits in the same order
def int2digits(n):
    digits = []
    while n > 0:
        digits.insert(0, n % 10)
        n = floor(n / 10)

    return digits


# Given the current recipes returns the updated scores and the new recipes
def combine_recipes(scores, current_recipes):
    # Compute score associated with the current recipes
    sum_recipes_scores = sum([scores[recipe] for recipe in current_recipes])

    # Add newly created recipes
    new_scores = scores + int2digits(sum_recipes_scores)

    # Compute new elves recipes
    new_current_recipes = []
    for recipe in current_recipes:
        new_recipe = (recipe + scores[recipe] + 1) % len(new_scores)
        new_current_recipes.append(new_recipe)

    return new_scores, new_current_recipes


# Number of elves
n_elves = 2

# Initial recipe for each elf
current_recipes = list(range(0, n_elves))

# Initial scores from data
scores = int2digits(37)

# Output info
length = 10
start_points = [9, 5, 18, 2018, data]
for start_point in start_points:
    end_point = start_point + length

    # Run game for n_turns
    while len(scores) < end_point:
        #print(current_recipes, [scores[recipe] for recipe in current_recipes])

        # Combine current recipes
        scores, current_recipes = combine_recipes(scores, current_recipes)
        if len(scores) % 1000 == 0:
            print('arrived to ' + str(len(scores)))

    print(''.join([str(d) for d in scores]))


    print('Initial point ' + str(start_point) + ' Scores = ' + ''.join([str(d) for d in scores[start_point:end_point]]))
