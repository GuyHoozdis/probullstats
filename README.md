# ProBullStats Data Engine

This is the `probullstats` package.  An engine to pull data from the [ProBullStats
website][probullstats-website] so that it can be collated with other relevant data and put into a
common format. Then clients can use that data for any analysis or research they wish to pursue.


## !!! IMPORTANT !!!

Data Access Requires a Subscription.

1. This module does not grant the user with any rights to access the curated data in the [ProBullStats
database][probullstats-database].
1. Data access requires a [subscription][probullstats-subscription] level that grants the rights to
generate and use API keys to access the site's data.  See the website's [service terms
here][probullstats-subscription].
1. The author of this package is not affiliated with the ProBullStats website.

## Quickstart

Install the package into you desired environment.
```
$ pip install probullstats
```

Display the CLI usage and options.
```
$ probullstats --help
```

**NOTE**: If you install the package into a virtual environment, then the CLI will only be available when that environment is active.



[probullstats-website]: https://probullstats.com
[probullstats-database]: https://probullstats.com/statstats.php
[probullstats-subscription]: https://probullstats.com/terms.php
[ubcotx-github]: https://github.com/ubcotx
[ubcotx-website]: https://ubcotx.com/
