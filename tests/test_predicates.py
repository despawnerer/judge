from unittest import TestCase

from judge.predicates import (
    otherwise,
    is_,
    is_not,
    eq,
    ne,
    gt,
    ge,
    lt,
    le,
    contains,
    divisible_by,
    starts_with,
    ends_with,
)


class OtherwiseTestCase(TestCase):
    def test_otherwise(self):
        self.assertTrue(otherwise())
        self.assertTrue(otherwise(10))
        self.assertTrue(otherwise(a=20))
        self.assertTrue(otherwise(10, 'str', [3, 4], a=20, b='some'))


class IdentityTestCase(TestCase):
    def test_is(self):
        isnone = is_(None)
        self.assertTrue(isnone(None))
        self.assertFalse(isnone(0))

    def test_is_not(self):
        notnone = is_not(None)
        self.assertTrue(notnone(0))
        self.assertFalse(notnone(None))


class ComparisonTestCase(TestCase):
    def test_eq(self):
        is_ten = eq(10)
        self.assertTrue(is_ten(10))
        self.assertFalse(is_ten(20))

    def test_ne(self):
        isnt_ten = ne(10)
        self.assertTrue(isnt_ten(20))
        self.assertFalse(isnt_ten(10))

    def test_gt(self):
        over_dozen = gt(12)
        self.assertTrue(over_dozen(20))
        self.assertFalse(over_dozen(12))
        self.assertFalse(over_dozen(10))

    def test_ge(self):
        dozen_or_more = ge(12)
        self.assertTrue(dozen_or_more(20))
        self.assertTrue(dozen_or_more(12))
        self.assertFalse(dozen_or_more(10))

    def test_lt(self):
        less_than_ten = lt(10)
        self.assertTrue(less_than_ten(8))
        self.assertFalse(less_than_ten(10))
        self.assertFalse(less_than_ten(20))

    def test_le(self):
        ten_or_less = le(10)
        self.assertTrue(ten_or_less(8))
        self.assertTrue(ten_or_less(10))
        self.assertFalse(ten_or_less(20))


class CollectionsTestCase(TestCase):
    def test_contains(self):
        checker = contains(10)
        self.assertTrue(checker([0, 10, 20]))
        self.assertFalse(checker([30, 40, 50]))

    def test_contains_string(self):
        checker = contains('bar')
        self.assertTrue(checker('foo_bar_baz'))
        self.assertFalse(checker('abc_def_ghi'))


class MathTestCase(TestCase):
    def test_divisible_by_single_number(self):
        div3 = divisible_by(3)
        self.assertTrue(div3(3))
        self.assertFalse(div3(5))

    def test_divisible_by_multiple_numbers(self):
        div3and5 = divisible_by(3, 5)
        self.assertTrue(div3and5(15))
        self.assertFalse(div3and5(3))
        self.assertFalse(div3and5(5))


class StringTestCase(TestCase):
    def test_starts_with(self):
        starts_here = starts_with('here')
        self.assertTrue(starts_here('here i am'))
        self.assertFalse(starts_here('there he is'))

    def test_ends_with(self):
        ends_now = ends_with('now')
        self.assertTrue(ends_now('this ends now'))
        self.assertFalse(ends_now('this doesnt end'))
