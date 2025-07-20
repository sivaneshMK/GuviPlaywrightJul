Feature: Login Functionality
  @wip
  Scenario: Successful Login
    Given as a user i am on the login page
    When the user enters valid credentials
    Then the user should be redirected to the dashboard
