*** Settings ***
Documentation                           This is the test case for Login
Library                                 Selenium2Library
Suite Teardown                          Close All Browsers


*** Variables ***
${username}                             user3
${password}                             user3

*** Test Cases ***
Register through web portal
    [Documentation]                     Tests if user can Log In and view information

    Open homepage
    Login to see user information


*** Keywords ***
Open homepage
    [Documentation]                     User can open homepage

    open browser                        http://0.0.0.0:8080/
    wait until page contains            Demo app

Login to see user information
    [Documentation]                     User can login and logout

    Click Link                          Log In    
    Input text                          username    ${username} 
    Input text                          password    ${password} 
    Click Button                        Log In
    set selenium speed                  1 seconds
    Page Should Not Contain Button      Log In 
    Page Should Contain                 User Information               
    Page Should Contain                 ${username} 
    Page Should Contain                 Log Out
    Click Link                          Log Out



