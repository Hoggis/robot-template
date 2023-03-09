from libraries.utils import get_library


class LibraryBase:
    """Base RF library class for setting useful properties."""

    def __init__(self):
        self.toslib = get_library("TOSLibrary")
