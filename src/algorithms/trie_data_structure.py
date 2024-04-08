class Node:
    def __init__(self):
        self.children = {}
        self.note = None #nuotti
        self.weight = 0
        self.value = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, notes_list):
        node = self.root
        print(node, "self_root")
        print(notes_list, "notes_list")
        for note in notes_list:
            print(note, "testi")
            if note not in node.children:
                node.children[note] = Node() 

                print(node.children[note] ,"uusi lapsi")
            node = node.children[note]
            node.weight += 1
            print(node.weight,"uuden lapsen paino")

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
        print("TÄTÄ SEARCH PALAUTTAA", tuple) #palauttaa lapset ja niiden painot

        return tuple

    def add_to_trie(self, notes_data, degree):
        for i in range(len(notes_data)-1):
            if i < len(notes_data) -1 :
                Trie().insert(notes_data[i:i+degree]) #tässä Triehen lisättäisiin datasta asteen pituisia pätkiä
            else:
                break


#nuotit pitää vielä muuttaa numeroiksi

trie = Trie()
notes_list = "cbeafcg" 
trie.insert(notes_list)  
notes_list2 = "cbcafaa"
trie.insert(notes_list2) 
trie.print_trie()

trie.search("cb")


#Miten eri sävellajeille saadaan eri Triet?
#Trie tyhjennetään välissä
#UI: käyttäjä valitsee sävellajin....ja tällöin Trie muodostuu sen
#sävellajin kappaleista
#kun käyttäjä valitsee toisen sävellajin Trie puhdistuu ja muodostuu sen sävellajin kappaleista

    


