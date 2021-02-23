Feature: search for topics at python.org

Scenario Outline: Verify a number of results for search topic
   Given we have a web site at python.org
    When we search for a "<topic>"
     And we parse the resulting page
    Then we get at least <number> of responses
     And the word "<topic>" appears on the page

   Examples: Search topics
   | topic   | number   |
   | pycon   | 3        |
   | version | 8        |
