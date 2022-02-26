#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ryan L. Boyd
# 2022-02-23

#      _      _______          _______    ___  ___            _ _   ______                           _
#     | |    |_   _\ \        / / ____|  |__ \|__ \          | (_) |  ____|                         | |
#     | |      | |  \ \  /\  / | |   ______ ) |  ) ______ ___| |_  | |__  __  ____ _ _ __ ___  _ __ | | ___
#     | |      | |   \ \/  \/ /| |  |______/ /  / |______/ __| | | |  __| \ \/ / _` | '_ ` _ \| '_ \| |/ _ \
#     | |____ _| |_   \  /\  / | |____    / /_ / /_     | (__| | | | |____ >  | (_| | | | | | | |_) | |  __/
#     |______|_____|   \/  \/   \_____|  |____|____|     \___|_|_| |______/_/\_\__,_|_| |_| |_| .__/|_|\___|
#                                                                                             | |
#                                                                                             |_|
"""
    This is an example script that demonstrates how to make a call to the LIWC-22 command line interface (CLI)
    from Python. Briefly described, what we want to do is launch the CLI application as a subprocess, then wait
    for that subprocess to finish.

    This is a very crude example script, so please feel free to improve/innovate on this example :)          """


# Make sure that you have the LIWC-22.exe GUI running — it is required for the CLI to function correctly :)
# Make sure that you have the LIWC-22.exe GUI running — it is required for the CLI to function correctly :)
# Make sure that you have the LIWC-22.exe GUI running — it is required for the CLI to function correctly :)
# Make sure that you have the LIWC-22.exe GUI running — it is required for the CLI to function correctly :)


import subprocess


#  ______    _     _                      _ _   _       _________   _________   ______ _ _
# |  ____|  | |   | |                    (_| | | |     |__   __\ \ / |__   __| |  ____(_| |
# | |__ ___ | | __| | ___ _ __  __      ___| |_| |__      | |   \ V /   | |    | |__   _| | ___ ___
# |  __/ _ \| |/ _` |/ _ | '__| \ \ /\ / | | __| '_ \     | |    > <    | |    |  __| | | |/ _ / __|
# | | | (_) | | (_| |  __| |     \ V  V /| | |_| | | |    | |   / . \   | |    | |    | | |  __\__ \
# |_|  \___/|_|\__,_|\___|_|      \_/\_/ |_|\__|_| |_|    |_|  /_/ \_\  |_|    |_|    |_|_|\___|___/

inputFolderTXT = "C:/Users/Ryan/Datasets/TED - English Only - TXT Files/"
outputLocation = "C:/Users/Ryan/Datasets/TED Talk TXT Files - Analyzed.csv"

# This command will read texts from a folder, analyze them using the standard "Word Count" LIWC analysis,
# then save our output to a specified location.
cmd_to_execute = ["LIWC-22-cli",
                  "--mode", "wc",
                  "--input", inputFolderTXT,
                  "--output", outputLocation]



# Let's go ahead and run this analysis:
subprocess.call(cmd_to_execute)

# We will see the following in the terminal as it begins working:
#
#    Picked up JAVA_TOOL_OPTIONS: -Dfile.encoding=UTF-8
#    Processing:
#     - [folder] C:\Users\Ryan\Datasets\TED - English Only - TXT Files
#    [===================                     ] 47.75%; Number of Texts Analyzed: 1304; Total Words Analyzed: 2.62M


# A thing of beauty, to be sure. What if we want to process our texts using an older LIWC dictionary,
# or an external dictionary file? This can be done easily as well.



# We can specify whether we want to use the LIWC2001, LIWC2007, LIWC2015,
# or LIWC22 dictionary with the --dictionary argument.
liwcDict = "LIWC2015"

# Alternatively, you can specify the absolute path to an external dictionary
# file that you would like to use, and LIWC will load this dictionary for processing.
#liwcDict = "C:/Users/Ryan/Dictionaries/Personal Values Dictionary.dicx"


# Let's update our output location as well so that we don't overwrite our previous file.
outputLocation = "C:/Users/Ryan/Datasets/TED Talk TXT Files - Analyzed (LIWC2015).csv"

cmd_to_execute = ["LIWC-22-cli",
                  "--mode", "wc",
                  "--dictionary", liwcDict,
                  "--input", inputFolderTXT,
                  "--output", outputLocation]

subprocess.call(cmd_to_execute)








#   _____  _______      __  ______ _ _
#  / ____|/ ____\ \    / / |  ____(_| |
# | |    | (___  \ \  / /  | |__   _| | ___
# | |     \___ \  \ \/ /   |  __| | | |/ _ \
# | |____ ____) |  \  /    | |    | | |  __/
#  \_____|_____/    \/     |_|    |_|_|\___|



# Beautiful. Now, let's do the same thing, but analyzing a CSV file full of the same texts.
inputFileCSV = 'C:/Users/Ryan/Datasets/TED Talk - English Transcripts.csv'
outputLocation = 'C:/Users/Ryan/Datasets/TED Talk CSV File - Analyzed.csv'


