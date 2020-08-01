import argparse
import pathlib
import random


def get_args():

    args = argparse.ArgumentParser(
        description='Random shuffling of word between extreme letters',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    args.add_argument(
        '-s', '--seed', default=1, type=int,
        metavar='Seed',
        help='Set the seed value here for reproducibility')

    args.add_argument(
        'text', type=str,
        metavar='TEXT/PATH',
        help='Put your text or path of file to be jumbled')

    parsers = args.parse_args()
    return parsers


def scrambler():

    arg_found = get_args()
    if_file = pathlib.Path(arg_found.text).is_file()

    if if_file:
        with open(arg_found.text) as file_ptr:
            data = file_ptr.read().split()
        print(data)
    else:
        data = arg_found.text.split(' ')

    all_data = list()
    for items in data:
        if len(items) >= 4:
            nt = list(items)[1:-1]
            random.seed(arg_found.seed)
            random.shuffle(nt)
            items = ''.join(
                [items[0]] + nt + [items[-1]])
        all_data.append(items)
    return ' '.join(all_data)


if __name__ == '__main__':
    print(scrambler())
