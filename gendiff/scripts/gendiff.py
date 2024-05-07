import argparse
from gendiff.src import gendiff

def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    
    # parser.name - ? 

    parser.add_argument('filepath1')
    parser.add_argument('filepath2')
    parser.add_argument('-f', '--format', help='set format of output')
    
    # parser.version - ? 

    # ToDo
    # diff = gendiff(
    #     parser.parse_args()[0],
    #     parser.parse_args()[1],
    #     opts?
    # )
    # print(diff)

if __name__ == '__main__':
    main()