""" """

import os

DIR_PREFIX = '│   '

L_BRACKET = '└───'

T_BRACKET = '├───'

SPACES = '   '

CONNECTOR = lambda x: DIR_PREFIX * (x)

class reversor:
    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, other):
        return other.obj == self.obj

    def __lt__(self, other):
        return other.obj < self.obj

def _sort_tree(tree):
	tree.sort()
	dirs = [x for x in tree if x[2]]

	output = []
	leftover = []

	for dire in dirs:
		output.append(dire)
		flags = [0]*len(tree)
		for idx, branch in enumerate(tree):
			if branch[2]:
				flags[idx] = 1
			elif branch[0][:-1] == dire[0]:
				output.append(branch)
				flags[idx] = 1
		tree = [tree[x] for x in range(len(tree)) if flags[x]==0]
	
	return output + tree

def _walk_directory(root):
	tree_list = []
	for root, dirs, files in os.walk(root, topdown=True):
		walk_list = []
		for name in dirs:
			walk_list.append([root, name, len(root.split('\\')), True])
		for name in files:
			walk_list.append([root, name, len(root.split('\\')), False])
		tree_list += walk_list
	return tree_list


import sys

if __name__=="__main__":
	dir = sys.argv[1]
	print(_walk_directory(dir).sort())