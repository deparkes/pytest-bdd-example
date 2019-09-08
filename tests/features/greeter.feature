Feature: Greeter
   Class to greet the user
   
Scenario: A simple greeter
    Given a Greeter
    When I give my name as "George"
    Then The greeter says Hello "George"