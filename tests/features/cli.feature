@wip
Feature: Command Line Interface

  Scenario: The CLI is on the binary search path after installation
    Given the "probullstats" application is installed
    When I execute "probullstats --version" in a terminal or shell
    Then its version should be written to stdout
     and it should indicate success to the executing shell
