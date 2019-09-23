#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program calculates cost of a pizza

import constants


def main():
    # input
    diameter = int(input("please enter the diameter of the pizza that you" +
                         " would like to order (inch): "))

    # process
    sub_total = constants.LABOR + constants.RENT + \
        (constants.MATERIAL * diameter)
    total = sub_total + (sub_total * constants.HST)

    # output
    print("the cost for a {0} inch pizza is ${1:,.2f}"
          .format(diameter, total))


if __name__ == "__main__":
    main()
