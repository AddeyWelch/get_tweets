import oauth2 as oauth
import urllib
import urllib.request

# See assignment1.html instructions or README for how to get these credentials

api_key = "Q0TP2raf1ouXhZqM7ISdTUoaL"
api_secret = "XeKVlvS7RFB7RprCadmOU3HIdD5Lkk2hi7UstcAahDdzyvIOHX"
access_token_key = "808329254840791040-dBzQeXEl9Ebb9jTHzRRhlWTBxVojzpu"
access_token_secret = "h3BYkpNIXMarh8bpFNS3WIYe8IeKHy0BA9Rx7VWoMy1dU"

api = twitter.Api(consumer_key=api_key,
                  consumer_secret=api_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)

_debug = 0

oauth_token = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"

http_handler = urllib.request.HTTPHandler(debuglevel=_debug)
https_handler = urllib.request.HTTPSHandler(debuglevel=_debug)
'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''


def twitterreq(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                                token=oauth_token,
                                                http_method=http_method,
                                                http_url=url,
                                                parameters=parameters)

    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

    headers = req.to_header()

    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()

    opener = urllib.request.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    response = opener.open(url, encoded_post_data)

    return response


def fetchsamples():
    url = "https://stream.twitter.com/1/statuses/sample.json"
    parameters = []
    response = twitterreq(url, "GET", parameters)
    for line in response:
        print(line.strip())


if __name__ == '__main__':
    fetchsamples()
