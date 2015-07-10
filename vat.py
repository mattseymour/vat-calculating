#! /usr/bin/env python
from __future__ import print_function

import sys
import argparse

def remove_vat(price, vat):
    """
    Returns price exluding vat, and vat amount
    """
    price_ex_vat = price / ((vat / 100) + 1)
    vat_paid = price - price_ex_vat
    return price_ex_vat, vat_paid


def add_vat(price, vat):
    """
    Returns price including vat amount, and vat amount
    """
    vat_paid = price * (vat/100)
    return price + vat_paid, vat_paid


if __name__ == '__main__':
    class MyParser(argparse.ArgumentParser):
        def error(self, message):
            sys.stderr.write('error: %s\n' % message)
            self.print_help()
            sys.exit(2)

    parser = MyParser(
        prog='Vat calculator',
        description='calculating vat.'
    )
    parser.add_argument(
        '--vat',
        help='Set a tax amount. Default vat amount 20%%',
        nargs='?',
        default=float(20),
        type=float
    )

    subparsers = parser.add_subparsers(help='sub-command help', dest='command')
    rm_sub = subparsers.add_parser('remove', help='Subtract VAT')
    rm_sub.add_argument('amount', type=float, help='Amount')
    add_group = subparsers.add_parser('add', help='Add VAT')
    add_group.add_argument('amount', type=float, help='an amount')

    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    def print_remove_vat(amount, vat_percentage):
        price_ex, vat = remove_vat(amount, vat=vat_percentage)
        print('Removing VAT:')
        print('Price inc tax: {0:.2f}'.format(amount))
        print('Tax paid at {0}%: {1:.2f}'.format(vat_percentage, vat))
        print('Price exl tax: {0:.2f}'.format(price_ex))

    def print_add_vat(amount, vat_percentage):
        price_inc, vat = add_vat(args.amount, vat=args.vat)
        print('Adding VAT:')
        print('Price exl tax: {0:.2f}'.format(args.amount))
        print('Tax paid at {0:.2f}%: {1:.2f}'.format(args.vat, vat))
        print('Price inc tax: {0:.2f}'.format(price_inc))

    if args.command == 'remove':
        print_remove_vat(args.amount, args.vat)
    elif args.command == 'add':
        print_add_vat(args.amount, vat=args.vat)
