import unittest
from RulesOf6005 import RulesOf6005Class

class TestRulesOf6005(unittest.TestCase):

    def test_may_use_code_in_assignment(self):
        # Test case: un-cited publicly-available code, should return False
        self.assertFalse(RulesOf6005Class.may_use_code_in_assignment(
            written_by_yourself=False,
            available_to_others=True,
            written_as_coursework=False,
            citing_your_source=False,
            implementation_required=False
        ), "Expected false: un-cited publicly-available code")

        # Test case: self-written required code, should return True
        self.assertTrue(RulesOf6005Class.may_use_code_in_assignment(
            written_by_yourself=True,
            available_to_others=False,
            written_as_coursework=True,
            citing_your_source=True,
            implementation_required=True
        ), "Expected true: self-written required code")

    # Additional test cases:

    def test_cited_publicly_available_code_but_required(self):
        # Test case: publicly available and cited, but required to be implemented by the student, should return False
        self.assertFalse(RulesOf6005Class.may_use_code_in_assignment(
            written_by_yourself=False,
            available_to_others=True,
            written_as_coursework=True,
            citing_your_source=True,
            implementation_required=True
        ), "Expected false: publicly available and cited, but required to be implemented")

    def test_cited_publicly_available_code_not_required(self):
        # Test case: publicly available and cited, and not required to be implemented by the student, should return True
        self.assertTrue(RulesOf6005Class.may_use_code_in_assignment(
            written_by_yourself=False,
            available_to_others=True,
            written_as_coursework=True,
            citing_your_source=True,
            implementation_required=False
        ), "Expected true: publicly available and cited, not required to be implemented")

if __name__ == '__main__':
    unittest.main()
