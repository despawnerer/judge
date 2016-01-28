import numbers
import collections


# catch-all predicate that always matches

otherwise = lambda *args, **kwargs: True


# types

instancechecker = lambda cls: lambda x: isinstance(x, cls)
subclasschecker = lambda cls: lambda x: issubclass(x, cls)

is_string = lambda x: isinstance(x, basestring)
is_number = lambda x: isinstance(x, numbers.Number)
is_callable = lambda x: isinstance(x, collections.Callable)
is_sequence = lambda x: isinstance(x, collections.Sequence)
is_mapping = lambda x: isinstance(x, collections.Mapping)


# identity checks

is_ = lambda y: lambda x: x is y
is_not = lambda y: lambda x: x is not y


# comparisons

eq = lambda y: lambda x: x == y
ne = lambda y: lambda x: x != y
gt = lambda y: lambda x: x > y
ge = lambda y: lambda x: x >= y
lt = lambda y: lambda x: x < y
le = lambda y: lambda x: x <= y


# collections

contains = lambda y: lambda x: y in x


# math

divisible_by = lambda *ys: lambda x: all(x % y == 0 for y in ys)


# strings

starts_with = lambda sub: lambda s: s.startswith(sub)
ends_with = lambda sub: lambda s: s.endswith(sub)
