import data_07dec2018
data = data_07dec2018.data

def get_free_element(dictionary):
    firsts = []
    for p in dictionary.keys():
        head = True
        for l in dictionary.values():
            if p in l:
                head = False
                break
        if head:
            firsts.append(p)
    firsts.sort()
    return firsts

def get_first_element(dictionary):
    return get_free_element(dictionary)[0]


# Parsing data
import re
expr = "Step ([A-Z]) must be finished before step ([A-Z]) can begin."
data_parsed = []
for d in data:
    m = re.search(expr, d)
    if len(m.groups()) == 2:
        data_parsed.append([m.group(2), m.group(1)])
    else:
        print("Error! Current line don't match re")
        print(d)

# Create Priorities
priorities = {}                 # key has priority over values
for d in data_parsed:
    if d[1] in priorities:
        priorities[d[1]].append(d[0])
    else:
        priorities[d[1]] = [d[0]]

# Get first letter
sorted = []
removed = []
temp = priorities.copy()
while len(temp) > 0:
    f = get_first_element(temp)
    sorted.append(f)
    for r in temp[f]:
        removed.append(r)
    temp.pop(f)

# Add letters without priority
to_add = []
for r in removed:
    if r not in sorted and r not in to_add:
        to_add.append(r)
to_add.sort()
for a in to_add:
    sorted.append(a)

print(''.join(sorted))


# Parallel Working
priorites_copy = priorities.copy()
for s in sorted:
    if s in priorites_copy:
        priorites_copy[s].append('-')
    else:
        priorites_copy[s] = '-'

max_coworkers = 5
time_for_job = 60
elapsed_time = 0
done = []
on_working = []
free_jobs = get_free_element(priorites_copy)
while len(priorites_copy) > 0 or len(on_working) > 0:
    something_done = False
    string_out = "time " + str(elapsed_time)
    # Remove finished jobs
    for jobs in on_working:
        if jobs[1] <= elapsed_time:
            something_done = True
            done.append(jobs[0])
            string_out += " ended " + jobs[0]
            priorites_copy.pop(jobs[0])
            on_working.pop(on_working.index(jobs))
            free_jobs = get_free_element(priorites_copy)
            for ow in on_working:
                if ow[0] in free_jobs:
                    free_jobs.pop(free_jobs.index(ow[0]))



    # Take new jobs
    while len(on_working) < max_coworkers and len(free_jobs) > 0 :
        something_done = True
        new_job = free_jobs[0]
        on_working.append([new_job, elapsed_time + time_for_job + ord(new_job.lower()) - 96])
        string_out += " token " + new_job + " will end at " + str(elapsed_time + time_for_job + ord(new_job.lower()) - 96)
        free_jobs.pop(0)

    if something_done:
        print(string_out)
    elapsed_time += 1

print(elapsed_time-1)
