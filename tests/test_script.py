import xyz.abcd.script as module
import unittest as _ut

class Testxyz(_ut.TestCase):

    def test_bin(self):
        self.assertEqual(module.bin(0,0), 0)
