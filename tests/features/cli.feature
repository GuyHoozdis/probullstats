@wip
Feature: Command Line Interface

  Scenario: The CLI is on the binary search path after installation
    Given the "<application>" application is installed
    When I execute "<application> --help" in a terminal or shell
    Then I the application's usage is written to stdout
