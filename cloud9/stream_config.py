# Twitter Authentication
APP_KEY =''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''
bearer_token='' 


# Twitter Rules List (stream filters), see Twitter docs for details
# Note that these rules are overwritten each time the script is run!
sample_rules = [
    { 'value': 'prozac OR fluoxetine OR cymbalta OR celexa OR citalopram OR amoxil OR amoxicillin OR lexapro OR escitalopram lang:en -is:retweet', "tag": "newest"},
]
#prozac OR fluoxetine OR cymbalta OR celexa OR citalopram OR amoxil OR amoxicillin OR lexapro OR escitalopram
# DynamoDB Information
region_name ='us-east-1'
aws_access_key_id = ''
aws_secret_access_key = ''
table_name = 'ae_tweets_ddb'

# Fxn: Searches for drug mentions (substring) in raw text of Tweet. Returns a list of comma-separated drug names.
def drug_types(text):
    contains = []
    if "prozac" in text.lower() or "fluoxetine" in text.lower():
        contains.append("prozac")
    if "celexa" in text.lower() or "citalopram" in text.lower():
        contains.append("celexa")
    if "cymbalta" in text.lower() or "duloxetine" in text.lower():
        contains.append("cymbalta")
    if "lexapro" in text.lower() or "escitalopram" in text.lower():
        contains.append("lexapro")
    if "amoxicillin" in text.lower() or "amoxil" in text.lower() or "moxatag" in text.lower():
        contains.append("amoxicillin")
    return contains