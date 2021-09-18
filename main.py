import sys
import argparse

import utility as u

import warnings

def get_parser():
    parser = argparse.ArgumentParser(description="CLI tool to run Olympic models")

    parser.add_argument("-t", "--team",
                        help="Name of the country(default: india)", 
                        default="ind")

    parser.add_argument("-e", "--event", 
                        help="Name of the event(default: hockey)"
                        )

    parser.add_argument("-y", "--year", 
                        help="Which year's prediction do you want(default: 2020)"
                        
                        )

    parser.add_argument("-g", "--gdp",
                        help="GDP of the country in resp. year(default: gdp of ind in 2020)"
                        )

    parser.add_argument("-p", "--population",
                        help="Population of the country")

    parser.add_argument("-ho", "--host",
                        help="If the country that you provided is also the host")

    parser.add_argument("-u", "--unemployment",
                        help="Unemployment rate in the country"
                        )

    parser.add_argument("-hdi", "--hdi",
                        help="Human Development Index in the country"
                        )

    parser.add_argument("-l", "--life-expectancy",
                        help="Life expectancy in that country"
                        )

    parser.add_argument("-cap", "--calorie-animal",
                        help="Calorie from Animal"
                        )

    parser.add_argument("-cpa", "--calorie-plant",
                        help="Calorie from plant"
                        )

    parser.add_argument("-cfp", "--calorie-fat",
                        help="Calorie from fat"
                        )

    parser.add_argument("-cc", "--calorie-carbo",
                        help="Calorie from carbo"
                        )

    parser.add_argument("-cd", "--commu-demo",
                        help="If this country given is Communist or democratic"
                        )

    parser.add_argument("-pt", "--participants",
                        help="No. of participants for the event"
                        )

    return parser

    
def main(argv=None):
    warnings.filterwarnings("ignore")
    parser = get_parser()
    if argv == None:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    args = parser.parse_args(argv[1:])

    team = args.team
    year = args.year
    event = args.event
    gdp = args.gdp
    population = args.population
    host = args.host
    unemployment = args.unemployment
    hdi = args.hdi
    life_expectancy = args.life_expectancy
    cal_an = args.calorie_animal
    cal_pl = args.calorie_plant
    cal_f = args.calorie_fat
    cal_carbo = args.calorie_carbo
    c_d = args.commu_demo
    parti = args.participants

    model = u.run_model(event)
    # Input format to the model is of type: 
    # GDP, Population, Host Country, Unemployment Rate, HDI, life-exp, Cal-anim, Cal-plan, Cal-fat, Comm./Dem. participant, 
    inp = [gdp, population, host, unemployment, hdi, life_expectancy, cal_an, cal_pl, cal_f, cal_carbo, c_d, parti]
    result = u.predict_model(model, inp)

    res = {
        0: "Nothing",
        1: "Bronze",
        3: "Silver",
        5: "Gold",
        4: "Silver anr Bronze",
        6: "Bronze and Gold",
        8: "Silver and Gold",
        9: "Gold, Silver and Bronze"
    }
    print(f"{team} will win {res[result[0]]} in {event} in {year}")


if __name__ == "__main__":
    main(sys.argv)
