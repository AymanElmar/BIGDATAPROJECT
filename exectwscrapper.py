import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level
import datetime

#Scraping tweets from relevant accounts in twitter that give more relevant information:

#read csv file and look up tweets for each name:
with open('EXECUTIVE NAMES.csv') as f:
    lis = f.readlines()
    lis = [x.strip() for x in lis]
    lis[0]=lis[0].strip('ï»¿')
    lis=[x for x in lis if x != '']
f.close()
#set up the API:
api = API()
async def main():
    for name in lis:
        with open("GET_OLD_TWEETS/"+name+".json", 'w') as f:
            #set up the query:
            query = '$TSLA OR Tesla min_faves:50 from:'+name+' since:2019-01-01'
            num_tweets = 3000

            async for tweet in api.search(query, limit=num_tweets)  :
                f.write(tweet.json() + "\n")
            print("done with "+name)
        f.close()

if __name__ == "__main__":
   asyncio.run(main())