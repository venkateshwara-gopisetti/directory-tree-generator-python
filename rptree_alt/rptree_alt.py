import os

DIR_PREFIX = '│  '

L_BRACKET = '└──'

T_BRACKET = '├──'

SPACES = '   '

def _generate_tree(prefix, dir):
    output = []
    items = os.listdir(dir)
    items = sorted(items, key=lambda entry: os.path.isfile(entry))
    for index, element in enumerate(items):
        if os.path.isdir(element):
            if index == len(items) - 1:
                entry_prefix = L_BRACKET
            else:
                entry_prefix = T_BRACKET
            output.append(prefix + entry_prefix + element + os.sep)
            output += _add_directory(prefix + DIR_PREFIX, element)
        else:
            if index == len(items) - 1:
                output.append(_add_file(prefix + L_BRACKET, element))
            else:
                output.append(_add_file(prefix + T_BRACKET, element))
    return output

def _add_root(root):
    print(root + os.sep)

def _add_file(prefix, dir):
    return prefix + dir

def _add_directory(prefix, dir):
    return _generate_tree(prefix, dir)

def get_contents(dir):
    _add_root(dir)
    output = _generate_tree('', dir)
    for i in output:
        print(i)

if __name__=="__main__":
    get_contents('.')
