import argparse
import sys
import re
from collections import Counter


def read_in(file,encoding="utf-8"):
   f = open(file, encoding=encoding)
   file = f.read()
   f.close()
   #file = file.split("\n")
   return file

def find_labels(STRING):
    #pattern1 = re.compile(r'labels":\["([A-Z][a-z]*)",|"labels\\":\[\\"([A-Z][a-z]*)\\",')
    pattern1 = re.compile(r'labels":\["([A-Z][a-z]*)"',re.IGNORECASE)
   # pattern1= '(\"labels\":[\"([A-Z][a-z]*)\",)|\"labels\\\":[\\\"([A-Z][a-z]*)\\\",'

    #for match in pattern1.finditer(STRING):
        #print(match.group(1))
        #print(match.group(2))
    #if re.findall(pattern1,STRING):
        #return [match.groups() for match in pattern1.finditer(STRING)]

    return re.findall(pattern1,STRING)



def main():
    if len(sys.argv) == 1: print("Please specify the following arguments:\n  --ext: the extractions file")
    parser = argparse.ArgumentParser(description='specify --ext')
    parser.add_argument("--ext",
                        help="The file where your Odin extractions are, these should be a result of the ASIST Dialog agent.",
                        required=True)
    parser.add_argument("--enc",
                        help="The encoding of your extraction file, default = utf-8",
                        required=False)
    parser.add_argument("--out",
                        help="The name of the outputfile",
                        required=False)
    args = parser.parse_args()
    c = Counter()
    if args.enc:
        extraction_file = read_in(args.ext,args.enc)
    else:
        extraction_file = read_in(args.ext)
        labels = find_labels(extraction_file)
        print(labels)
        c.update(labels)
        print(c)

    if args.out:
        pass
    else:
        file = open("label_statistics.txt", "w+", encoding='utf-8')
        for item in c:
            file.write(item)
            file.write(":"+str(c[item]))
            file.write("\n")



        #print(extraction_file[0:5])








if __name__ == '__main__':
    main()


