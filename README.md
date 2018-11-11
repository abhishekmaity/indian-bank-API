# Flask based Indian Bank API

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)](https://github.com/abhishekmaity/backend-assignment)
[![PyPI - Python Version](https://img.shields.io/badge/build-flask%201.0.2-green.svg)](https://github.com/abhishekmaity/backend-assignment)
[![PyPI - Python Version](https://img.shields.io/badge/database-SQLite-lightgrey.svg)](https://github.com/abhishekmaity/backend-assignment)

A REST service that can:
1. Given a bank branch IFSC code, get branch details
2. Given a bank name and city, gets details of all branches of the bank in the city

The deployed version can be found at https://bank-query.herokuapp.com/. <br>



For e.g<br>
If the IFSC is SBIN0000001, then → https://bank-query.herokuapp.com/ifsc/SBIN0000001
``` bash
[["SBIN0000001", "1", "KOLKATA MAIN", "SAMRIDDHI BHAWAN, 1 STRAND ROAD, KOLKATA 700 001", "KOLKATA", "KOLKATA", "WEST BENGAL", "STATE BANK OF INDIA"]]
```
To get DENA BANK in MYSORE, then → [https://bank-query.herokuapp.com/bank_name/DENA BANK/city/MYSORE](https://bank-query.herokuapp.com/bank_name/DENA%20BANK/city/MYSORE)
``` bash
[["BKDN0610536", "25", "MYSORE", "618,CHAMRAJA DROAD,PBNO205,MYSORE570024", "MYSORE", "MYSORE", "KARNATAKA", "DENA BANK"], ["BKDN0611872", "25", "RAMAKRISHNA NAGAR MYSROE", "DARSHANA NO 10 VASU LAYOUT RAMAKRISHNA NAGAR VISWAMANAVA DOUBLE ROAD MYSORE 570022", "MYSORE", "MYSORE", "KARNATAKA", "DENA BANK"]]
```

