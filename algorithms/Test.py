import unittest
import mutate


class TestNode(unittest.TestCase):

    def test_initializer(self):
        dna = "actgatcgatcgatcgtcagctactgcatcgatc"
        node = mutate.PhylogeneticNode(dna)
        self.assertIsInstance(node, mutate.PhylogeneticNode)

    def test_getSequence(self):
        dna = "actgatcgatcgatcgtcagctactgcatcgatc"
        node = mutate.PhylogeneticNode(dna)
        node_dna = node.get_sequence()
        self.assertEqual(node_dna, dna)

    def test_setSequence(self):
        dna = "actgatcgatcgatcgtcagctactgcatcgatc"
        node = mutate.PhylogeneticNode(dna)
        node.set_dna_sequence("actgtacacagtgtgtg")
        node_dna = node.get_sequence()
        self.assertNotEqual(node_dna, dna)

    def test_calculateDistance(self):
        dna1 = "actgatcgatcgatcgtcagctactgcatcgatc"
        dna2 = "accgatcgatcgatcggcagctactgcatcgatc"
        node1 = mutate.PhylogeneticNode(dna1)
        node2 = mutate.PhylogeneticNode(dna2)
        calc_distance = mutate.PhylogeneticNode.calculate_distance(node1, node2)
        self.assertEqual(calc_distance, 2)

def build_example_nodes():
    dna1 = "actgatcgatcgatcgtcagctactgcatcgatc"
    dna2 = "accgatcgatcgatcggcagctactgcatcgatc"
    node1 = mutate.PhylogeneticNode(dna1)
    node2 = mutate.PhylogeneticNode(dna2)
    return (node1, node2)

class TestTree(unittest.TestCase):

    def test_initializer(self):
        nodes = build_example_nodes()
        vertices = [nodes[0], nodes[1]]
        edges = [(nodes[0], nodes[1])]
        tree = mutate.Tree(vertices, edges)
        self.assertIsInstance(tree, mutate.Tree)

    def test_getVertices(self):
        nodes = build_example_nodes()
        vertices = [nodes[0], nodes[1]]
        edges = [(nodes[0], nodes[1])]
        tree = mutate.Tree(vertices, edges)
        calc_vertices = tree.get_vertices()
        self.assertEqual(calc_vertices, vertices)

    def test_getEdges(self):
        nodes = build_example_nodes()
        vertices = [nodes[0], nodes[1]]
        edges = [(nodes[0], nodes[1])]
        tree = mutate.Tree(vertices, edges)
        calc_edges = tree.get_edges()
        self.assertEqual(calc_edges, edges)

    def test_addVertex(self):
        nodes = build_example_nodes()
        vertices = [nodes[0], nodes[1]]
        edges = [(nodes[0], nodes[1])]
        tree = mutate.Tree(vertices, edges)
        tree.add_vertex(mutate.PhylogeneticNode("actgtacacagtgtg"))
        self.assertEqual(len(tree.get_vertices()), 3)

    def test_addEdge(self):
        nodes = build_example_nodes()
        vertices = [nodes[0], nodes[1]]
        edges = [(nodes[0], nodes[1])]
        new_node = mutate.PhylogeneticNode("actgtacacagtgtgtg")
        tree = mutate.Tree(vertices, edges)
        tree.add_vertex(new_node)
        tree.add_edge((new_node, vertices[0]))
        self.assertEqual(len(tree.get_edges()), 2)

class TestPhyloTree(unittest.TestCase):

    def test_initializer(self):
        nodes = build_example_nodes()
        vertices = [nodes[0], nodes[1]]
        edges = [(nodes[0], nodes[1])]
        tree = mutate.PhylogeneticTree(vertices, edges)
        self.assertIsInstance(tree, mutate.PhylogeneticTree)
        self.assertEqual(tree.get_root_node(), None)

    def test_rootNode(self):
        nodes = build_example_nodes()
        vertices = [nodes[0], nodes[1]]
        edges = [(nodes[0], nodes[1])]
        tree = mutate.PhylogeneticTree(vertices, edges)
        root = mutate.PhylogeneticNode("actgtacacagtgtgtg")
        tree.set_root_node(root)
        self.assertEqual(root, tree.get_root_node())
        self.assertEqual(len(tree.get_vertices()), 3)



if __name__ == '__main__':
    unittest.main()


