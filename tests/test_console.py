#!/usr/bin/python3
"""Defines unittests for condole.py."""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class TestHBNBCommand(unittest.TestCase):
    """Test for the console class"""

    def setUp(self):
        """Test the setup method"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Test the setup method"""
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        """Test the quite method"""
        self.assertTrue(self.console.onecmd("quit"))
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF_command(self, mock_stdout):
        """Test the setup method"""
        self.assertTrue(self.console.onecmd("EOF"))
        self.assertEqual(mock_stdout.getvalue(), "")

    def test_create_command(self):
        """Test the setup method"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(mock_stdout.getvalue().strip()) == 36)

    def test_show_command(self):
        """Test the setup method"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show BaseModel")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show BaseModel 12345")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** no instance found **")

    def test_all_command(self):
        """Test the setup method"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("all")
            self.assertTrue(len(mock_stdout.getvalue().strip()) == 0)

    def test_count_command(self):
        """Test the setup method"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("count")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("count BadClass")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** class doesn't exist **")

    def test_destroy_command(self):
        """Test the setup method"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** class name missing **")

    def test_update_command(self):
        """Test the setup method"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update BadClass")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** class doesn't exist **")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update BaseModel")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update BaseModel 12345")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** no instance found **")


if __name__ == '__main__':

    unittest.main()
