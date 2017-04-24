import sys, requests, datetime, re, json, os, time
from color import *
# get arguments
arguments=sys.argv
del arguments[0]
# arguments = ["score", "debug"]
if "debug" in arguments: debug=True
else: debug=False

# getting apikey
if debug: print "getting cricapi key\n"
try:
    key = (open(r'apikey.txt', 'r')).readlines()[0]
except ImportError:
    sys.exit("apikey.txt file does no exist. please create one according to the documentation given")
if debug: print "got the cric apikey:"+key+'\n'

# defining constants
today = str(datetime.datetime.now().date())
url = "http://cricapi.com/api/"


# printing matchlist, only today by default, all argumemt print all the data
if "matchlist" in arguments:
    requesturl = url+"matches/"
    try:
        response = requests.request('GET', requesturl, data={'apikey':key})
    except:
        sys.exit("please recheck your internet connection")
    data = json.loads(response.text)
    print ''.join(["%-30s"%"team-1", "%-30s"%"team-2", "%-20s"%"unique_id","%-20s"%"date"\
                   ,"%-15s"%"match started", '\n'])
    sys.stdout.write(RED)  # RED
    if "all" in arguments:
        for i in data['matches']:
            print ''.join(["%-30s" % i['team-1'], "%-30s" % i['team-2'], \
                           "%-20s" % i['unique_id'], "%-20s" % i['date'][0:10], \
                           "%-15s"%i['matchStarted'], '\n'])

    else:
        for i in data['matches']:
            if today == (i['date'][0:10]):
                print ''.join(["%-30s" % i['team-1'], "%-30s" % i['team-2'], \
                               "%-20s" % i['unique_id'], "%-20s" % i['date'][0:10], \
                               "%-15s" % i['matchStarted'], '\n'])
    sys.exit("please note the unique_id of the match score you want to check")

# print score of given match id
if "score" in arguments:
    matchid = raw_input("please enter a valid match id:")

    # receive and set timer else default timer is 2 seconds
    timer=15
    if "timer" in arguments:
        timer = int(raw_input("please enter refresh rate in seconds (>15) and (<60):"))
        if timer<15: timer=15
        if timer>60: timer=60

    requesturl = url+"cricketScore/"
    response = requests.request('GET', requesturl, data={'unique_id':matchid, 'apikey':key})
    data = json.loads(response.text)
    print data
    if not data['matchStarted']:
        print data['innings-requirement']
        sys.exit("match is not live right now\n")
    if "score" not in data:
        sys.exit("please enter a valid match id")
    else:
        while True:
            response = requests.request('GET', requesturl, data={'unique_id': matchid, 'apikey': key})
            data = json.loads(response.text)
            data = data['score']
            score = re.match('^(.*)\(', data).group(1)
            stats = re.match('^.*\((.*)\)', data).group(1).split(',')
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.stdout.write(GREEN)  # GREEN
            print ''.join(["%-14s" % "score", "%-10s" % "overs", "%-25s" % "batsman_strike", \
                           "%-25s" % "batsman_runner", "%-25s" % "bowler",'\n'])
            sys.stdout.write(RED)  # RED
            print ''.join(["%-14s" % score, "%-10s" % stats[0], "%-25s" % stats[1], \
                           "%-25s" % stats[2], "%-25s" % stats[3]])
            time.sleep(timer)