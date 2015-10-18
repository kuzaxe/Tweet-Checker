MIN_LENGTH = 1
MAX_LENGTH = 140


def is_valid_tweet(tweet):
    """ (str) -> bool 

    Return True if and only if tweet is no less than 1 and no more 
    than 140 characters long.

    >>> is_valid_tweet('To me programming is more than an important ' \
        + 'practical art. It is also a gigantic undertaking in the ' \
        + 'foundations of knowledge. - Grace Hopper')
    True
    >>> is_valid_tweet('The best programs are written so that computing ' \
        + 'machines can perform them quickly and so that human beings can ' \
        + 'understand them clearly. - Donald Knuth')
    False
    """
    return MIN_LENGTH <= len(tweet) <= MAX_LENGTH

def contains_hash_symbol(valid_tweet):
    """(str) -> bool

    Return True if and only if valid_tweet contains a hash symbol.

    >>> contains_hash_symbol("I love #Pie")
    True
    >>> contains_hash_symbol("I love cats")
    False
    """
    return "#" in valid_tweet


def is_mentioned(valid_tweet, valid_username):
    """(str, str) -> bool

    Return True if and only if valid_tweet mentions valid_username preceded by @.

    >>> is_mentioned("I love @cssc", "cssc")
    True
    >>> is_mentioned("I love apple", "apple")
    False
    """
    return ("@" + valid_username) in valid_tweet
    
def report_shortest(Tweet1, Tweet2):
    """(str, str) -> str

    Return one of three strings: 'Tweet 1', 'Tweet 2', or 'Same length' spelled
    and capitalized exactly as specified here.

    >>> report_shortest("I love apple","I love pie")
    'Tweet 2'
    >>> report_shortest("I love you", "I love you")
    'Same Length'
    >>> report_shortest("I am Batman!", "I am Superman!")
    'Tweet 1'
    """
    if len(Tweet1) > len(Tweet2):
        return "Tweet 2"
    elif len(Tweet2) > len(Tweet1):
        return "Tweet 1"
    else:
        return "Same length"        

def is_reply(valid_tweet):
    """(str) -> bool

    Return True if and only if valid_tweet is a reply.

    >>> is_reply("@rhythm I want to dance")
    True
    >>> is_reply("rhytym I want to sing")
    False
    """
    return valid_tweet[0] == "@"

def format_reply_to(valid_username, valid_tweet):
    """(str, str) -> str

    Return a reply tweet to the given valid_username.
    The reply should consist of a mention of valid_username followed by a space and the given valid_tweet.

     >>> format_reply_to("@John", "Will see you tomorrow!")
     '@John Will see you tomorrow!'
     >>> format_reply_to("@Mike", "Can you bring Mike's Hard Lemonade!")
     '@Mike Can you bring Mike's Hard Lemonade'
     >>> format_reply_to("Apple", "I want the iPhone 6")
     '@Apple I want the iPhone 6'
     >>> format_reply_to("Monkey","The best programs are written so that computing " \
        + "machines can perform them quickly and so that human beings can " \
        + "understand them clearly. - Donald Knuth")
    '8 characters too long'
    
    """
    if valid_username[0] == "@":
        new_mention = valid_username
    else: 
        new_mention = "@" + valid_username
		
    if len(valid_tweet) <= MAX_LENGTH:
        return new_mention + " " + valid_tweet
    elif len(valid_tweet) > MAX_LENGTH:
        return str(len(valid_tweet[MAX_LENGTH:])) + " characters too long"
