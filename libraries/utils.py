"""
Utility functions and helpers.
"""
import pdb
import re
import sys

from robot.libraries.BuiltIn import BuiltIn


# Helpful aliases
debug = pdb.Pdb(stdout=sys.__stdout__).set_trace
run = BuiltIn().run_keyword
get_library = BuiltIn().get_library_instance


def parse_raw_data(text):
    """
    Example function which parses input data.
    """
    pattern = re.compile(r"(^[\w\W]+)\:\s+(.*)$")
    result = {}
    for line in text.split("\n"):
        match = pattern.search(line)
        if match:
            key, value = match.groups()
            result[key] = value
        else:
            raise ValueError(f"Invalid line: {line}")
    return result


def get_variable(var_name):
    """Returns Robot Framework variable by its name.

    Boolean values casted to string are converted back to Python booleans.
    Non-string type variables are left untouched."""
    var = BuiltIn().get_variable_value(var_name)
    if not isinstance(var, str):
        return var
    return {
        "${True}": True,
        "True": True,
        "${False}": False,
        "False": False,
    }.get(var.strip(), var)
