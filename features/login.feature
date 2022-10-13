Feature: Login

As a user I wanted to login to the application so that I can purchase products

Scenario: Login with valid credentials
    Given I visit the Sauce Demo website login page
    When I enter valid login credentials
    Then I should see the inventory page


#Scenario Outline: Try to login with invalid credentials
#    Given I visit the Sauce Demo website login page
#    When I enter "<username>" and "<password>"
#    Then I should see an error message
#
#    Examples:
#        | username | password |
#        | fail-1   | fail-1 |
#        | fail-2   | fail-2 |
#        | fail-3   | fail-3 |
