#!/usr/bin/python3
"""A unittest class with test cases checking the Base class """
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Defining a test class on the Base class"""


    def setUp(self):
        """Set up resources for each test method"""
        print("Setting up resources...")

        Base._Base__nb_objects = 0

    def tearDown(self):
         """Tear down resources after each test method"""
         print("Tearing down resources...")

    def test_default_id(self):
        """Tests the default id method"""
        base = Base()

        self.assertEqual(base.id, 1)

    def test_id_increment(self):
        """Tests if id increments correctly"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, base1.id + 1)

    def test_id_manual(self):
        """Test if manually provided id is used"""
        base = Base(5)
        self.assertEqual(base.id, 5)

    def test_negative_id(self):
        """Tests for a negative id"""
        base = Base(-3)

        self.assertEqual(base.id, -3)
    
    def test_to_json_string_non_empty(self):
        """Test the to_json_string method with empty dictionary"""
        base = Base()
        json_string = base.to_json_string([{'id': 1, 'width': 5, 'height': 10}])
        self.assertEqual(json_string, '[{"id": 1, "width": 5, "height": 10}]')

    def test_to_json_string_empty(self):
        """Test the to_json_string method with non-empty dictionary"""
        base = Base()
        json_string0 = base.to_json_string(None)
        json_string1 = base.to_json_string({})

        self.assertEqual(json_string0,"[]")
        self.assertEqual(json_string0,"[]")

    def test_from_json_string_empty(self):
        """Test empty from_json_string method"""
        bases = Base.from_json_string("[]")
        
        self.assertEqual(bases, [])

    def test_from_json_string_non_empty(self):
        """Test non empty from_json_string method"""
        json_str = '[{"id": 1}, {"id": 2}]'
        bases = Base.from_json_string(json_str)
        
        self.assertEqual(len(bases), 2)
        self.assertEqual(bases[0]['id'], 1)
        self.assertEqual(bases[1]['id'], 2)

    def test_save_to_file(self):
        """Test the save_to_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(11, 1, 3, 4)
        list_of_rectangles = [r1, r2]
        Rectangle.save_to_file(list_of_rectangles)

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 106)

    def test_load_from_file(self):
        """Test load_from_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(11, 1, 3, 4)
        Rectangle.save_to_file([r1, r2])
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertEqual(str(loaded_rectangles[0]), str(r1))
        self.assertEqual(str(loaded_rectangles[1]), str(r2))

    def test_create(self):
        """Test create method"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        created_rectangle = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(created_rectangle))
        self.assertNotEqual(id(r1), id(created_rectangle))
        self.assertNotEqual(r1, created_rectangle)
            

if __name__ == "__main__":
    unittest.main()
