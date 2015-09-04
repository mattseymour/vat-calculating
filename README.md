## Tax calculating

A simple script to aid in the adding and removing of tax.


### Usage

 - Add vat to amount (10) `vat.py add 10`
 - Remove vat from amount (20) `vat.py remove 20`
 - Change vat amount (30% vat) `vat.py --vat 30 add 40`

### Example

    > python vat.py remove 6.99
    Removing VAT:
    Price inc tax: 6.99
    Tax paid at 20.0%: 1.17
    Price exl tax: 5.83
