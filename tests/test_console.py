#!/usr/bin/python3
"""Unit tests for console"""

import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test cases for HBNB console"""

    def setUp(self):
        """Set up for test cases"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down for test cases"""
        pass

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create City")
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Place")
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Review")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {}".format(obj_id))
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel {}".format(obj_id))
            self.assertEqual(f.getvalue().strip(), "")

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch('sys.stdout', new=StringIO())
