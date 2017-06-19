'''this bash cricket scores. get live cricket scores on your terminal.
the usage is simple. simply type: python cricket_scores.py and follow prompts to use the script.

arguments:
help: to print documentation for script
timer: to configure refresh rate
debug: to see debug information
timer: to configure refresh rate

usage:
python cricket_scores.py [arguments separated by blanks:optional'''


import sys, requests, datetime, re, json, os, time
from color import *

# get arguments
arguments=sys.argv
del arguments[0]

# printing help
if "help" in arguments:
    sys.exit(__doc__)

# arguments = ["score", "debug"]
if "debug" in arguments: debug=True
else: debug=False

# getting apikey
if debug: print "getting cricapi key\n"
try:
    key = (open(r'apikey.txt', 'r')).readlines()[0]
except ImportError:
    print "apikey.txt file not found"
    key=raw_input("please enter apikey:")
if debug: print "got the cric apikey:"+key+'\n'

# defining constants
today = str(datetime.datetime.now().date())
url = "http://cricapi.com/api/"
id_list=[]
timer=15

# printing matchlist
requesturl = url+"matches/"
try:
    response = requests.request('GET', requesturl, data={'apikey':key})
except:
    sys.exit("please recheck your internet connection")
data = json.loads(response.text)
print ''.join(["%-30s"%"team-1", "%-30s"%"team-2", "%-20s"%"unique_id","%-20s"%"date"\
               ,"%-15s"%"match started", '\n'])
if "all" in arguments:
    for i in data['matches']:
        id_list.append(str(i['unique_id']))
        print ''.join(["%-30s" % i['team-1'], "%-30s" % i['team-2'], \
                       "%-20s" % i['unique_id'], "%-20s" % i['date'][0:10], \
                       "%-15s"%i['matchStarted'], '\n'])
else:
    for i in data['matches']:
        if today == (i['date'][0:10]):
            id_list.append(str(i['unique_id']))
            print ''.join(["%-30s" % i['team-1'], "%-30s" % i['team-2'], \
                           "%-20s" % i['unique_id'], "%-20s" % i['date'][0:10], \
                           "%-15s" % i['matchStarted'], '\n'])

# checking id input
while True:
    matchid = raw_input("please enter a valid match id:")
    if matchid not in id_list:
        print "please recheck the id you wish to enter."
    else:
        break

# receive and set timer else default timer is 2 seconds
if "timer" in arguments:
    timer = int(raw_input("please enter refresh rate in seconds (>15) and (<60):"))
    if timer<15: timer=15
    if timer>60: timer=60

# calling cricapi website for data
requesturl = url+"cricketScore/"
response = requests.request('GET', requesturl, data={'unique_id':matchid, 'apikey':key})
data = json.loads(response.text)
if not data['matchStarted']:
    print data['innings-requirement']
    sys.exit("match is not live right now\n")

prev_score, print_list=-1, ['', '', '']
while True:
    response = requests.request('GET', requesturl, data={'unique_id': matchid, 'apikey': key})
    data = json.loads(response.text)
    data = data['score']
    score = re.match('^(.*)\(', data).group(1)
    stats = re.match('^.*\((.*)\)', data).group(1).split(',')
    table=''.join(["%-35s" % "score", "%-10s" % "overs", "%-25s" % "batsman_strike", \
                       "%-25s" % "batsman_runner", "%-25s" % "bowler", '\n'])

    # check if score has changed
    if stats[0]!= prev_score:
        os.system('cls||clear')
        prev_score=stats[0]
        print_list[1:3]=print_list[0:2]
        print_list[0]= ''.join(["%-35s" % score, "%-10s" % stats[0], "%-25s" % stats[1], \
                                "%-25s" % stats[2], "%-25s" % stats[3]])
        sys.stdout.write(GREEN)  # GREEN
        print table
        sys.stdout.write(RED)  # RED
        # print last three score entries
        for i in print_list:
            print i
    print
    time.sleep(timer)