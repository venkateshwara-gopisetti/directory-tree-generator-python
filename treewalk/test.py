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
			path = os.path.join(root, name)
			walk_list.append([path.split('\\'), len(path.split('\\'))-1, True])
		for name in files:
			path = os.path.join(root, name)
			walk_list.append([path.split('\\'), len(path.split('\\'))-1, False])
		max_q = len(walk_list)-1
		walk_list = [x + [max_q] for x in walk_list]
		tree_list += walk_list
	return tree_list

def _generate_tree(root):

	tree_list = _walk_directory(root)
	tree_list = _sort_tree(tree_list)
	counter = {root.strip('\\'):0}

	print(tree_list)
	for i in tree_list:
		item, level, is_dir, max_q = i
		counter_key = ''.join(item[:-1])
		if counter_key not in counter.keys():
			counter[counter_key] = 0
		is_last = counter[counter_key] == max_q
		# print(CONNECTOR(level))

		bracket = L_BRACKET if is_last else T_BRACKET
		print(
			CONNECTOR(level-1)
			+ bracket
			+ item[-1]
			+ (os.sep if is_dir else '')
		)
		# print(i)
		counter[counter_key] += 1

import sys

if __name__=="__main__":
	dir = sys.argv[1]
	_generate_tree(dir)