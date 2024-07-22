@wip
Feature: Command Line Interface

  Scenario: The CLI is on the binary search path after installation
    Given the "ProBullStats" application is installed
    When I execute "probullstats --help" in a terminal or shell
    Then its usage should be written to stdout
     and it should indicate success to the executing shell
