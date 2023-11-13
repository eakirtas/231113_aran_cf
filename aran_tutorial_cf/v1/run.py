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
        '--log',
        help='logging level',
        choices=['info', 'debug', 'warning', 'error', 'critical'],
        type=str,
        default='WARNING',
    )

    args = parser.parse_args()

    logging.basicConfig(
        format=
        '[LOG-%(levelname)s][%(module)s:%(lineno)d] %(asctime)s -- %(message)s',
        handlers=[logging.StreamHandler()],
        level=getattr(logging, args.log.upper(), None),
    )

    logging.info('Welcome to AR.AN tutorial')
    logging.debug('Welcome to AR.AN tutorial')
    logging.warning('Welcome to AR.AN tutorial')
    logging.error('Welcome to AR.AN tutorial')
    logging.critical('Welcome to AR.AN tutorial')
