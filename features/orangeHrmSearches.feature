Feature: Login

As a user I wanted to login to the application so that I can purchase products

    Background: Common steps
        Given I have successfully logged in to the Orange HRM website

Scenario: Standard search
    When I navigate to the search page
    Then the search page is displayed


Scenario: Advanced search
    When I navigate to the advanced search page
    Then the advanced search page is displayed

