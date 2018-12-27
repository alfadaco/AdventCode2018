import data_02dec2018

data = data_02dec2018.data

count_2 = 0
count_3 = 0

for box_id in data:
    letter_dict = {}
    for letter in box_id:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    count_dict = set()
    for letter in letter_dict:
        count_dict.add(letter_dict[letter])

    if 2 in count_dict:
        count_2 += 1

    if 3 in count_dict:
        count_3 += 1

print(str(count_2) + " * " + str(count_3) + " = " + str(count_2*count_3))

for box_id_1 in data:
    for box_id_2 in data:
        if len(box_id_1) != len(box_id_2):
            continue
        if id(box_id_1) == id(box_id_2):
            continue

        common_string =""
        hamming_dist = 0
        for i in range(0, len(box_id_1)):
            if box_id_1[i] != box_id_2[i]:
                hamming_dist += 1
            else:
                common_string += box_id_1[i]

        if hamming_dist == 1:
            print(box_id_1 + " and " + box_id_2 + " has hamming distance = 1")
            print("string common part is " + common_string)

