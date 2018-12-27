import numpy as np

import data_08dec2018
data_orig = data_08dec2018.data


class Node:
    def __init__(self, n_child, n_metadata):
        self.child = []
        self.metadata = []
        self.n_child = n_child
        self.n_metadata = n_metadata
        self.score = -1

    def add_child(self, child):
        self.child.append(child)

    def add_metadata(self, metadata):
        self.metadata = metadata

    def get_score(self, node_list):
        if not self.check_node():
            return -1

        # score still computed
        if self.score >= 0:
            return self.score

        # if it has no child
        if self.n_child == 0:
            self.score = np.sum(self.metadata)
            return self.score

        self.score = 0
        for m in self.metadata:
            if 0 < m <= self.n_child:
                self.score += node_list[self.child[m-1]].get_score(node_list)
        return self.score

    def metadata_ok(self):
        return len(self.metadata) == self.n_metadata

    def child_ok(self):
        return len(self.child) == self.n_child

    def check_node(self):
        return len(self.metadata) == self.n_metadata and len(self.child) == self.n_child


if __name__ == '__main__':
    nodes = []
    unfinished = []
    data = data_orig.copy()
    while len(data) > 0:
        current_node = Node(data[0], data[1])
        data = data[2:]
        unfinished.append(len(nodes))
        nodes.append(current_node)
        idx = unfinished[-1]
        while nodes[idx].child_ok():
            nodes[idx].add_metadata(data[:nodes[idx].n_metadata])
            data = data[nodes[idx].n_metadata:]
            unfinished.pop()
            if len(unfinished) > 0:
                nodes[unfinished[-1]].add_child(idx)
                idx = unfinished[-1]
            else:
                break

    print(len(nodes))

    # Sum metadata
    sum_metadata = 0
    for n in nodes:
        sum_metadata += np.sum(n.metadata)

    print("sum of metadata: " + str(sum_metadata))

    print("tree score is: " + str(nodes[0].get_score(nodes)))





