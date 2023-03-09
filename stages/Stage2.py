"""Example Consumer stage of an RPA process.

This is a template to be used as the starting point for RPA development.
Replace all docstrings in this module with your own when implementing the stage
(including this one).
"""

from robot.api import logger
from robot.api.deco import keyword
from RPALibrary.stages.Consumer import Consumer

from libraries.utils import debug, run, get_variable, get_library


class Stage2(Consumer):
    """Stage class inherits either RPALibrary.stages.Producer or RPALibrary.stages.Consumer
    and is named according to its place in the overall process sequence
    (starting from ``Stage0.py``, followed by ``Stage1.py`` etc.).

    Typically, stages following the first one (numbered 1 and upwards) are Consumers.
    Implement ``main_action`` and, optionally, ``pre_action`` and ``post_action`` for handling task objects.
    Call ``main loop`` from Robot script:

    .. code:: robotframework

        Library  ../stages/Stage0.py

        *** Tasks ***
        My Consumer stage
            [Tags]    stage_1
            [Setup]    Stage1.Setup
            Stage1.Main Loop
            [Teardown]    Stage1.Teardown
    """

    def __init__(self):
        super().__init__()

    def setup(self):
        """Steps performed only once at the start of this stage.

        Set this keyword as the Task Setup of the Robot Task corresponding to this stage. Implementation is optional.
        """
        pass

    def pre_action(self, to):
        """Action to do for every task object before the error handled main action.

        Implementation is optional. See ``RPALibrary.stages.Consumer`` for details.
        """
        return to

    def main_action(self, to):
        """Define the main workflow for consuming task objects.

        Implementation is mandatory. See ``RPALibrary.stages.Consumer`` for details.
        """
        raise NotImplementedError

    def post_action(self, to, status):
        """Action to do for every task object after the main action has completed succesfully or failed.

        Implementation is optional. See ``RPALibrary.stages.Consumer`` for details.
        """
        return to

    def action_on_fail(self, to):
        """Custom action to do when an error is encountered."""
        pass

    def action_on_skip(self, to):
        """Custom action to do when a task object is skipped."""
        pass

    def teardown(self):
        """Steps performed only once at the end of this stage.

        Set this keyword as the Task Teardown of the Robot Task corresponding to this stage. Implementation is optional.
        """
        pass
