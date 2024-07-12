#! /usr/bin/python3

import argparse

# intialize parser
parser=argparse.ArgumentParser()
parser.add_argument("n",help="Number you want to get factorial from",type=int)
parser.add_argument('-v',"--verbose",action="store_true",help="Increase output verbosity")

args=parser.parse_args()

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num -1)

result=factorial(args.n)
if args.verbose:
    print(f"factorial of {args.n} is equal to: {result}")
else:
    print(result)