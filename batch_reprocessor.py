import txt_reprocessor as txt
import argparse
import sys
import os
from unipath import Path


def start_parser() -> argparse.ArgumentParser:
    if len(sys.argv) == 1: print("Please specify the following arguments:\n --dir: the directory you wish to use")
    parser = argparse.ArgumentParser(description='specify a directory')
    parser.add_argument("--dir", help="The directory where your files are.",
                    required=True)
    parser.add_argument("--pickle",
                       help="Parameter for the output type of your outputfiles. If True, the output will be a pickle file, "
                            "if False, the output will be a JSON textfile."
                            "Default: True",
                       required=False, default=True, type=txt.str2bool)
    parser.add_argument("--tomcatdir",
                        help="The location of your ASIST DialogAgent. If you do not have the ASIST DialogAgent, call \'git clone https://github.com/remo-help/tomcat-text.git\' .",
                        required=True, type=str)
    return parser

def run_dir(dirpath: str, pickling: bool,daDIR: str):
    txtpath = dirpath + '/txt_outputs/'
    pickle_path = dirpath + '/pickle_outputs/'
    meta_path = dirpath + '/DialogAgent_outputs/'
    filepath = str(Path(__file__))[:-len("batch_reprocessor.py")]
    os.system(f"mkdir {txtpath}")
    os.system(f"mkdir {pickle_path}")
    os.system(f"mkdir {meta_path}")
    for entry in os.scandir(dirpath):
        txtname = (txtpath + entry.name[:-3] + 'txt')
        metaname = (meta_path + entry.name[:-3] + 'metadata')
        caption_list = txt.txt_single(inputfile=entry.path,outputfile=txtname)
        if caption_list:
            os.chdir(daDIR)
            try:
                os.system(f"sbt \"runMain org.clulab.asist.apps.RunDialogAgent file {txtname} {metaname}\"")
            except:
                print("Please ensure that your tomcat-text repo is working as expected and the --tomcatdir argument is set correctly")
            os.chdir(filepath)
            pickle = pickle_path + entry.name[:-4]
            txt.import_extractions(inputfile=entry.path,jsonfile=metaname,pickling=pickling,outputfile=pickle)




def main():
    parser = start_parser()
    args = parser.parse_args()
    run_dir(dirpath=args.dir, pickling=args.pickle, daDIR=args.tomcatdir)
    pass


if __name__ == '__main__':
    main()