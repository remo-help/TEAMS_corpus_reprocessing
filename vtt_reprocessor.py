import pandas as pd
import os
import argparse
import sys
from webvtt import WebVTT, Caption


def main():
    if len(sys.argv) == 1: print("Please specify the following arguments:\n --dir: the directory you wish to use")
    parser = argparse.ArgumentParser(description='specify a directory')
    parser.add_argument("--dir", help="The directory where your files are, if this is the directory, try \"here\"",
                        required=True)
    parser.add_argument("--filename", help="The name of your file, if no option is chosen this defaults to \"writefile\"",
                        required=False)
    parser.add_argument("--vtt",
                        help="Which vtt mode, default is webvtt, options are \"web\" and \"classic\"",
                        required=False)
    args = parser.parse_args()  # returns data from the options specified (echo
    print("You chose directory:", args.dir)
    if args.dir == 'here':
        args.dir = os.path.dirname(os.path.realpath(__file__))

    if args.filename:
        writefile = open(args.filename+".vtt", "w+", encoding='utf-8')
        writefile.write("WEBVTT\n\n")
    else:
        writefile = open("writefile.vtt", "w+", encoding='utf-8')
        writefile.write("WEBVTT\n\n")

    directory = args.dir

    def vtt():
        for entry in os.scandir(directory):
            if (entry.path.endswith(".xls")) and entry.is_file():
                file = pd.read_excel(entry.path)
                vtt = WebVTT()
                for i in file.index:
                    caption = Caption(
                        '00:00:00.000',
                        '00:00:00.000',
                        str(file['Utterance'][i])
                    )
                    vtt.captions.append(caption)
        vtt.save('my_captions.vtt')


    def classic():
        for entry in os.scandir(directory):
            if (entry.path.endswith(".xls")) and entry.is_file():
                file = pd.read_excel(entry.path)
                for i in file.index:
                    writefile.write(str(i+1))
                    writefile.write("\n")
                    writefile.write("00:00:")
                    writefile.write(str(file['Timestamp_Start'][i]))
                    writefile.write(" --> ")
                    writefile.write("00:00:")
                    writefile.write(str(file['Timestamp_End'][i]))
                    writefile.write("\n")
                    writefile.write(str(file['Speaker_Role'][i])+': ')
                    writefile.write(str(file['Utterance'][i]))
                    writefile.write("\n")
                    writefile.write("\n")
            #utterances = file['Utterance']
            #print(utterances[0:5])
            #for utterance in utterances:
            #    writefile.write(str(utterance))
            #    writefile.write("\n")
        writefile.close()

    if args.vtt == "web":
        vtt()
    elif args.vtt == "classic":
        classic()
    else:
        vtt()

if __name__ == '__main__':
    main()

