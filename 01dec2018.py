import data_01dec2018

b = data_01dec2018.data
print("sum = " + str(sum(b)))

list_of_partial_sums = set()
partial_sum = 0
found = False

q = 0
i = 0
while not found:
    data = b[i]
    partial_sum += data

    if partial_sum in list_of_partial_sums:
        print("First repeated partial sum: " + str(partial_sum))
        found = True

    list_of_partial_sums.add(partial_sum)

    i += 1
    if i >= len(b):
        i = 0
        q += 1
        if q % 10 == 0:
            print(q)


