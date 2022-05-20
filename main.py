# importing required modules 
import argparse 

def obtain_args(): 
    # create a parser object
    parser = argparse.ArgumentParser(description = "An addition program")

    # add argument
    parser.add_argument("team", nargs = 1, metavar = "team", type = str,
                        help = "The team of package that you want to search")

    # parse the arguments from standard input
    args = parser.parse_args()
    
    # check if add argument has any input data.
    # If it has, then print sum of the given numbers
    if len(args.team) != 0:
        print(args.team)