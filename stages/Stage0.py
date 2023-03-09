"""Example Producer stage of an RPA process.

This is a template to be used as the starting point for RPA development.
Replace all docstrings in this module with your own when implementing the stage
(including this one).
"""

from robot.api import logger
from robot.api.deco import keyword
from RPALibrary.stages.Producer import Producer

from libraries.utils import debug, run, get_variable, get_library


class Stage0(Producer):
    """Stage class inherits either RPALibrary.stages.Producer or RPALibrary.stages.Consumer
    and is named according to its place in the overall process sequence
    (starting from ``Stage0.py``, followed by ``Stage1.py`` etc.).

    Typically, the first stage (numbered 0) is a Producer.
    Implement ``process_data`` and, optionally, ``preloop_action``, ``postprocess_data`` for creating task objects.
    Call ``main loop`` from Robot script:

    .. code:: robotframework

        Library  ../stages/Stage0.py

        *** Tasks ***
        My Producer Stage
            [Tags]    stage_0
            [Setup]    Stage0.Setup
            Stage0.Main Loop
            [Teardown]    Stage0.Teardown
    """

    def __init__(self):
        super().__init__()

    def preloop_action(self):
        """Prefetch data to iterate in ``process_data``.
        This method should return a sequence (list, tuple) or a generator.

        Implementation is optional, but needed in most processes. See ``RPALibrary.stages.Producer`` for details.
        """
        data = []

        return data

    def process_data(self, item):
        """Define how the data is turned into a task object.
        Task object(s) are created from the return value of this method.

        Implementation is mandatory. See ``RPALibrary.stages.Producer`` for details.
        """
        raise NotImplementedError

    def postprocess_data(self, to):
        """
        Postprocess the already created task object.

        Implementation is optional. See ``RPALibrary.stages.Producer`` for details.
        """
        return to

    def action_on_fail(self, to):
        """Custom action to do when an error is encountered.

        Implementation is optional. See ``RPALibrary.stages.BaseStage`` for details.
        """
        pass

    def post_action(self, to, status, *args, **kwargs):
        """Action to do for every task object after the main action has completed succesfully or failed.

        Implementation is optional. See ``RPALibrary.stages.BaseStage`` for details.
        """
        return to

    def setup(self):
        """Steps performed only once at the start of this stage.

        Set this keyword as the Task Setup of the Robot Task corresponding to this stage. Implementation is optional.
        """
        pass

    def teardown(self):
        """Steps performed only once at the end of this stage.

        Set this keyword as the Task Teardown of the Robot Task corresponding to this stage. Implementation is optional.
        """
        pass
