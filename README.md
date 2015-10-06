#EskomLoadSheddingTwitterBot
A python script that tweets when the Eskom load shedding stage changes. This script powers the twitter bot [@LDShedStatus](https://twitter.com/ldshedstatus). 

##How it works
EskomLoadShedddingTwitterBot is a python script which utilizes Twython to tweet, when the Eskom api changes the load shedding status. It stores an offline copy of the load shedding status in loadSheddingStatus.txt. The python script then compares the offline load shedding value to the value from the Eskop api. If the values are different, the python script tweets the new load shedding status and updates the offline load shedding value. The offline load shedding values are stored to match the load shedding stage. So a value of 0 represents Stage-0, while a value of 3 represents Stage-3 load shedding.

##How to use
Simply run the python script as often as you would like. I've included a shell script, checkStatusAndTweet.sh, which runs the python script every five minutes.

To run the shell script in a Linux environment, simply execute 'sh checkStatusAndTweet.sh' in your favorite terminal.

You will need to create a [twitter application key](https://dev.twitter.com/oauth) in order to use [Twython](http://twython.readthedocs.org/en/latest/). Then you must update the key values in the python script in order to login and post from your twitter account.

Check out this post about how to [run the bot in Google Cloud Shell](http://jekel.me/2015/Python-Twitter-Bot-Using-Google-Shell/).

You can install Twython with pip. Simply run 'pip install twhython' in your terminal. 

##MIT License
The MIT License (MIT)

Copyright (c) 2015 Charles Jekel

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
