import argparse
import sys
import re


def read_in(file,encoding="utf-8"):
   f = open(file, encoding=encoding)
   file = f.read()
   f.close()
   file = file.split("\n")
   return file

def find_labels(LIST):
    for i in LIST:
        re.search()


def main():
    if len(sys.argv) == 1: print("Please specify the following arguments:\n  --ext: the extractions file")
    parser = argparse.ArgumentParser(description='specify --ext')
    parser.add_argument("--ext",
                        help="The file where your Odin extractions are, these should be a result of the ASIST Dialog agent.",
                        required=True)
    parser.add_argument("--enc",
                        help="The encoding of your extraction file, default = utf-8",
                        required=False)
    args = parser.parse_args()

    if args.enc:
        extraction_file = read_in(args.ext,args.enc)
    else:
        extraction_file = read_in(args.ext)

        print(extraction_file[0:5])








if __name__ == '__main__':
    main()