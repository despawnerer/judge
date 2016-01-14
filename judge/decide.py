from functools import partial


__all__ = ['decide', 'rules', 'NoMatchingRule']


def decide(rules_obj, *args, **kwargs):
    """
    Return first matching value from rules_obj by invoking each predicate
    within it with *args, **kwargs until a match is found. rules_obj
    must be an instance of rules.

    If no match is found, raise NoMatchingRule.

    If no arguments are passed, then return a partially applied function
    that can be later used to choose a value using a the given set of rules.

    """
    assert isinstance(rules_obj, rules)

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
        self.__rules = rules

    def __iter__(self):
        for rule in self.__rules:
            yield rule


class NoMatchingRule(Exception):
    """
    No matching rule found for given value.
    """
