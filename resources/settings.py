"""
Configuration objects.
"""
import datetime
import importlib
import os
import platform

from resources.settings_helpers import (
    PACKAGE_ROOT,
    get_vars_from_config,
    import_variables_from_class,
    import_variables_from_env,
    import_variables_from_module,
)

PLATFORM = platform.system()
TODAY = datetime.datetime.now()


def get_variables(env):
    if env.lower() == "prod":
        robot_vars = get_vars_from_config(ProdConfig)
    elif env.lower() == "test":
        robot_vars = get_vars_from_config(TestConfig)
    else:
        robot_vars = get_vars_from_config(DevConfig)
    robot_vars.update(import_variables_from_env())
    return robot_vars


class Config:
    browser = "gc"
    templates = import_variables_from_module("resources.templates")

    db_server = "mongodb+srv://demorobot-dbxun.mongodb.net"
    db_port = 27017
    db_auth_source = "admin"
    db_name = "demorobot"


class DevConfig(Config):
    _env = "dev"

    db_server = "localhost"


class TestConfig(Config):
    _env = "test"


class ProdConfig(Config):
    _env = "prod"
