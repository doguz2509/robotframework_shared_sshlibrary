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