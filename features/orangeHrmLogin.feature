Feature: Login

As a user I wanted to login to the application so that I can purchase products

Scenario: Login with valid credentials
    Given I launch a Chrome browser
    When I navigate to the Orange HRM homepage
    And I enter username "Admin" and password "admin123"
    And I click on the login button
    Then user is successfully logged in to the dashboard page

