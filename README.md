<div id="top"></div>



<!-- PROJECT LOGO -->
<br />
<div align="center">
	<a href="https://github.com/brahimmade/Casa_Bourse_Scraper">
		<img src="images/casabourse.png" alt="Logo" width="100" height="120">
	</a>
	<h3 align="center">Casa Bourse Scraper</h3>
	<p align="center">
		Obtenir l'accès simplifié aux données de la Bourse de Casablanca.  
	</p>
</div>


<div align="center">

[![Language](https://img.shields.io/badge/Language-Python-green?style)](https://github.com/brahimmade)
[![PyPI](https://img.shields.io/pypi/v/StocksMA)]()
[![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flatcolor=BC4E99)](https://github.com/brahimmade/Casa_Bourse_Scraper)

</div>

## CasaBourseScraper

CasaBourseScraper is a package to simplify the access to financial and economic data of Moroccan stocks. It tries to present potentially useful and interesting information.

The package include functions to grab informations about all stocks form [casablanca-bourse](https://www.casablanca-bourse.com/bourseweb/index.aspx?aspxerrorpath=/bourseweb/bourseweb/index.aspx) & allows the user to download historical and intraday data from all the shares traded on Casablanca Stock Exchange.

> Note: Sometimes, some functions may fail to get the data from some sources due to WAF protection.


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* [Python3](https://www.python.org/)

### Installation

```bash
$ pip install CasaBourseScraper
```

## Usage

  - [Import the package](#import-the-package)
  - [Get all availabale tickers](#get-all-availabale-tickers)

  
### Import the package

```python
>> import CasaBourseScraper as cbs
```

### Get all availabale tickers
Show available tickers with the full name of the company
**Example**:
```python
cbs.get_tickers()
```
