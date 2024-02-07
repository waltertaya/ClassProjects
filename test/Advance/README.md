# Advanced Python3

## String Template Class in Python

- Template class allows us to create simplified syntax for output specification.
- The format uses placeholder names formed by `$' with valid python identifiers.
- Writing `$$` creates a single escaped `$`.

## Python String Template

- The Python String Template is created by passing the template string to its constructor.
- Example:

```from string import Template


# if you want to change $ to "#"
class myTemplate(Template):
	delimiter = "#"

names = [{firstname: Joe, lastname: mark}, {firstname: Harris, lastname: White}]
t = myTemplate(#firstname #lastname)

```

## Argparse Tutorial
