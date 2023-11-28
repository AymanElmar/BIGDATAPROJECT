import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level
import datetime

#LOOP ON DATES
#START DATE: 2021-01-01   
async def main():
    start_date = datetime.datetime(2021,1,1)
    end_date = datetime.datetime(2021,1,2)
    with open("TSLA_tweets.json", "w") as f:
        while end_date.strftime("%Y-%m-%d") != "2023-11-24":
            api = API()
            q = "$TSLA since:"+start_date.strftime("%Y-%m-%d")+" until:"+ end_date.strftime("%Y-%m-%d")+" lang:en" 
            async for tweet in api.search(q, limit=20):
                f.write(tweet.json() + "\n")
            start_date += datetime.timedelta(days=1)
            end_date += datetime.timedelta(days=1)
            print(start_date.strftime("%Y-%m-%d"))
    f.close()

if __name__ == "__main__":
    asyncio.run(main())