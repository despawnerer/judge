from functools import partial


__all__ = ['decide', 'rules', 'NoMatchingRule']


def decide(rules_obj, *args, **kwargs):
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
    def __init__(self, *rules):
        self.__rules = rules

    def __iter__(self):
        for rule in self.__rules:
            yield rule


class NoMatchingRule(Exception):
    pass
