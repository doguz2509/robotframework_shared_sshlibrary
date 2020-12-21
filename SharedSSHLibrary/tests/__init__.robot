*** Settings ***
Library  BuiltIn
Library  SSHLibrary

Suite Setup  run keywords
...   set global variable  $PROMPT  ${PROMPT}
...   open connection ${HOST}
...   login  ${USER}  ${PASSWORD}

Suite Teardown  close all connections

*** Variables ***
${HOST}
${USER}
${PASSWORD}
${PROMPT}  #

*** Keywords ***
