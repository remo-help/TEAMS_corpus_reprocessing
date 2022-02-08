# TEAMS_corpus_reprocessing
A repository for scripts which are used to process TEAMS corpus data for processing with the tomcat-text engine.

# Data Structure
The output of these scripts contains the following structure:

* pickle mode True: a pickle file containing an object of type \[{}\] (a list of dictionaries)
* * each dictionary contains the following values:
* * * Speaker: string: speaker_role
* * * Timestamp: tuple of floats
* * * Team_ID: string: the ID of the team and the game
* * * Extractions: \[ a list of DialogAgent extractions\]
* * * Utterance: A string object of the utterance
* pickle mode False: a text file containing the above data structure as a file of JSON objects

## Single File Mode (txt_reprocessor.py)
This mode allows you to process a single TEAMS corpus .xls file. Use as follows:

    python txt_reprocessor.py --file YOUR_INPUT_FILE.xls --outputfile YOUR_OUTPUTFILE.txt

This will extract all lines of text from your .xls file and write them as lines in a simple .txt file. Next you will need to process ths .txt file with the ASIST DialogAgent (we are using a fork here):

    git clone https://github.com/remo-help/tomcat-text.git
    cd tomcat-text
    sbt "runMain org.clulab.asist.apps.RunDialogAgent file path/YOUR_TXT_FILE.txt path/ASIST_OUTPUTFILE"

This will run the DialogAgent on all the lines in the .txt file you produced. The outputfile you define will contain a JSON object for each line.

Now we can process the DialogAgent extractions into our TEAMS data:

    python txt_reprocessor.py --file YOUR_INPUT_FILE.xls --json ASIST_OUTPUTFILE --outputfile FINAL_OUTPTUTFILE

It is imperative that `YOUR_INPUT_FILE.xls` is the same file you called the first time. The output of this operation will be a `pickle` file which contains a list of dictionaries. The dictionaries are representations of JSON objects.

If you wish your output to be a readable text file instead, you can call the above with an additional flag:

    python txt_reprocessor.py --file YOUR_INPUT_FILE.xls --json ASIST_OUTPUTFILE --outputfile FINAL_OUTPTUTFILE --pickle False
    
With the `--pickle` flag marked as `False` or `no` you will export a text file instead of a pickle file.

## Multi File Mode
 The multi file mode allows you to process entire directories of TEAMS corpus files in batch.
It will produce 3 subdirectories in the directory you point it to:

* `/txt_outputs/` These are the .txt files containing the extracted utterances as lines
* `/DialogAgent_outputs/` The DialogAgent metadata files containing the DialogAgent Extractions of your .txt lines.
* `/pickle_outputs/` The final output files as described in *Data Structure*. These will be in this directory regardless of whether you call the `--pickle 0/1` parameter.

### Usage

The usage for this mode is simple. First you need to clone the tomcat-text repo. For the TEAMS corpus you want our fork:

    git clone https://github.com/remo-help/tomcat-text.git

Make sure you know where you clone this repo to. You will need the path of the repo in the next step. Now call the `batch_processor.py` script:

    python batch_reprocessor.py --dir DIRECTORY_OF_TEAMS_FILES --pickle TRUE/FALSE --tomcatdir DIRECTORY_OF_TOMCAT_REPO

That's it. The batch processor will now process every file in your --dir. This may take a while.