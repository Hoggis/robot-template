Robot Template
==============

### Project structure

The project should adhere to the below folder structure. Folders should only contain files of the denoted type(s), following the naming conventions.

    .
    ├── libraries               # For implementing keywords that interact with target systems
    │   ├── SystemALibrary.py
    │   ├── SystemBLibrary.py
    │   └── utils.py
    ├── pipelines               # Declarative-style Jenkins pipelines
    │   ├── Jenkinsfile
    │   └── process.groovy
    ├── resources               # Configuration and other resources
    │   ├── settings.py
    │   ├── settings_helpers.py
    │   └── ???_keywords.resource
    ├── scripts                 # Batch/shell cripts for running setup, tests and the process
    │   └── start.(cmd|sh)
    ├── stages                  # Robot workflow split into stages
    │   ├── Stage0.py
    │   └── StageN.py
    ├── tasks                   # Robot Framework workflows
    │   └── main.robot
    ├── tests                   # Unit tests
    │   └── test_???.py
    ├── .gitignore
    ├── .pylintrc
    ├── .rflintargs
    ├── requirements.txt
    ├── requirements-dev.txt
    ├── requirements-tests.txt
    ├── run.py
    ├── setup.cfg
    ├── setup.py
    └── README.md
