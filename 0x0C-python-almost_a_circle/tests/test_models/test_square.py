#!/usr/bin/python3
"""Unittests for Square class. - Task 0"""


import io
import unittest
import importlib
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import models.base
import models.rectangle
import models.square


class Test_Square(unittest.TestCase):
    """Class for testing Square class. - Task 0"""

    def setUp(self):
        Square._Base__nb_objects = 0
        importlib.reload(models.square)
        importlib.reload(models.rectangle)
        importlib.reload(models.base)

    def test_init(self):
        a = Square(2)
        self.assertEqual(a.size, 2)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        self.assertEqual(a.id, 1)
        b = Square(1, 9, 2)
        self.assertEqual(b.size, 1)
        self.assertEqual(b.x, 9)
        self.assertEqual(b.y, 2)
        self.assertEqual(b.id, 2)
        c = Square(4, 2, 5, 12)
        self.assertEqual(c.size, 4)
        self.assertEqual(c.x, 2)
        self.assertEqual(c.y, 5)
        self.assertEqual(c.id, 12)
        d = Square(9, 3)
        self.assertEqual(d.size, 9)
        self.assertEqual(d.x, 3)
        self.assertEqual(d.y, 0)
        self.assertEqual(d.id, 3)
        with self.assertRaises(TypeError, msg='width must be an integer'):
            e = Square("hi", 3)
        with self.assertRaises(ValueError, msg='width must be > 0'):
            f = Square(-8, 4)
        with self.assertRaises(TypeError, msg='width must be an integer'):
            g = Square([1, 2, 3], 4)
        with self.assertRaises(TypeError, msg='x must be an integer'):
            l = Square(3, "hi")
        with self.assertRaises(TypeError, msg='x must be an integer'):
            m = Square(3, [1, 2])
        with self.assertRaises(TypeError, msg='x must be an integer'):
            n = Square(5, float(8))
        with self.assertRaises(ValueError, msg='x must be > 0'):
            o = Square(1, 8, -3)
        with self.assertRaises(TypeError, msg='y must be an integer'):
            p = Square(4, 3, "hi")
        with self.assertRaises(TypeError, msg='y must be an integer'):
            q = Square(1, 19, set([1, 22, 2, 2]))
        with self.assertRaises(ValueError, msg='y must be > 0'):
            r = Square(1, 8, -14)

    def test_area(self):
        """Test to make sure area() method outputs as expected."""
        a = Square(4, 5)
        b = a.area()
        self.assertEqual(b, 16)

    def test_display(self):
        a = Square(3)
        s = "###\n###\n###\n"
        f = io.StringIO()
        with redirect_stdout(f):
            a.display()
        self.assertEqual(f.getvalue(), s)

    def test_display_xy(self):
        a = Square(4, 2, 3)
        s = "\n\n\n  ####\n  ####\n  ####\n  ####\n"
        f = io.StringIO()
        with redirect_stdout(f):
            a.display()
        self.assertEqual(f.getvalue(), s)

    def test_str(self):
        a = Square(1, 2, 3, 4)
        s = "[Square] (4) 2/3 - 1"
        self.assertEqual(str(a), s)
