""" = Shared SSHLibrary are premodifier for SSHLibrary
Allowing share connection registry over multiple TestSuites using SSHLibrary

= Usage:
    Add premodifier to robot command line:
    --premodifier SharedSSHLibrary

Example:
    Main suite folder
    __init__.robot
    *** Settings ***
    Library  BuiltIn
    Library  SSHLibrary

    Suite Setup  run keywords
    ...   open connection ${HOST}
    ...   login  ${USER}  ${PASSWORD}

    Suite Teardown  close connections

    *** Variables ***
    ${HOST}
    ${USER}
    ${PASSWORD}

    Suite1.robot
    *** Settings ***
    Library  SSHLibrary

    *** Test Cases ***
    Test 1.1
        ${stdout}=  execute command  ls -l ~/
        should not empty  ${stdout}  No content found

    Test 1.2
        start command  ls -l ~/
        ${stdout}=  read until  #
        should not empty  ${stdout}  No content found

    Suite1.robot
    *** Settings ***
    Library  SSHLibrary

    *** Test Cases ***
    Test 2.1
        ${stdout}=  execute command  du -h ~/
        should not empty  ${stdout}  No content found

    Test 2.2
        start command  du -h ~/
        ${stdout}=  read until  #
        should not empty  ${stdout}  No content found
"""