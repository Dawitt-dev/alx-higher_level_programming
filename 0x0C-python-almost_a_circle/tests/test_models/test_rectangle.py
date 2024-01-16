#!/usr/bin/python3
"""Defines a class TestRectangleMethods"""

import unittest
import json
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """ Defines tests for Rectangle class """

    def test_docstring(self):
        """ Test if docstring is present """
        self.assertIsNotNone(Rectangle.__doc__)

    def test_constructor(self):
        """ Test constructor """
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_width_height_types(self):
        """ Test for width and height types"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Dave", 6)
            Rectangle('L', 9)
            Rectangle(True, 5)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "wish")
            Rectangle(4, 'W')
            Rectangle(True, 8)

    def test_width_height_ranges(self):
        """ Test for width and height ranges"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 9)
            Rectangle(0, 9)
            Rectangle(0, 3)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(9, -5)
            Rectangle(8, 0)
            Rectangle(1, 0)

    def test_area(self):
        """ Test area method """
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_display(self):
        """ Test display method """
        r = Rectangle(3, 2)
        result = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_str(self):
        """ Test __str__ return value """
        r = Rectangle(4, 6, 2, 1, 12)
        result = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r), result)

    def test_update(self):
        """ Test the update method """
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_to_dictionary(self):
        """ Test to_dictionary method """
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        j = {'id': 11,'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(d, j)
        self.assertEqual(type(d), dict)

    def test_save_to_file(self):
        """ Test save_to_file method """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        s2f = [r1, r2]
        Rectangle.save_to_file(s2f)
        with open("Rectangle.json", mode="r") as myFile:
            data = json.load(myFile)
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]['width'], 10)
            self.assertEqual(data[1]['width'], 2)

    def test_load_from_file(self):
        """ Test load_from_file method """
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 2)
        Rectangle.save_to_file([r1, r2])
        lff = Rectangle.load_from_file()
        self.assertEqual(lff[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(lff[1].to_dictionary(), r2.to_dictionary())


if __name__ == '__main__':
    unittest.main()

