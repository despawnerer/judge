from functools import partial


__all__ = ['decide', 'rules', 'NoMatchingRule']


def decide(rules_obj, *args, **kwargs):
    """
    Return first matching value from rules_obj by invoking each predicate
    within it with *args, **kwargs until a match is found. rules_obj
    must be an instance of rules.

    If a non-rules object is passed as rules_obj, raise TypeError.

    If no match is found, raise NoMatchingRule.

    If no arguments are passed, then return a partially applied function
    that can be later used to choose a value using a the given set of rules.

    """
    if not isinstance(rules_obj, rules):
        raise TypeError(
            "Expected 'rules' object, got '%s'" % type(rules_obj).__name__)

    if not args and not kwargs:
        return partial(decide, rules_obj)

    for predicate, value in rules_obj:
        matches = predicate(*args, **kwargs)
        if matches:
            if isinstance(value, rules):
                return decide(value, *args, **kwargs)
            else:
                return value
    else:
        raise NoMatchingRule(args, kwargs)


class rules(object):
    """
    A list of predicates to be used in the decision process.

    Each rule is a 2-tuple (predicate, value). predicate is a function
    that returns True or False depending on whether the given arguments
    match some condition. value is the value that will be returned if the
    predicate matches. Rules can be nested by setting value to another
    rules object.
    """
    def __init__(self, *rules):
        self._rules = rules

    def __iter__(self):
        for rule in self._rules:
            yield rule

    def __len__(self):
        return len(self._rules)

    def __add__(self, other):
        if isinstance(other, rules):
            return rules(*(self._rules + other._rules))
        else:
            raise NotImplementedError


class NoMatchingRule(Exception):
    """
    No matching rule found for given value.
    """
