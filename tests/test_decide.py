import collections
from unittest import TestCase

from judge.decide import decide, rules, NoMatchingRule
from judge.predicates import lt, gt, eq, is_number, is_string, otherwise


class DecideTestCase(TestCase):
    def setUp(self):
        self.positivity_rules = rules(
            (gt(0), 'positive'),
            (lt(0), 'negative'),
        )
        self.type_rules = rules(
            (is_number, rules(
                (gt(0), 'positive number'),
                (eq(0), 'zero'),
                (lt(0), 'negative number'),
            )),
            (is_string, 'string'),
            (otherwise, 'unhandled type'),
        )

    def test_flat_rules(self):
        value = decide(self.positivity_rules, -10)
        self.assertEqual(value, 'negative')

    def test_nested_rules(self):
        value = decide(self.type_rules, 0)
        self.assertEqual(value, 'zero')

    def test_no_matching_rules(self):
        with self.assertRaises(NoMatchingRule):
            decide(self.positivity_rules, 0)

    def test_non_rules_objects_as_rules(self):
        with self.assertRaises(AssertionError):
            decide(['something', 'whatever'], 20)

    def test_partial_application(self):
        positivity = decide(self.positivity_rules)
        self.assertIsInstance(positivity, collections.Callable)
        value = positivity(10)
        self.assertEqual(value, 'positive')
