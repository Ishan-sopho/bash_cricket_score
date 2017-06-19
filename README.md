# bash_cricket_score
Live cricket scores on your terminal  
*credits*: data taken from http://www.cricapi.com

# Requirements
The code is written in `python 2.7` and you will require to install it on your PC.
The data is taken from [CricAPI](http://www.cricapi.com). You will need to create an account with the website to get the `apikey`. It is free and allows unlimited calls.
Store this `apikey` in a file called `apikey.txt`. Just copy and paste the apikey you get, in this file.

# Arguments supported

`debug`: shows debugger information.
`help`: to show documentation
`timer`: to configure refresh rate

Example 
```bash
>> python cricket_scores.py help
>> python cricket_scores.py debug
>> python cricket_scores.py timer
```

# Personalize
You can personalize the font of scores and match list displayed. the file color.py contains colors in ANSII format.
Simply change the color in the a `sys.stdout.write(<color you want chosen from color.py>)`

# Message
Please feel free to make suggestions, improvements and point out any bugs you encounter.
