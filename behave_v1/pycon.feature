Feature: search for topics at python.org

Scenario Outline: generate a positive random number
   Given  we have navigated to python.org
    When  we search for "<topic>"
    Then  we get at least <number> of responses

   Examples: Search Topics
    | topic   | number   |
    | pycon   | 3        |
    | max     | 8        |
