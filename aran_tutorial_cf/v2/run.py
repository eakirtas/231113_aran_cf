import argparse
import logging

from aran_tutorial_cf.v2.generate import generete_data_at, load_data


def get_args():

    return args.parser_args()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='run',
        description="This is a basic tutorial for python libraries",
        epilog='This tutorial is written by Manos Kirtas (eakirtas@csd.auth.gr)'
    )

    parser.add_argument(
        '--log',
        help='logging level',
        choices=['info', 'debug', 'warning', 'error', 'critical'],
        type=str,
        default='WARNING',
    )

    parser.add_argument(
        'data_path',
        help='path to data',
        type=str,
        default='./data/',
    )

    parser.add_argument('--num_points',
                        help='the number of points to generate',
                        type=int,
                        default=50)

    parser.add_argument('--function',
                        help='use function to generate data',
                        type=str,
                        choices=['x', 'f_x', 'g_x', 'h_x'],
                        default=['x', 'f_x', 'g_x', 'h_x'],
                        nargs='+')

    parser.add_argument("--generate",
                        "-g",
                        help='generate data',
                        default=False,
                        action='store_true')

    parser.add_argument("--load",
                        "-l",
                        help='loads data',
                        default=False,
                        action='store_true')

    args = parser.parse_args()

    logging.basicConfig(
        format=
        '[LOG-%(levelname)s][%(module)s:%(lineno)d] %(asctime)s -- %(message)s',
        handlers=[logging.StreamHandler()],
        level=getattr(logging, args.log.upper(), None),
    )

    if args.generate:
        generete_data_at(args.data_path, args.num_points, args.function)
    if args.load:
        load_data(args.data_path, args.function)
