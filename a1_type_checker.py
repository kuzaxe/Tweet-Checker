import tweet
import builtins

# Get the initial value of the constant
constants_before = [tweet.MIN_LENGTH, tweet.MAX_LENGTH]

# Type check tweet.is_valid_tweet
result = tweet.is_valid_tweet('Test 123')
assert isinstance(result, bool), \
       '''tweet.is_valid_tweet should return a bool, but returned {0}
       .'''.format(type(result))

# Type check tweet.contains_hash_symbol
result = tweet.contains_hash_symbol('Test 123')
assert isinstance(result, bool), \
       '''tweet.contains_hash_symbol should return a bool, but returned {0}.''' \
       .format(type(result))

# Type check tweet.is_mentioned
result = tweet.is_mentioned('Test 123', 'abc')
assert isinstance(result, bool), \
       '''tweet.is_mentioned should return an bool, but returned {0}.''' \
       .format(type(result))


# Type check tweet.report_shortest
result = tweet.report_shortest('abc', 'def')
assert isinstance(result, str), \
       '''tweet.report_shortest should return an str, but returned {0}.''' \
       .format(type(result))


# Type check tweet.is_reply
result = tweet.is_reply('abcd')
assert isinstance(result, bool), \
       '''tweet.is_reply should return an bool, but returned {0}.''' \
       .format(type(result))


# Type check tweet.format_reply_to
result = tweet.format_reply_to('abcd', 'def')
assert isinstance(result, str), \
       '''tweet.format_reply_to should return an str, but returned {0}.''' \
       .format(type(result))


# Get the final values of the constants
constants_after = [tweet.MIN_LENGTH, tweet.MAX_LENGTH]

# Check whether the constants are unchanged.
assert constants_before == constants_after, \
       '''Your function(s) modified the value of constant MIN_LENGTH or
       MAX_LENGTH. Edit your code so that the values of constants are not 
       changed by your functions.'''
    

print("""

The type checker passed.

This means that the functions in tweet.py:
- are named correctly,
- take the correct number of arguments, and
- return the correct types.  

This does NOT mean that the functions are correct!

Be sure to thoroughly test your functions yourself before submitting.""")


# Check for use of functions print and input.

def disable_print(*args):
    raise Exception("You must not call built-in function print!")

def disable_input(*args):
    raise Exception("You must not call built-in function input!")

builtins.print = disable_print
builtins.input = disable_input
