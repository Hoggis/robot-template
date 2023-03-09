*** Settings ***
Variables         ../resources/settings.py    ${env}
Library           TOSLibrary    ${db_server}    ${db_name}
...               ${DB_CRED_USR}    ${DB_CRED_PSW}    ${db_auth_source}
Library           ../libraries/ExampleLibrary.py
Library           ../stages/Stage0.py
Library           ../stages/Stage1.py
Library           ../stages/Stage2.py

*** Test Cases ***
Producer stage
    [Tags]    stage_0
    [Setup]    Stage0.Setup
    [Documentation]    This is the producer stage
    Stage0.Main Loop
    [Teardown]    Stage0.Teardown

Consumer stage
    [Tags]    stage_1
    [Setup]    Stage1.Setup
    [Documentation]    This is the first consumer stage
    Stage1.Main Loop
    [Teardown]    Stage1.Teardown

Consumer stage 2
    [Tags]    stage_2
    [Setup]    Stage2.Setup
    [Documentation]    This is the 2nd consumer stage
    Stage2.Main Loop
    [Teardown]    Stage2.Teardown
