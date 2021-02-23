Feature: simple example

Scenario: generate a random number
   Given  we have loaded a random number generator
    When  we ask for a random integer between 1 and 20
    Then  we get an integer between 1 and 20

Scenario: generate a negative random number
   Given  we have loaded a random number generator
    When  we ask for a random integer between -100 and -20
    Then  we get an integer between -100 and -20

Scenario Outline: generate a positive random number
   Given  we have loaded a random number generator
    When  we ask for a random integer between <low> and <high>
    Then  we get an integer between <low> and <high>

   Examples: Positive Integers
    | low   | high   |
    | 12    | 45     |
    | 1111  | 1234   |
    | 2111  | 2234   |
    | 3111  | 3234   |