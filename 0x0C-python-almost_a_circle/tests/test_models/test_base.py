#!/usr/bin/python3
"""Unittests for base model. - Task 0"""


import io
import unittest
import importlib
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import models.base
import models.rectangle
import models.square


class Test_Base(unittest.TestCase):
    """Class for testing base class. - T0"""

    def setUp(self):
        """Setup for reseting tests.- T0"""
        Base._Base__nb_objects = 0
        importlib.reload(models.square)
        importlib.reload(models.rectangle)
        importlib.reload(models.base)

    def test_autoId(self):
        """test automatic id generation. - T0"""
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)

    def test_specificId(self):
        """assigned id. - T0"""
        a = Base(8)
        self.assertEqual(a.id, 8)