# We're going to use a variation on the command above. Since this is a CSV file, we want to include the indices of
#     1) the columns that include the text identifiers (although this is not required, it makes our data easier to merge later)
#     2) the columns that include the actual text that we want to analyze
#
# In my CSV file, the first column has the text identifiers, and the second column contains the text.
# For more complex datasets, please use the --help argument with LIWC-22 to learn more about how to process your text.
cmd_to_execute = ["LIWC-22-cli",
                  "--mode", "wc",
                  "--input", inputFileCSV,
                  "--row-id-indices", "1",
                  "--column-indices", "2",
                  "--output", outputLocation]

# Let's go ahead and run this analysis:
subprocess.call(cmd_to_execute)


# We will see the following in the terminal as LIWC does its magic:
#    Picked up JAVA_TOOL_OPTIONS: -Dfile.encoding=UTF-8
#    Processing:
#     - [file] C:\Users\Ryan\Datasets\TED Talk - English Transcripts.csv
#    [========================================] 100.00%; Number of Rows Analyzed: 2737; Total Words Analyzed: 5.40M
#    Done. Please examine results in C:\Users\Ryan\Datasets\TED Talk CSV File - Analyzed.csv









#                       _                  _____ _        _
#     /\               | |                / ____| |      (_)
#    /  \   _ __   __ _| |_   _ _______  | (___ | |_ _ __ _ _ __   __ _
#   / /\ \ | '_ \ / _` | | | | |_  / _ \  \___ \| __| '__| | '_ \ / _` |
#  / ____ \| | | | (_| | | |_| |/ |  __/  ____) | |_| |  | | | | | (_| |
# /_/    \_|_| |_|\__,_|_|\__, /___\___| |_____/ \__|_|  |_|_| |_|\__, |
#                          __/ |                                   __/ |
#                         |___/                                   |___/

# What if we want to simply pass a string to the CLI for analysis? This is possible. As described on the
# Help section of the liwc.app website, this is generally not recommended as it will not be very performant.
# However, if you insist...

# The string that we would like to analyze.
inputString = r"This is some text that I would like to analyze. After it has finished, I will say \"Thank you, LIWC!\""

# For this one, let's save our result as a newline-delimited json file (.ndjson)
outputLocation = 'C:/Users/Ryan/Datasets/LIWC-22 Results from String.ndjson'


cmd_to_execute = ["LIWC-22-cli",
                  "--mode", "wc",
                  "--input", "console",
                  "--console-text", inputString,
                  "--output", outputLocation]


# Let's go ahead and run this analysis:
subprocess.call(cmd_to_execute)

# The results from this analysis:
#{"Segment": 1,"WC": 20,"Analytic": 3.8,"Clout": 40.06,"Authentic": 28.56,"Tone": 99,"WPS": 10,"BigWords": 10,
#"Dic": 100, "Linguistic": 80,"function": 70,"pronoun": 30,"ppron": 15,"i": 10,"we": 0,"you": 5,"shehe": 0,"they": 0,
#"ipron": 15,"det": 15,"article": 0,"number": 0,"prep": 15,"auxverb": 20,"adverb": 0,"conj": 5,"negate": 0,
#"verb": 35,"adj": 0,"quantity": 5,"Drives": 5,"affiliation": 0,"achieve": 5,"power": 0,"Cognition": 15,
#"allnone": 0,"cogproc": 15,"insight": 5,"cause": 0,"discrep": 10,"tentat": 0,"certitude": 0,"differ": 0,
#"memory": 0,"Affect": 15,"tone_pos": 15,"tone_neg": 0,"emotion": 10,"emo_pos": 10,"emo_neg": 0,"emo_anx": 0,
#"emo_anger": 0,"emo_sad": 0,"swear": 0,"Social": 20,"socbehav": 15,"prosocial": 5,"polite": 5,"conflict": 0,"moral": 0,
#"comm": 15,"socrefs": 5,"family": 0,"friend": 0,"female": 0,"male": 0,"Culture": 5,"politic": 0,"ethnicity": 0,"
#tech": 5,"Lifestyle": 0,"leisure": 0,"home": 0,"work": 0,"money": 0,"relig": 0,"Physical": 0,"health": 0,"illness": 0,
#"wellness": 0,"mental": 0,"substances": 0,"sexual": 0,"food": 0,"death": 0,"need": 0,"want": 0,"acquire": 0,"lack": 0,
#"fulfill": 0,"fatigue": 0,"reward": 0,"risk": 0,"curiosity": 0,"allure": 0,"Perception": 0,"attention": 0,"motion": 0,
#"space": 0,"visual": 0,"auditory": 0,"feeling": 0,"time": 10,"focuspast": 0,"focuspresent": 10,"focusfuture": 5,
#"Conversation": 0,"netspeak": 0,"assent": 0,"nonflu": 0,"filler": 0,
#"AllPunc": 30,"Period": 5,"Comma": 10,"QMark": 0,"Exclam": 5,"Apostro": 0,"OtherP": 10}
