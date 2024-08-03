Feature: Collate Data
  As a bull owner
  In order to make data driven decisions for my business
  I want to be able to retrieve data about bulls and events
  so that I can perform higher level analysis on the raw data

  Scenario: All events in a date range
    Given a start date and end date
    When I request data about events
    Then I am returned a list of events that occurred between those dates (inclusive)
     And the meta information for each event

  Scenario: All bulls at an event
    Given the information that identifies one or more events
    When I request data about the bulls at those events
    Then I am returned a list of events with the bull roster for each event
     And the meta information for each bull

  Scenario: All outs at an event
    Given the information that identifies one or more events
     When I request data about all the outs for bulls at those events
     Then I am returned a list of events with the list of outs for each event
      And the meta information for each out
