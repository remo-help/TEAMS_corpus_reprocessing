import txt_reprocessor as txt
import argparse
import sys
import os


def start_parser() -> argparse.ArgumentParser:
    if len(sys.argv) == 1: print("Please specify the following arguments:\n --dir: the directory you wish to use")
    parser = argparse.ArgumentParser(description='specify a directory')
    parser.add_argument("--dir", help="The directory where your files are.",
                    required=True)
    parser.add_argument("--outputname", help="The name structure of your outputfiles. All outputfiles will have this appended.",
                    required=False)
    return parser


def main():
    parser = start_parser()
    args = parser.parse_args()
    pass


if __name__ == '__main__':
    main()