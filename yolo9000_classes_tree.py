from anytree import Node, RenderTree
from anytree.exporter import DotExporter

def __read_from_file(file_name):
    try:
        with open(file_name,'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except (OSError, IOError) as e:
        print(e)

def __write_to_file(to_write, file_name, write_mode="w"):
    try:
        with open(file_name,write_mode, encoding='utf-8') as file:
            for item in to_write:
                file.write(item.__str__())
                file.write("\n")
    except (OSError, IOError) as e:
        print(e)



names_list = __read_from_file("9k.names").split("\n")
temp_list = __read_from_file("9k.tree").split()
tree_list = []
for i, c in enumerate(temp_list):
    if(i%2 !=0):
        tree_list.append(c)

root = Node("root")
nodes = []
for t, n in zip(tree_list, names_list):
    if(int(t) == -1):
        nodes.append(Node(n,parent=root))
    else:
        nodes.append(Node(n,parent=nodes[int(t)]))

to_save = []
for pre, fill, node in RenderTree(root):
    # print("%s%s" % (pre, node.name))
    to_save.append("%s%s" % (pre, node.name))


__write_to_file(to_save,"nodes.txt")

# DotExporter(udo).to_picture("udo.png")

