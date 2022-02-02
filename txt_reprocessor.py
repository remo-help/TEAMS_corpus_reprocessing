import pandas as pd
import os
import argparse
import sys


def write_txt(lines:list,filename:str):
    writefile= open(filename, "w+", encoding='utf-8')
    for line in lines:
        if line == lines[-1]:
            writefile.write(line)
        else:
            writefile.write(line)
            writefile.write("\n")




def main():
    if len(sys.argv) == 1: print("Please specify the following arguments:\n --dir: the directory you wish to use")
    parser = argparse.ArgumentParser(description='specify a directory')
    parser.add_argument("--dir", help="The directory where your files are, if this is the directory, try \"here\"",
                        required=True)
    parser.add_argument("--filename", help="The name of your file",
                        required=True)
    parser.add_argument("--vtt",
                        help="Which vtt mode, default is webvtt, options are \"web\" and \"classic\"",
                        required=False)
    args = parser.parse_args()  # returns data from the options specified (echo
    print("You chose directory:", args.dir)
    if args.dir == 'here':
        args.dir = os.path.dirname(os.path.realpath(__file__))

    directory = args.dir

    def txt():
        caption_list = []
        utterance_list = []
        for entry in os.scandir(directory):
            if (entry.path.endswith(".xls")) and entry.is_file():
                file = pd.read_excel(entry.path)
                print(str(entry.path))
                for i in file.index:
                    timestamp_start= float(file['Timestamp_Start'][i])
                    timestamp_end= float(file['Timestamp_End'][i])
                    caption = {'Speaker':file['Speaker_Role'][i],'Timestamp':(timestamp_start,timestamp_end),'Utterance':file['Utterance'][i],'Team_ID':file['TeamID'][i]}
                    caption_list.append(caption)
                    utterance_list.append(str(caption['Utterance']))
        write_txt(utterance_list,args.filename)
        print(len(caption_list))



    if args.vtt == "txt":
        txt()


if __name__ == '__main__':
    main()

