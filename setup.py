from setuptools import setup

setup(
    name                          = 'CasaBourseScraper',
    version                       = '0.1.0',
    author                        = 'BEL-LAHCEN Brahim',
    author_email                  = 'brahimbellahcen@outlook.com',
    packages                      = ['CasaBourseScraper', 'CasaBourseScraper.test'],
    url                           = 'https://github.com/brahimmade/Casa_Bourse_Scraper',
    license                       = 'LICENSE.txt',
    description                   = 'Python library to scrape financial data from the Casablanca Stock Exchange',
    long_description_content_type = 'text/markdown',
    long_description              = open('README.txt').read(),
    keywords                      = ['Web scrapping','Casablanca Stock Exchange', 'MASI'],
    install_requires              = [],
)