from unittest import TestCase

from .dagoba import Dagoba
import fixtures


class DbModelTest(TestCase, fixtures.TestMixin):

    nodes = [
        {'_id': 1, 'name': 'foo'},
        {'_id': 2, 'name': 'bar'},
    ]
    edges = [
        {'_from': 1, '_to': 2},
    ]

    def setUp(self):
        self.db = Dagoba(self.nodes, self.edges)

    def test_nodes(self):
        nodes = list(self.db.nodes())
        self.assertEqual(2, len(nodes))
        self.assert_item(nodes, _id=1, name='foo')
        self.assert_item(nodes, _id=2, name='bar')

    def test_edges(self):
        edges = list(self.db.edges())
        self.assertEqual(1, len(edges))
        self.assert_item(edges, _from=1, _to=2)

    def test_nodes_with_duplicate_id(self):
        nodes = [
            {'_id': 1, 'name': 'foo'},
            {'_id': 1, 'name': 'bar'},
        ]
        with self.assertRaises(ValueError):
            Dagoba(nodes, self.edges)

    def test_invalid_edge(self):
        edges = [{'_from': -1, '_to': 2}]
        with self.assertRaises(ValueError):
            Dagoba(self.nodes, edges)

    def test_node(self):
        self.assertIsNotNone(self.db.node(1))

    def test_node_invalid_pk(self):
        with self.assertRaises(KeyError):
            self.db.node(-1)
