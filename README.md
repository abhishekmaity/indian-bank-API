# Flask based Indian Bank API

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)](https://github.com/abhishekmaity/backend-assignment)
[![PyPI - Python Version](https://img.shields.io/badge/build-flask%201.0.2-green.svg)](https://github.com/abhishekmaity/backend-assignment)
[![PyPI - Python Version](https://img.shields.io/badge/database-SQLite-lightgrey.svg)](https://github.com/abhishekmaity/backend-assignment)

A REST service that can:
1. Given a bank branch IFSC code, get branch details
2. Given a bank name and city, gets details of all branches of the bank in the city

The deployed version can be found at https://bank-query.herokuapp.com/. <br>



For e.g If the IFSC is SBIN0000001, then → https://bank-query.herokuapp.com/ifsc/SBIN0000001 to get details <br>
OR<br>
For e.g If the details of all DENA BANK in MYSORE, then → https://bank-query.herokuapp.com/bank_name/DENA%20BANK/city/MYSORE to get details



