Feature: Collate Data
  As a bull owner
  In order to make data driven decisions for my business
  I want to be able to retrieve data about bulls and events
  so that I can perform higher level analysis on the raw data

  @wip
  Scenario: All events in a date range
    Given the following arguments
      | command line arguments |
      | --after 2023-01-01 --before 2024-01-01 |
    When I request data about those "events"
    Then I am returned a list of events
     And the meta information for each event

  Scenario: All bulls at an event
    Given the following arguments
      | command line arguments |
      | --after 2023-01-01 --before 2024-01-01 --bull-roster |
    When I request data about those "events"
    Then I am returned a list of events with the bull roster for each event
     And the meta information for each bull

  Scenario: All outs at an event
    Given the following arguments
      | command line arguments |
      | --after 2023-01-01 --before 2024-01-01 --with-outs |
    When I request data about those "events"
    Then I am returned a list of events with the list of outs for each event
     And the meta information for each out
