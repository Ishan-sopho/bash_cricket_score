# bash_cricket_score
live cricket scores on your terminal
credits: data taken from http://www.cricapi.com

# requirements
the code is wrutten in python 2.7 and you will require to install it on your PC.
the data is taken from http://www.cricapi.com. you will need to create an account with the website to get the apikeey. it is free and allows unlimited calls.
store this apikey in a file called 'apikey.txt'. just copy and paste the apikey you get in this folder.

# arguments supported

matchlist: displays a list of matches along woth unique ids. this is by default set to display current matches, however you can give a "all" argument to display all matches upto five days ahead. note down the unique_id of teh match you want to follow.

score: you will be prompted to enter a a valid unique_id for the match you want to follow. the score will display basic statistics oon the  command line. the score will automaticaly refresh ever 15 seconds. you can change the refresh rate by entering teh argunment timer which will allow you to enter refresh rate in seconds.

deubg: shows debugger information

# personalize

you can personalize the font of scores and match list displayed. the file color.py contains colors in ANSII format. simply change the color in the a sys.stdout.write(\\color you want chosen from color.py)
