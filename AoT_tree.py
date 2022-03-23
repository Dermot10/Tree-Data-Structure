# Tree Data structure
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    # Add child node to children attribute
    # Assign parent as self, since a Tree is recursive structure with each node an instance, and therefore it's own parent
    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    # whilst the instance has parent, increment count
    def get_level(self):
        level = 0
        current = self.parent
        while current:
            level += 1
            current = current.parent
        return level

    # Pretty Print the Tree structure,  hierarchical structure shown
    def printTree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printTree()


# Helper function used to build Tree, when called the instances are  instantiated
def buildTree():
    root = TreeNode("9 Titans")

    Founder = TreeNode("Founder")
    Founder.addChild(TreeNode("Titan Control"))

    Attack = TreeNode("Attack")
    Attack.addChild(TreeNode("Future Memory Inheritance"))

    Female = TreeNode("Female")
    Female.addChild(TreeNode("Adaptation"))
    Female.addChild(TreeNode("Titan Attraction"))

    Armoured = TreeNode("Armoured")
    Armoured.addChild(TreeNode("Armour"))

    Jaw = TreeNode("Jaw")
    Jaw.addChild(TreeNode("Enhanced Jaw strength"))
    Jaw.addChild(TreeNode("Enhanced Claw strength"))
    Jaw.addChild(TreeNode("Enhanced Agility"))

    Colossal = TreeNode("Colossal")
    Colossal.addChild(TreeNode("Enormous Size"))
    Colossal.addChild(TreeNode("Steam emission"))

    Beast = TreeNode("Beast")
    Beast.addChild(TreeNode("Animal Characteristics"))

    Characteristics = TreeNode("")
    Characteristics.addChild(TreeNode("Throwing Ability"))

    Cart = TreeNode("Cart")
    Cart.addChild(TreeNode("Quadrupedal"))
    Cart.addChild(TreeNode("Enhanced Endurance"))

    WarHammer = TreeNode("WarHammer")
    WarHammer.addChild(TreeNode("Structural Hardening"))
    WarHammer.addChild(TreeNode("Remote Control"))

    root.addChild(Founder)
    root.addChild(Attack)
    root.addChild(Female)
    root.addChild(Armoured)
    root.addChild(Colossal)
    root.addChild(Jaw)
    root.addChild(Beast)
    root.addChild(Cart)
    root.addChild(WarHammer)
    Beast.addChild(Characteristics)

    return root


if __name__ == "__main__":
    root = buildTree()
    root.printTree()
