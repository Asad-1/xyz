import abcd.script as module
import unittest as _ut

class TestP1Over2Spectroscopy(_ut.TestCase):

    def test_bin(self):
        self.assertEqual(module.bin(0,0), 0)
