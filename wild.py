import tweepy
count = 0
f = open("tweets.txt",'a')
EW = 0
BO = 0
DemTwitterHandles = {'Beto O\'Roarke' : '@betoorourke','Elizabeth Warren' : "ewarren",'Bernie Sanders' : 'BernieSanders'}

DemCandidates = {'Beto O\'Roarke' : 0 ,'Elizabeth Warren': 0,'Joe Biden' : 0, 'Bernie Sanders' : 0}
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        for name in DemCandidates.keys():
            if name in status.text:
                DemCandidates[name] +=1


        try:
            print(status.text)
            f.write(status.text)



            print(status.text)
        except:
            print("can't print character")
        print(DemCandidates)

consid = 'XXX'

secret = 'XXX'
actk = 'XXX'
sctk = 'XXX'
auth = tweepy.OAuthHandler(consid,secret)
auth.set_access_token(actk,sctk)
api = tweepy.API(auth)

lner = MyStreamListener()
lner = tweepy.Stream(auth = api.auth, listener=lner)
lner.filter(track=DemCandidates)

"""
tweets = tweepy.Cursor(api.search,q="//1").items(100)
for page in tweepy.Cursor(api.search,q ='@realDonaldTrump',count=10).pages(10):
    for tweet in page:
        r = tweet.text
        if(len(r)<100):
            print(r)
"""
