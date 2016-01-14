judge
=====

`judge` is a Python library for choosing values based on a tree of conditions.

For example:

```python
from judge import decide, rules, gt, lt, eq, is_number, otherwise

positivity = rules(
	(is_number, rules(
		(gt(0), 'positive'),
		(eq(0), 'zero'),
    	(lt(0), 'negative'),
	)),
	(otherwise, 'not a number')
)

decide(positivity, -10)     # 'negative'
decide(positivity, 0)       # 'zero'
decide(positivity, 10)      # 'positive'
decide(positivity, 'text')  # 'not a number'
```


Installation
------------

	$ pip install judge


Usage
-----

```python
judge.decide(rules_obj, *args, **kwargs)
```

Return first matching value from `rules_obj` by invoking each predicate within it with `*args, **kwargs` until a match is found. `rules_obj` must be an instance of `rules`.

If no match is found, raise `NoMatchingRule`.

If no arguments are passed, then return a partially applied function that can be later used to choose a value using a the given set of rules.


```python
judge.rules(*rules)
```

A list of predicates to be used in the decision process.

Each rule is a 2-tuple `(predicate, value)`. `predicate` is a function that returns `True` or `False` depending on whether the given arguments match some condition. `value` is the value that will be returned if the `predicate` matches. Rules can be nested by setting `value` to another `rules` object.


Built-in predicates
-------------------

### Generic

Predicate              | Matches
:----------------------|:-----------------------------------------------
`otherwise`            | Catch-all that matches anything


### Type checks

Predicate              | Matches
:----------------------|:-----------------------------------------------
`instancechecker(cls)` | Instances of `cls`
`subclasschecker(cls)` | Subclasses of `cls`
`is_string`            | Strings
`is_number`            | Numbers (ints, floats, decimals...)
`is_callable`          | Callables (functions, classes...)
`is_sequence`          | Sequences (lists, tuples...)
`is_mapping`           | Mappings (dicts)


### Identity checks

Predicate              | Matches
:----------------------|:-----------------------------------------------
`is_(other)`           | `value is other`
`is_not(other)`        | `value is not other`


### Comparisons

Predicate              | Matches
:----------------------|:-----------------------------------------------
`eq(other)`            | `value == other`
`ne(other)`            | `value != other`
`gt(other)`            | `value > other`
`ge(other)`            | `value >= other`
`lt(other)`            | `value < other`
`le(other)`            | `value <= other`


### Collections

Predicate              | Matches
:----------------------|:-----------------------------------------------
`contains(element)`    | `element in value`


### Mathematical

Predicate              | Matches
:----------------------|:-----------------------------------------------
`divisible_by(*ys)`    | Numbers that are divisible by all of the given divisors `ys`


Examples
--------

### Declarative FizzBuzz

```python
from judge import decide, rules, divisible_by, otherwise

fizzbuzz = decide(rules(
	(divisible_by(3, 5), "FizzBuzz"),
	(divisible_by(3), "Fizz"),
	(divisible_by(5), "Buzz"),
	(otherwise, None)
))

for number in range(1, 101):
	print(fizzbuzz(number) or number)
```
