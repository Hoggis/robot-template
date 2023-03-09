from robot.api.deco import keyword

from robot.api import logger

from libraries.LibraryBase import LibraryBase
from libraries.utils import (
    debug,
    run,
    get_variable,
)


class ExampleLibrary(LibraryBase):
    """
    Template for implementing a robot library.
    """

    def __init__(self):
        super().__init__()
        self.env = get_variable("${ENV}")

    @keyword
    def debug_library(self):
        logger.info(f"{self.__class__}")
        debug()

    @keyword
    def do_something(self):
        run("Log", f"Doing something in {self.env}")
