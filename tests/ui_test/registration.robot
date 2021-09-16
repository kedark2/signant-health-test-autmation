*** Settings ***
Documentation                           This is the test case for Registration
Library                                 Selenium2Library
Suite Teardown                          Close All Browsers

*** Variables ***
${username}                             user3
${password}                             user3
${firstname}                            First Name
${lastname}                             Lastname
${phone}                                12345


*** Test Cases ***
Register through web portal
    [Documentation]                     Tests if registration can be done

    Open homepage
    Register a user

*** Keywords ***

Open homepage
    [Documentation]                     User can open homepage

    open browser                        http://0.0.0.0:8080/
    wait until page contains            Demo app

Register a user
    [Documentation]                     New user can be registered

    set selenium speed                  1 seconds
    Click Link                          Register    
    Input text                          username    ${username} 
    Input text                          password    ${password} 
    Input text                          firstname   ${firstname} 
    Input text                          lastname    ${lastname} 
    Input text                          phone       ${phone} 
    Click Button                        Register
    Page Should Not Contain Button      Register                 
