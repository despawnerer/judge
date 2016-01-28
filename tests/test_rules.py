from unittest import TestCase

from judge.decide import decide, rules
from judge.predicates import lt, gt, eq


class RulesTestCase(TestCase):
    def test_len(self):
        these_rules = rules(
            (gt(0), 'positive'),
            (lt(0), 'negative'),
        )
        self.assertEqual(len(these_rules), 2)

    def test_addition(self):
        rules1 = rules(
            (gt(0), 'positive'),
            (lt(0), 'negative'),
        )
        rules2 = rules(
            (eq(0), 'zero'),
        )
        these_rules = rules1 + rules2
        self.assertEqual(len(these_rules), 3)
        self.assertEqual(decide(these_rules, 0), 'zero')
