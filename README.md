# TEAMS_corpus_reprocessing
A repository for scripts which are used to process [TEAM corpus](https://sites.google.com/site/teamentrainmentstudy/corpus) data into .vtt files for processing with the [tomcat-text](https://github.com/clulab/tomcat-text) engine.


# vtt_reprocessor
Usage: $ python vtt_reprocessor --dir --filename

--dir: a directory of .xls files (transcripts of the TEAM corpus)

--filename: the filename of your outputfile

description: this script will take a directory of TEAM corpus transcripts and reprocess them into a single .vtt file. 
