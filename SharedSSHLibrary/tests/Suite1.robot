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