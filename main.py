import sys
import argparse

import pandas as pd

parser = argparse.ArgumentParser(description="CLI tool to run Olympic models")

parser.add_argument("-t", "--team",
                    nargs='+',
                    help="Name of the country(default: india)", 
                    default="ind")

parser.add_argument("-e", "--event", 
                    nargs='+',
                    help="Name of the event(default: hockey)"
                    )

parser.add_argument("-y", "--year", 
                    nargs='+',
                    help="Which year's prediction do you want(default: 2020)"
                    
                    )

parser.add_argument("-g", "--gdp", nargs='+',
                    help="GDP of the country in resp. year(default: gdp of ind in 2020)"
                    )

parser.add_argument("-p", "--population", nargs='+')

parser.add_argument("-h", "--host", nargs='+')

parser.add_argument("-u", "--unemployment", nargs='+')

parser.add_argument("-hdi", "--hdi", nargs='+')

parser.add_argument("-l", "--life-expectancy", nargs='+')

parser.add_argument("-cap", "--calorie-animal", nargs='+')

parser.add_argument("-cpa", "--calorie-plant", nargs='+')

parser.add_argument("-cfp", "--calorie-fat", nargs='+')

parser.add_argument("-cc", "--calorie-carbo", nargs='+')

parser.add_argument("-cd", "--commu-demo", nargs='+')

parser.add_argument("-pt", "--participants", nargs='+')



if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args=parser.parse_args()

if args.
