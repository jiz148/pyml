"""
# test_misc_big_number.py

"""
import logging
import os
import unittest
import sys

from ml.utils.logger import get_logger

LOGGER = get_logger(__name__)


class BigNumberTests(unittest.TestCase):
    """
    StackTests includes all unit tests for ml.misc.big_number module
    """
    @classmethod
    def teardown_class(cls):
        logging.shutdown()

    def setUp(self):
        """setup for test"""
        self.test_path = os.path.dirname(os.path.realpath(__file__))
        self.repo_path = os.path.dirname(self.test_path)
        self.proj_path = os.path.join(self.repo_path, "ml")
        self.base_path = os.path.join(self.repo_path, "ml", "misc")
        self.data_path = os.path.join(self.repo_path, "ml", "misc", "datasets")
        pass

    def tearDown(self):
        """tearing down at the end of the test"""
        pass

    def test__init__(self):
        """
        test ml.misc.big_number :: BigNumber :: __init__
        @return:
        """
        from ml.misc.big_number import BigNumber

        max_list = [9, 2, 2, 3, 3, 7, 2, 0, 3, 6, 8, 5, 4, 7, 7, 5, 8, 0, 7]
        tests = [{
            "string": '0', "list": [0],
        }, {
            "string": '-98', "list": [0],
        }, {
            "string": '    888    ', "list": [8, 8, 8],
        }, {
            "string": 778345, "list": [7, 7, 8, 3, 4, 5],
        }, {
            "string": -23524, "list": [0],
        }, {
            "string": sys.maxsize, "list": max_list,
        }, {
            "string": '   +10086', "list": [1, 0, 0, 8, 6],
        }, {
            "string": '', "list": [0],
        }, {
            "string": '+', "list": [0],
        }, {
            "string": '-', "list": [0],
        }, {
            "string": 'abc', "list": [0],
        }, {
            "string": '    1.7', "list": [0],
        }, {
            "string": '-1543-23-12', "list": [0],
        }, {
            "string": None, "list": [0],
        }, {
            "string": int, "list": [0],
        }, {
            "string": ['1'], "list": [0],
        }, {
            "string": {'1': '1'}, "list": [0],
        }]
        for test in tests:
            o = BigNumber(test["string"])
            self.assertListEqual(o.list, test["list"])

    def test_add(self):
        """
        test ml.misc.big_number :: BigNumber :: add
        @return:
        """
        from ml.misc.big_number import BigNumber

        over_num_string = '9223372036854776327'
        tests = [{
            "init": '123', "input": '999', "result": '1122',
        }, {
            "init": str(sys.maxsize), "input": '520', "result": over_num_string,
        }, {
            "init": str(over_num_string), "input": 0, "result": over_num_string,
        }, {
            "init": '345', "input": '-345', "result": '345',
        }, {
            "init": '678', "input": 'string', "result": '678',
        }, {
            "init": None, "input": '789', "result": '789',
        }, {
            "init": '77777', "input": None, "result": '77777',
        }]
        for test in tests:
            obj = BigNumber(test["init"])
            obj.add(test["input"])
            result = obj.to_string()
            self.assertEqual(result, test["result"])
