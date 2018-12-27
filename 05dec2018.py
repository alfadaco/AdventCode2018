import data_05dec2018

def react_polymer(original_polymer):
    reacted_polymer = original_polymer
    i = 0
    while i < len(reacted_polymer) - 1:
        if reacted_polymer[i].isupper() and reacted_polymer[i+1].islower() and reacted_polymer[i+1].upper() == reacted_polymer[i]:
            reacted_polymer = reacted_polymer.replace(reacted_polymer[i:i+2], '')
            if i > 0:
                i -= 1
        elif reacted_polymer[i].islower() and reacted_polymer[i+1].isupper() and reacted_polymer[i+1].lower() == reacted_polymer[i]:
            reacted_polymer = reacted_polymer.replace(reacted_polymer[i:i + 2], '')
            if i > 0:
                i -= 1
        else:
            i += 1
    return reacted_polymer


if __name__ == '__main__':
    data = data_05dec2018.data
    reacted_polymer = react_polymer(data)
    print('fully reacted polymer:')
    print(reacted_polymer)
    print(len(reacted_polymer))

    map = {}
    for i in range(0, len(data)):
        if data[i].upper() not in map:
            new_data = data.replace(data[i].upper(), '')
            new_data = new_data.replace(data[i].lower(), '')
            new_reaction = react_polymer(new_data)
            map[data[i].upper()] = new_reaction

    for element in map:
        print(element + ' len = ' + str(len(map[element])))



