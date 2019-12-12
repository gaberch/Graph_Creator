## A simple unit test example. Replace by your own tests

import sys
import unittest

from a1ece650 import *

class A1TestSet(unittest.TestCase):

    def test_parser(self):

        with self.assertRaises(Exception):
            parse_input('a"test street" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input("a 'test street' (4,1)(4,3)")

        with self.assertRaises(Exception):
            parse_input(' a "test street" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('aa "test street" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('A "test street" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('1a "test street" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('a1 "test street" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('a\n "test street" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('a\t "test street" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('x "test street" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('"test street" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('a test street" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('a ""test street" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('a "test" street" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('a "test street (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('a "test street"(4,1)(4,3)')

        # with self.assertRaises(Exception):
        #     parse_input('a "test street" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('a "1test street" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('a "tes1t street" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('a "test street1" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('a ""test street (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('a "" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('a "?test street" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('a "test st?reet" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('a "test street?" (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (41)(4,3)(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,1,)(4,3)(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (41,)(4,3)(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,1),(4,3),(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,1)(4,3)(4,5')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,1)(4,3(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,1,2)(4,3)(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" 4,1)(4,3)(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,1)(4,3,2)(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,1)(4,3)(a,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,1)(4,")(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,1)(4,3):(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,1)(4,3)(4,5),')

        with self.assertRaises(Exception):
            parse_input('"a "test street" (4,1)(4,3)(4,5)"')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,1)(4,3)(4,5) hello')

        with self.assertRaises(Exception):
            parse_input('a "test street" d (4,1)(4,3)(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,1)((4,3)(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,1)(- 4,3)(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" ((4,1)(4,3)(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,,1)(4,3)(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4 4,1)(4,3)(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,1)(4,3))(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,1)(,)4,3(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,1)(4,3 3)(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,1)(4,3))(4,5)')

        with self.assertRaises(Exception):
            parse_input('a "test street" (4,1)4,3)(4,5)')


        with self.assertRaises(Exception):
            parse_input('a " " (4,1)(4,3)')

        with self.assertRaises(Exception):
            parse_input('r " "')

        with self.assertRaises(Exception):
            parse_input('r "test street" (4,1)(4,3)(4,5)')

        with self.assertRaises(Exception):
            parse_input('r "test street" (')

        with self.assertRaises(Exception):
            parse_input('r "test street" a')

        with self.assertRaises(Exception):
            parse_input(' r "test street"')

        with self.assertRaises(Exception):
            parse_input('r"test street"')

        with self.assertRaises(Exception):
            parse_input('r "test s1treet"')

        with self.assertRaises(Exception):
            parse_input('r "test s?treet"')

        with self.assertRaises(Exception):
            parse_input('r "test street')

        with self.assertRaises(Exception):
            parse_input('g "test street"')

        with self.assertRaises(Exception):
            parse_input(' g')



    def test_street_db(self):
        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a "a" (4,1)(4,3)(4,5)')
        cmd2, street2, pts2 = parse_input('a "A" (4,1)(4,3)(4,5)')
        cmd3, street3, pts3 = parse_input('a "A" (4,1)')
        cmd4, street4, pts4 = parse_input('a "A" (4,1)')

        with self.assertRaises(Exception):
            if cmd1 == "a":
                street_db.add(street1, pts1)
            if cmd2 == "a":
                street_db.add(street2, pts2)
        with self.assertRaises(Exception):
            if cmd3 == "a":
                street_db.add(street3, pts3)

        with self.assertRaises(Exception):
            if cmd4 == "a":
                street_db.add(street4, pts4)

        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a "King Street" (4,1)(4,3)(4,5)')
        cmd2, street2, pts2 = parse_input('a "KING Street" (4,1)(4,3)(4,5)')

        with self.assertRaises(Exception):
            if cmd1 == "a":
                street_db.add(street1, pts1)
            if cmd2 == "a":
                street_db.add(street2, pts2)

        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a "King Street" (4,1)(4,3)(4,5)')
        cmd2, street2, pts2 = parse_input('a "king street" (4,1)(4,3)(4,5)')

        with self.assertRaises(Exception):
            if cmd1 == "a":
                street_db.add(street1, pts1)
            if cmd2 == "a":
                street_db.add(street2, pts2)

        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a " King Street" (4,1)(4,3)(4,5)')
        street_db.add(street1,pts1)

        self.assertEqual(cmd1, 'a')
        self.assertEqual(street1, " King Street")
        self.assertEqual(pts1, [[4,1],[4,3],[4,5]])
        self.assertEqual(pts1,street_db.data[street1])
        self.assertIn(street1,street_db.data.keys())

        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a " King Street" (4,1)(4,3)(4,5)')
        street_db.add(street1, pts1)

        self.assertEqual(cmd1, 'a')
        self.assertEqual(street1, " King Street")
        self.assertEqual(pts1, street_db.data[street1])
        self.assertIn(street1, street_db.data.keys())

        cmd2, street2, pts2 = parse_input('c " king street" (1,2)(2,3)')

        street_db.change(street2, pts2)
        self.assertEqual(cmd2, 'c')
        self.assertEqual(street2, " king street")
        self.assertEqual(pts2, street_db.data[street1])

        cmd2, street2, pts2 = parse_input('c "king street" (1,2)(2,3)')

        self.assertEqual(cmd2, 'c')
        with self.assertRaises(Exception):
            street_db.change(street2, pts2)

        cmd2, street2, pts2 = parse_input('c "  king street" (1,2)(2,3)')

        self.assertEqual(cmd2, 'c')
        with self.assertRaises(Exception):
            street_db.change(street2, pts2)

        cmd2, street2, pts2 = parse_input('c " king street" (1,2)')

        self.assertEqual(cmd2, 'c')
        with self.assertRaises(Exception):
            street_db.change(street2, pts2)

        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a "King Street" (4,1)(4,3)(4,5)')
        cmd2, street2, pts2 = parse_input('a "Queen Street" (4,1)(4,3)(4,5)')

        self.assertEqual(cmd1, 'a')
        self.assertEqual(cmd2, 'a')

        street_db.add(street1, pts1)
        street_db.add(street2, pts2)

        cmd2, street2 = parse_input('r "queen street"')

        self.assertEqual(cmd2, "r")
        street_db.remove(street2)
        self.assertNotIn(street2, street_db.data.keys())

        cmd2, street2 = parse_input('r " King Street"')
        self.assertEqual(cmd2, "r")

        with self.assertRaises(Exception):
            street_db.remove(street2)

        cmd2, street2 = parse_input('r "King Street "')
        self.assertEqual(cmd2, "r")

        with self.assertRaises(Exception):
            street_db.remove(street2)

        cmd2, street2 = parse_input('r "King  Street"')
        self.assertEqual(cmd2, "r")

        with self.assertRaises(Exception):
            street_db.remove(street2)

    def test_do_intersect(self):

        p = [[0, 0], [1, 1], [0, 1], [1, 0]]
        self.assertTrue(do_intersect(p[0][0], p[0][1],p[1][0],p[1][1],p[2][0],p[2][1],p[3][0],p[3][1]))

        p = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        self.assertTrue(do_intersect(p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1], p[3][0], p[3][1]))

        p = [[0, 0], [0, 1], [0, 0], [1, 0]]
        self.assertTrue(do_intersect(p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1], p[3][0], p[3][1]))

        p = [[0, 1], [0, 0],  [0, 0], [1, 0]]
        self.assertTrue(do_intersect(p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1], p[3][0], p[3][1]))

        p = [[0, 1], [0, 0], [1, 0], [0, 0]]
        self.assertTrue(do_intersect(p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1], p[3][0], p[3][1]))

        p = [[0, 0], [0, 2], [0, 1], [0, 3]]
        self.assertTrue(do_intersect(p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1], p[3][0], p[3][1]))

        p = [[0, 0], [0, 2], [0, 3], [0, 1]]
        self.assertTrue(do_intersect(p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1], p[3][0], p[3][1]))

        p = [[0, 0], [0, 1], [0, 1], [0, 2]]
        self.assertTrue(do_intersect(p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1], p[3][0], p[3][1]))

        p = [[0, 1], [0, 2], [0, 0], [0, 3]]
        self.assertTrue(do_intersect(p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1], p[3][0], p[3][1]))

        p = [[0, -1], [0, 2], [0, 0], [0, 3]]
        self.assertTrue(do_intersect(p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1], p[3][0], p[3][1]))

    def test_graph_builder(self):
        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a "King Street" (0,0)(1,1)')
        cmd2, street2, pts2 = parse_input('a "Queen Street" (1,0)(0,1)')

        self.assertEqual(cmd1, 'a')
        self.assertEqual(cmd2, 'a')

        street_db.add(street1, pts1)
        street_db.add(street2, pts2)

        graph = GraphBuilder(street_db)
        v, e = graph.build()

        graph_printer = PrintGraph(graph.v, graph.e)
        graph_printer.print_graph()
        self.assertEqual(len(v), 5)
        self.assertEqual(len(e), 4)

        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a "Weber Street" (2,-1) (2,2) (5,5) (5,6) (3,8)')
        cmd2, street2, pts2 = parse_input('a "King Street S" (4,2) (4,8)')
        cmd3, street3, pts3 = parse_input('a "Davenport Road" (1,4) (5,8)')

        self.assertEqual(cmd1, 'a')
        self.assertEqual(cmd2, 'a')
        self.assertEqual(cmd3, 'a')

        street_db.add(street1, pts1)
        street_db.add(street2, pts2)
        street_db.add(street3, pts3)

        graph = GraphBuilder(street_db)
        v, e = graph.build()

        graph_printer = PrintGraph(graph.v, graph.e)
        graph_printer.print_graph()
        self.assertEqual(len(v),10)
        self.assertEqual(len(e),9)

        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a "Weber Street" (2,-1) (2,2)')
        cmd2, street2, pts2 = parse_input('a "King Street S" (4,2) (4,8)')
        cmd3, street3, pts3 = parse_input('a "Davenport Road" (1,4) (5,8)')

        self.assertEqual(cmd1, 'a')
        self.assertEqual(cmd2, 'a')
        self.assertEqual(cmd3, 'a')

        street_db.add(street1, pts1)
        street_db.add(street2, pts2)
        street_db.add(street3, pts3)

        graph = GraphBuilder(street_db)
        v, e = graph.build()

        graph_printer = PrintGraph(graph.v, graph.e)
        graph_printer.print_graph()
        self.assertEqual(len(v), 5)
        self.assertEqual(len(e), 4)

        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a "Weber Street" (2,-1) (2,2)')
        cmd3, street3, pts3 = parse_input('a "Davenport Road" (1,4) (5,8)')

        self.assertEqual(cmd1, 'a')
        self.assertEqual(cmd3, 'a')

        street_db.add(street1, pts1)
        street_db.add(street3, pts3)

        graph = GraphBuilder(street_db)
        v, e = graph.build()

        graph_printer = PrintGraph(graph.v, graph.e)
        graph_printer.print_graph()
        self.assertEqual(len(v), 0)
        self.assertEqual(len(e), 0)



        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a "King Street" (0,0)(0,1)')
        cmd2, street2, pts2 = parse_input('a "Queen Street" (0,2)(0,3)')

        self.assertEqual(cmd1, 'a')
        self.assertEqual(cmd2, 'a')

        street_db.add(street1, pts1)
        street_db.add(street2, pts2)

        graph = GraphBuilder(street_db)
        v, e = graph.build()
        self.assertEqual(len(v), 0)
        self.assertEqual(len(e), 0)



        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a "King Street" (0,0)(0,1)')
        cmd2, street2, pts2 = parse_input('a "Queen Street" (1,0)(1,1)')

        self.assertEqual(cmd1, 'a')
        self.assertEqual(cmd2, 'a')

        street_db.add(street1, pts1)
        street_db.add(street2, pts2)

        graph = GraphBuilder(street_db)
        v, e = graph.build()
        self.assertEqual(len(v), 0)
        self.assertEqual(len(e), 0)

        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a "King Street" (0,0)(0,1)(0,4)(0,6)')
        cmd2, street2, pts2 = parse_input('a "Queen Street" (2,2)(0,2)(0,3)(2,3)')

        self.assertEqual(cmd1, 'a')
        self.assertEqual(cmd2, 'a')

        street_db.add(street1, pts1)
        street_db.add(street2, pts2)

        graph = GraphBuilder(street_db)
        v, e = graph.build()
        graph_printer = PrintGraph(graph.v, graph.e)
        graph_printer.print_graph()
        self.assertEqual(len(v), 5)
        self.assertEqual(len(e), 4)

        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a "a" (0,0)(0,4)(4,4)(4,8)(0,8)')
        cmd2, street2, pts2 = parse_input('a "b" (1,0)(1,7)')
        cmd3, street3, pts3 = parse_input('a "c" (3,0)(3,7)')
        cmd4, street4, pts4 = parse_input('a "d" (2,0)(2,9)')

        street_db.add(street1, pts1)
        street_db.add(street2, pts2)
        street_db.add(street3, pts3)
        street_db.add(street4, pts4)

        graph = GraphBuilder(street_db)
        v, e = graph.build()
        graph_printer = PrintGraph(graph.v, graph.e)
        graph_printer.print_graph()
        self.assertEqual(len(v), 14)
        self.assertEqual(len(e), 13)

        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a "a" (0,0)(0,4)(4,4)(4,9)(0,9)')
        cmd2, street2, pts2 = parse_input('a "b" (1,0)(1,7)')
        cmd3, street3, pts3 = parse_input('a "c" (3,0)(3,7)')
        cmd4, street4, pts4 = parse_input('a "d" (2,0)(2,9)')

        street_db.add(street1, pts1)
        street_db.add(street2, pts2)
        street_db.add(street3, pts3)
        street_db.add(street4, pts4)

        graph = GraphBuilder(street_db)
        v, e = graph.build()
        graph_printer = PrintGraph(graph.v, graph.e)
        graph_printer.print_graph()
        self.assertEqual(len(v), 13)
        self.assertEqual(len(e), 12)

        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a "King Street" (0,0)(0,1)')
        cmd2, street2, pts2 = parse_input('a "Queen Street" (0,1)(1,2)')

        self.assertEqual(cmd1, 'a')
        self.assertEqual(cmd2, 'a')

        street_db.add(street1, pts1)
        street_db.add(street2, pts2)

        graph = GraphBuilder(street_db)
        v, e = graph.build()
        graph_printer = PrintGraph(graph.v, graph.e)
        graph_printer.print_graph()
        self.assertEqual(len(v), 3)
        self.assertEqual(len(e), 2)

        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a "King Street" (0,0)(0,1)')
        cmd2, street2, pts2 = parse_input('a "Queen Street" (0,1)(0,2)')

        self.assertEqual(cmd1, 'a')
        self.assertEqual(cmd2, 'a')

        street_db.add(street1, pts1)
        street_db.add(street2, pts2)

        graph = GraphBuilder(street_db)
        v, e = graph.build()
        graph_printer = PrintGraph(graph.v, graph.e)
        graph_printer.print_graph()
        self.assertEqual(len(v), 3)
        self.assertEqual(len(e), 2)

        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a "King Street" (0,0)(1,0)')
        cmd2, street2, pts2 = parse_input('a "Queen Street" (1,0)(2,0)')

        self.assertEqual(cmd1, 'a')
        self.assertEqual(cmd2, 'a')

        street_db.add(street1, pts1)
        street_db.add(street2, pts2)

        graph = GraphBuilder(street_db)
        v, e = graph.build()
        graph_printer = PrintGraph(graph.v, graph.e)
        graph_printer.print_graph()
        self.assertEqual(len(v), 3)
        self.assertEqual(len(e), 2)

        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a "King Street" (1,0)(4,0)')
        cmd2, street2, pts2 = parse_input('a "Queen Street" (2,0)(5,0)')

        self.assertEqual(cmd1, 'a')
        self.assertEqual(cmd2, 'a')

        street_db.add(street1, pts1)
        street_db.add(street2, pts2)

        graph = GraphBuilder(street_db)
        v, e = graph.build()
        graph_printer = PrintGraph(graph.v, graph.e)
        graph_printer.print_graph()
        self.assertEqual(len(v), 4)
        self.assertEqual(len(e), 3)

        street_db = StreetDB()
        cmd1, street1, pts1 = parse_input('a "King Street" (0,0)(0,1)')
        cmd2, street2, pts2 = parse_input('a "Queen Street" (1,0)(1,1)')

        self.assertEqual(cmd1, 'a')
        self.assertEqual(cmd2, 'a')

        street_db.add(street1, pts1)
        street_db.add(street2, pts2)

        graph = GraphBuilder(street_db)
        v, e = graph.build()
        self.assertEqual(len(v), 0)
        self.assertEqual(len(e), 0)


    def test_get_edges(self):

        intersection_set = {2:(1,0),3:(2,0),4:(3,0)}
        vertices = {1:(0,0),5:(4,0)}
        edges = []
        x1 = 0
        y1 = 0
        x2 = 4
        y2 = 0
        result = get_edges(x1, y1, x2, y2, intersection_set, vertices, edges)
        self.assertItemsEqual(result, [(1,2),(2,3),(3,4),(4,5)])

        intersection_set = {2: (1, 0), 3: (2, 0), 5: (3, 0)}
        vertices = {1: (0, 0), 5: (3, 0)}
        edges = [(1,10)]
        x1 = 0
        y1 = 0
        x2 = 3
        y2 = 0
        edges = get_edges(x1, y1, x2, y2, intersection_set, vertices, edges)
        self.assertItemsEqual(edges, [(1, 2), (2, 3), (3, 5), (1, 10)])



















    # def test_upper(self):
    #     """Test the upper() function of class string"""
    #     self.assertEqual('foo'.upper(), 'FOO')
    #
    # def test_isupper(self):
    #     """Test isupper() function of class string"""
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('foo'.isupper())
    #     self.assertFalse('foo'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_failing(self):
    #     """A test that fails"""
    #     self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
