*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${error_message}     Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz później.

*** Keywords ***
Log In Wikipedia
    [Arguments]      ${login}      ${password}
    Open Browser      https://pl.wikipedia.org    chrome
    Maximize Browser Window
    Run Keyword And Ignore Error    Click Element    id:nieistniejace
    Wait Until Element Is Visible    id:pt-login-2    5
    Click Element    id:pt-login-2
    Input Text    id:wpName1    ${login}
    Input Password    id:wpPassword1    ${password}
    Click Button    id:wpLoginAttempt
    Sleep    2
*** Test Cases ***
Successful login
    Log In Wikipedia      RobotTests      RobotFramework
    Input Text    name:search   Teoria Wielkiego Podrywu
    Click Button    xpath=/html/body/div[1]/header/div[2]/div/div/div/form/div/button
    Close Browser
Unsuccessful login
    Log In Wikipedia    xxxx    xxxx
    ${my_error_message}    Get Text    xpath=//*[@id="userloginForm"]/form/div[1]/div
    Log    ${my_error_message}
    Log To Console     ${my_error_message}
    Should Be Equal As Strings    ${my_error_message}    ${error_message}
    Close Browser