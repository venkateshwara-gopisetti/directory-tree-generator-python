# -*- coding: utf-8 -*-
"""
@author:Venkateshwara Gopisetti
"""

from os import listdir as _os_listdir
from os import sep as _os_sep
from os.path import join as _os_path_join
from os.path import isfile as _os_is_file
from os.path import isdir as _os_is_dir

DIR_PREFIX = '│  '

L_BRACKET = '└──'

T_BRACKET = '├──'

SPACES = '   '

class AltRptree:
    def _generate_tree(self, prefix, directory):
        output = []
        items = _os_listdir(directory)
        items = sorted(items, key=lambda entry: _os_is_file(_os_path_join(directory,entry)))
        for index, element in enumerate(items):
            if _os_is_dir(_os_path_join(directory, element)):
                if index == len(items) - 1:
                    entry_prefix = L_BRACKET
                    next_prefix = SPACES
                else:
                    entry_prefix = T_BRACKET
                    next_prefix = DIR_PREFIX
                output.append(prefix + entry_prefix + element + _os_sep)
                output += self._add_directory(prefix + next_prefix, _os_path_join(directory, element))
            else:
                if index == len(items) - 1:
                    output.append(self._add_file(prefix + L_BRACKET, element))
                    output.append(prefix + SPACES)
                else:
                    output.append(self._add_file(prefix + T_BRACKET, element))
        return output

    def _add_root(self, root):
        print(root + _os_sep)

    def _add_file(self, prefix, directory):
        return prefix + directory

    def _add_directory(self, prefix, directory):
        return self._generate_tree(prefix, directory)

    def get_contents(self, directory):
        self._add_root(root=directory)
        output = self._generate_tree('', directory)
        for i in output:
            print(i)

if __name__=="__main__":
    tree = AltRptree()
    tree.get_contents('.')
