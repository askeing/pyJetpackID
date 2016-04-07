__author__ = 'Askeing'

import os
import unittest
from jetpackid.jetpackid import JetpackID


class MyTestCase(unittest.TestCase):
    def test_is_valid_id_true(self):
        self.assertTrue(JetpackID.is_valid_id("@askeing_test-0.0.1.xpi"))
        self.assertTrue(JetpackID.is_valid_id("askeing@JETPACK_ID-0.0.1"))
        self.assertTrue(JetpackID.is_valid_id("007@askeing-test.xpi"))
        self.assertTrue(JetpackID.is_valid_id("{12345678-1234-1234-1234-123412341234}"))
        self.assertTrue(JetpackID.is_valid_id("{abcdefAB-ABCD-abcd-abcd-abcdefABCDEF}"))

    def test_is_valid_id_false(self):
        self.assertFalse(JetpackID.is_valid_id("{abcdefgh-wxyz-abcd-abcd-abcdefabcdef}"))
        self.assertFalse(JetpackID.is_valid_id("@***askeing.xpi"))
        self.assertFalse(JetpackID.is_valid_id("#askeing.xpi"))
        self.assertFalse(JetpackID.is_valid_id("-"))

    def test_get_id(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))

        file_path = os.path.join(current_dir, 'package.json')
        self.assertEqual(JetpackID.get_id(file_path), '@testname')

        file_path = os.path.join(current_dir, 'package_fail.json')
        self.assertEqual(JetpackID.get_id(file_path), None)


if __name__ == '__main__':
    unittest.main()
