import sys
import argparse

import pickle
import pandas as pd

import utility as u

def get_parser():
    parser = argparse.ArgumentParser(description="CLI tool to run Olympic models")

    parser.add_argument("-t", "--team",
                        nargs='+',
                        help="Name of the country(default: india)", 
                        default="ind")

    parser.add_argument("-e", "--event", 
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

    parser.add_argument("-ho", "--host", nargs='+')

    parser.add_argument("-u", "--unemployment", nargs='+')

    parser.add_argument("-hdi", "--hdi", nargs='+')

    parser.add_argument("-l", "--life-expectancy", nargs='+')

    parser.add_argument("-cap", "--calorie-animal", nargs='+')

    parser.add_argument("-cpa", "--calorie-plant", nargs='+')

    parser.add_argument("-cfp", "--calorie-fat", nargs='+')

    parser.add_argument("-cc", "--calorie-carbo", nargs='+')

    parser.add_argument("-cd", "--commu-demo", nargs='+')

    parser.add_argument("-pt", "--participants", nargs='+')

    return parser

    
def main(argv=None):
    parser = get_parser()
    if len(argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    args = parser.parse_args(argv)

    model = u.model_name(args.event)
    # Input format to the model is of type: 
    # GDP, Population, Host Country, Unemployment Rate, HDI, life-exp, Cal-anim, Cal-plan, Cal-fat, Comm./Dem. participant, 
    inp = []
    result = u.model_name(model, inp)



