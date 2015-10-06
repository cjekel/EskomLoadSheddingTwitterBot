import urllib2
import datetime
from twython import Twython

#   Setup twitter login details
APP_KEY = 'XXXXX'  # Customer Key here
APP_SECRET = 'XXXX'  # Customer secret here
OAUTH_TOKEN = 'XXXX'  # Access Token here
OAUTH_TOKEN_SECRET = 'XXXX'  # Access Token Secret here

#   load the previous load shedding status
with open('loadSheddingStatus.txt','r') as  pre:
    prevLDStatus = int(pre.read())

#   pull the html from the url
shareNet = urllib2.urlopen('http://loadshedding.eskom.co.za/LoadShedding/GetStatus?_=')
htmlShareNet = shareNet.readlines()

#   Check to see that the url was successfully pulled
if len(htmlShareNet) < 1:
    print 'error connectiong to website'
    loadSheddingStatus = prevLDStatus   #   Set the status equal to the previous one
else:
    #   Set the load shedding status
    loadSheddingStatus = int(htmlShareNet[0]) - 1 # such that a zero load stage = 0   

#   Pull the local time from the  os
theTimeIs = str(datetime.datetime.now())

if prevLDStatus > loadSheddingStatus:
    print 'the load shedding status has been lowered'
    
    #   login to twitter
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    if loadSheddingStatus == 0:
        statusString = 'No longer load shedding. ' + theTimeIs
        twitter.update_status(status=statusString)

    else:
        statusString = 'Now STAGE-'+str(loadSheddingStatus)+'! The load Shedding Stage has been lowered to Stage-' + str(loadSheddingStatus) + '. ' + theTimeIs
        twitter.update_status(status=statusString)
        
elif prevLDStatus < loadSheddingStatus:
    print 'the load shedding status has been Raised'
    
    #   login to twitter
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    statusString = 'Now STAGE-'+str(loadSheddingStatus)+'! The load Shedding Stage has been raised to Stage-' + str(loadSheddingStatus) + '. ' + theTimeIs
    twitter.update_status(status=statusString)

else:
    print 'the load shedding status is unchanged'


#   Save the loadSheddingStatus
with open('loadSheddingStatus.txt','w') as out:
    out.write(str(loadSheddingStatus))
