# Answer 1815525
import sys


class Tree(object):
    "Generic tree node."

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.filebytes = 0

    def __repr__(self):
        return self.name

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

    def fetch_child(self, name):
        for node in self.children:
            if node.name == name:
                return node
        # Should not happen cause input is always kosher
        raise SystemExit("Could not find directory")

    def update_size(self, size):
        self.filebytes += size
        parent = self.parent
        if parent:
            parent.update_size(size)

    def display_tree(self):
        self.show_all_nodes(0)

    def show_all_nodes(self, cnt):
        print(f'{" " * cnt}{self.name}: {self.filebytes}')
        cnt += 3
        for node in self.children:
            node.show_all_nodes(cnt)

    def find_nodes_by_size(self, size):
        results = []
        self.filter_nodes_by_size(results, size)
        return results

    def filter_nodes_by_size(self, results, size):
        if self.filebytes >= size:
            results.append(self)
        for node in self.children:
            node.filter_nodes_by_size(results, size)


with open(sys.argv[1], "r", encoding="ascii") as fl:
    master_tree = Tree("root")
    current_tree = master_tree
    look_for_stuff = False
    for line in fl:
        args = line.strip().split()
        if args[0] == "$":
            if args[1] == "cd":
                directory = args[2]
                # Change directory
                if directory == "/":
                    current_tree = master_tree
                elif directory == "..":
                    # Change current to parent
                    current_tree = current_tree.parent
                else:
                    # Assume directory exists
                    current_tree = current_tree.fetch_child(directory)

                look_for_stuff = False

            elif args[1] == "ls":
                look_for_stuff = True
            else:
                # Ignore unexpected commands
                look_for_stuff = False
                continue
        elif look_for_stuff:
            if args[0] == "dir":
                # Add child directory tree
                child_tree = Tree(args[1], current_tree)
                current_tree.add_child(child_tree)
            else:
                # This is a file size. We don't care about the file's name.
                # Add the file size to the current tree's byte count
                file_size = int(args[0])
                current_tree.update_size(file_size)

    # master_tree.display_tree()

    update_size = 30000000
    unused_space = 70000000 - master_tree.filebytes
    extra_space_required = update_size - unused_space
    nodes = master_tree.find_nodes_by_size(extra_space_required)
    # Get the size of the directory with the smallest required space for deletion
    print(f"Size of directory to delete: {min(node.filebytes for node in nodes)}")
