Feature: Command Line Interface
  As a technical user
  In order to use the functionality of this package before the application interface is built
  I want a way to invoke the package functionality
  so that it produces output in a format I can share with non-technical users
  and those non-techical users can conduct higher level analysis on the data using other tools

  Scenario: The CLI is in the binary search path after installation
    Given the "probullstats" application is installed
     When I execute "probullstats --version" in a terminal or shell
     Then its version should be written to stdout
      And it should indicate success to the executing shell

  Scenario: The package is in the Python module path
    Given the "probullstats" application is installed
     When I execute "python -m probullstats --version" in a terminal or shell
     Then its version should be written to stdout
      And it should indicate success to the executing shell
