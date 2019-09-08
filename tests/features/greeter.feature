Feature: Greeter
   Class to greet the user

Scenario Outline: A simple greeter
    Given a Greeter
    When I give my name as "<name>"
    Then The greeter says Hello "<name>"
  Examples: Names
    | name |
    | George |
    | Sarah |
    | Tim |