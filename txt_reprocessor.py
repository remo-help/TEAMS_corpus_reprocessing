import pandas as pd
import argparse
import sys
import json
import pickle

def write_txt(lines: list,filename: str):
    writefile= open(filename, "w", encoding='utf-8')
    for line in lines:
        if lines.index(line) == len(lines)-1:
            writefile.write(line)
        else:
            writefile.write(line)
            writefile.write("\n")

#using this to convert a string argument to a boolean
def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def start_parser() -> argparse.ArgumentParser:
    if len(sys.argv) == 1: print("Please specify the following arguments:\n --file: the inputfile (TEAMS corpus.xls file) "
                                 "\n --outputfile: The name of your outputfile. If called with --file only, then this will yield utterances per line. If called with --json and --file, then this will yield a JSON file")
    parser = argparse.ArgumentParser(description='specify a --file argument for your inputfile')
    parser.add_argument("--file", help="The file excel transcript file you wish to process",
                        required=False)
    parser.add_argument("--outputfile", help="The name of your outputfile. If called with --file only, then this will yield utterances per line. If called with --json and --file, then this will yield a JSON file",
                        required=False)
    parser.add_argument("--json", help="The JSN file containing DialogAgent Extractions",
                        required=False)
    parser.add_argument("--pickle", help="Parameter for the output type of your --outputfile if --json is called. If True, the output will be a pickle file, "
                                         "if False, the output will be a JSON textfile."
                                         "Default: True",
                        required=False, default=True, type=str2bool)
    return parser


def txt_single(inputfile: str, outputfile: str=None):
    caption_list = []
    utterance_list = []
    file = pd.read_excel(inputfile)
    print(f"working on {inputfile}")
    for i in file.index:
        timestamp_start= float(file['Timestamp_Start'][i])
        timestamp_end= float(file['Timestamp_End'][i])
        caption = {'Speaker':file['Speaker_Role'][i],'Timestamp':(timestamp_start,timestamp_end),'Utterance':file['Utterance'][i],'Team_ID':file['TeamID'][i]}
        caption_list.append(caption)
        utterance_list.append(str(caption['Utterance']))
    if outputfile:
        write_txt(utterance_list,outputfile)
        print(caption_list[len(caption_list)-1])
    else:
        return caption_list

def import_extractions(inputfile: str,jsonfile: str,outputfile: str,pickling: bool=True):
    captions = txt_single(inputfile=inputfile)
    try:
        with open(jsonfile) as f:
            extractions = json.load(f)
    except:
        extractions=[]
        f = open(jsonfile, 'r')
        file = f.read()
        f.close()
        linefile = file.split("\n")
        for line in linefile:
            try:
                extractions.append(json.loads(line))
            except:
                pass

    if captions[0]["Utterance"] == extractions[0]["data"]["text"]:
        print("Your --json file and your inputfile (--file) are compatible")
    else:
        raise Exception("Your --json file and your inputfile (--file) do not cover the same text")

    for i in range(0,len(captions)):
        captions[i]["Extractions"] = extractions[i]["data"]["extractions"]

    if pickling is True:
        with open(outputfile, 'wb') as fh:
            pickle.dump(captions, fh)
        print("Pickle file created successfully")
    elif pickling is False:
        with open(outputfile, 'w') as fh:
            for caption in captions:
                fh.write(str(caption))
                fh.write("\n")
        print("JSON output file created successfully")



def main():
    parser = start_parser()
    args = parser.parse_args()  # returns data from the options specified (echo
    print("You chose --file:", args.file)
    if args.file and args.outputfile and not args.json:
        txt_single(inputfile=args.file,outputfile=args.outputfile)
    elif args.file and args.json and args.outputfile:
        import_extractions(inputfile=args.file,outputfile=args.outputfile,jsonfile=args.json,pickling=args.pickle)







if __name__ == '__main__':
    main()

