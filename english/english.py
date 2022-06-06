import tweepy
import os

from english_keys import API_key, API_secret, Access_token, Access_secret

auth = tweepy.OAuthHandler(API_key, API_secret)
auth.set_access_token(Access_token, Access_secret)

api = tweepy.API(auth)

'''
# To test access to Twitter
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
api.update_status("This is an API access test tweet.")
'''

print(os.getcwd())
os.chdir(os.path.dirname(__file__))

# To tweet the first line from the file then save the file without that line
with open('english_ready.txt', 'r') as ttc:
	split = ttc.read().splitlines()
	tweet = split.pop(0)
	api.update_status(tweet)
	strsplit = '\n'.join(split) # convert [] to line-sep''

with open('english_ready.txt','w') as overwrite:
	overwrite.seek(0) # ensure you're at the beginning of the file
	overwrite.write(strsplit)
