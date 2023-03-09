import os
from pydoc import locate

from dotenv import dotenv_values

DIRNAME = os.path.dirname(os.path.abspath(__file__))
PACKAGE_ROOT = os.path.abspath(os.path.join(DIRNAME, os.pardir))


def import_variables_from_module(module):
    """Import whole module containing variables.

    Use this when you have just a list of names or instantiated classes.
    Don't use this when you have settings for multiple environments.
    """
    variables = locate(f"{module}")
    if not variables:
        raise ImportError(f"Cannot import variables from {module}.")
    return variables


def import_variables_from_class(module, class_name, env):
    """Import a variable object preserving full namespace.

    Use this when you have settings for multiple environments.
    Usage:
        >>> import_from("kassa", "Kassa", "dev")
        <class 'variables.kassa.DevKassa'>
    """
    if env:
        variables = locate(f"{module}.{env.title()}{class_name}")
    else:
        variables = locate(f"{module}.{class_name}")
    if not variables:
        raise ImportError(f"Cannot import variables from {module}.{class_name} with {env} config")
    return variables


def import_variables_from_env(var_names: list = None, load_dotenv=True) -> dict:
    """Import relevant environment variables.

    Names of variables to import are deduced from `.env.template` or they can be
    named explicitly.

    If variable has not been set in environment, it will be loaded from `.env`.
    Raises if variable not found in either."""

    env_vars = {}
    if not var_names:
        env_template_file = os.path.join(PACKAGE_ROOT, ".env.template")
        env_template = open(env_template_file, "r", encoding="utf-8").read().strip()
        var_names = [line.strip().removesuffix("=") for line in env_template.splitlines()]

    for var in var_names:
        if not var in env_vars:
            try:
                print(f"Looking for {var}")
                value = os.environ.get(var) or dotenv_values()[var]
                env_vars.update({var: value})
            except KeyError as e:
                raise NameError(f"Required environment variable not found: {var}") from e

    return env_vars


def get_vars_from_config(config_object):
    return {k: getattr(config_object, k) for k in dir(config_object) if not k.startswith("_")}
