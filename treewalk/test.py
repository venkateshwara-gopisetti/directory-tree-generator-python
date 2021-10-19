import os

tree_list = []

for root, dirs, files in os.walk(".", topdown=False):
   # for name in files:
   #    print(os.path.join(root, name))
   # for name in dirs:
   #    print(os.path.join(root, name))

   for name in files:
      tree_list.append([os.path.join(root, name), False])
   for name in dirs:
      tree_list.append([os.path.join(root, name), True])

tree_list.sort()
for element in tree_list:
   print(element)