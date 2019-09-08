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


Scenario: No name provided
  Given a Greeter
  When I don't provide a name
  Then the greeter says "Please provide a name"