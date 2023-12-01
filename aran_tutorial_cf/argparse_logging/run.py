import argparse
import logging


def get_args():

    return args.parser_args()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='run',
        description="This is a basic tutorial for python libraries",
        epilog='This tutorial is written by Manos Kirtas (eakirtas@csd.auth.gr)'
    )

    parser.add_argument(
        'data_path',
        help='path to data',
        type=str,
        default='./data/',
    )

    parser.add_argument(
        '--log',
        help='logging level',
        choices=['info', 'debug', 'warning', 'error', 'critical'],
        type=str,
        default='WARNING',
    )

    parser.add_argument('--num_points',
                        help='the number of points to generate',
                        type=int,
                        default=50)

    args = parser.parse_args()

    logging.basicConfig(
        format=
        '[LOG-%(levelname)s][%(module)s:%(lineno)d] %(asctime)s -- %(message)s',
        handlers=[logging.StreamHandler()],
        level=getattr(logging, args.log.upper(), None),
    )

    logging.info('This is an info message')
    logging.debug('This is a debug message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical')

    logging.debug(f'Num points: {args.num_points}')
    logging.debug(f'File to export: {args.data_path}')
