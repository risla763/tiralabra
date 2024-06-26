class Node:
    """
    Luokka, joka alustaa triehen tulevan solmun
    """
    def __init__(self):
        self.children = {}
        self.note = None
        self.weight = 0
        self.value = False


class Trie:
    """
    Datarakenne, johon talletetaan abc notaatio 
    numeroiden muodossa.

    Puuhun talletetaan asteen pituisia haaroja.    
    """
    def __init__(self):
        self.root = Node()

    def insert(self, notes_list):
        node = self.root
        for note in notes_list:
            if note not in node.children:
                node.children[note] = Node() 
            node = node.children[note]
            node.weight += 1
            node.note = note

        node.value = True
        

    def print_trie(self, node=None, depth=0):
        if node is None:
            node = self.root
        for pair, child_node in node.children.items():
            print("  " * depth + str(pair) + " -> " + str(child_node.value) + " (Weight: " + str(child_node.weight) + ")")
            self.print_trie(child_node, depth + 1)

    def search(self, notes):
        node = self.root
        list_of_frequences = []
        list_of_keys = []
        list_of_children = {}
        for note in notes:
            if note not in node.children:
                return None
            node = node.children[note]
        list_of_children.update(node.children)
        for i in list_of_children:
            list_of_frequences.append(list_of_children[i].weight)
        for i in list_of_children.keys():
            list_of_keys.append(i)
        tuple = (list_of_keys, list_of_frequences)
        return tuple

    def add_to_trie(self, notes_data, degree):
        for song in notes_data:
            for i in range(len(song)-1):
                if i < len(song) -1 :
                    self.insert(song[i:i+degree])
                else:
                    break




    



