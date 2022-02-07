# TEAMS_corpus_reprocessing
A repository for scripts which are used to process TEAMS corpus data for processing with the tomcat-text engine.

# Usage

## Single File Mode (txt_reprocessor.py)
This mode allows you to process a single TEAMS corpus .xls file. Use as follows:

    `python txt_reprocessor.py --file YOUR_INPUT_FILE.xls --outputfile YOUR_OUTPUTFILE.txt`

This will extract all lines of text from your .xls file and write them as lines in a simple .txt file. Next you will need to process ths .txt file with the ASIST DialogAgent:

    `git clone https://github.com/remo-help/tomcat-text.git`
    `sbt "runMain org.clulab.asist.apps.RunDialogAgent file path/YOUR_TXT_FILE.txt path/ASIST_OUTPUTFILE"`

This will run the DialogAgent on all the lines in the .txt file you produced. The outputfile you define will contain a JSON object for each line.

Now we can process the DialogAgent extractions into our TEAMS data:

    `python txt_reprocessor.py --file YOUR_INPUT_FILE.xls --json ASIST_OUTPUTFILE --outputfile FINAL_OUTPTUTFILE`

It is imperative that `YOUR_INPUT_FILE.xls` is the same file you called the first time. The output of this operation will be a `pickle` file which contains a list of dictionaries. The dictionaries are representations of JSON objects.
