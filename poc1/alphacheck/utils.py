'''
text manipulation utils for text-service api
'''
import string


VERSION_REGISTRY = {}

def version(num):
    '''
    decorator to handle registering a specific version of a function
    '''
    def decorator(func):
        VERSION_REGISTRY['v%d' % num] = func
        return func
    return decorator

def has_all_alphabet(query, **kw):
    '''
    checks to see if a string has every letter of the alphabet
    '''
    vers = kw.pop('version')
    return VERSION_REGISTRY[vers](query, **kw)

def _handle_case(query, case_insensitive):
    '''
    returns the query and alphabet depending on whether case sensitivity is enabled
    '''
    if case_insensitive:
        return query.lower(), string.ascii_lowercase
    return query, string.ascii_letters

@version(1)
def has_all_alphabet_v1(query, case_insensitive=False):
    '''
    returns true if input query contains every letter of the alphabet
    '''
    query, alphabet = _handle_case(query, case_insensitive)
    letters = {}
    for letter in query:
        if letter in alphabet:
            letters.setdefault(letter, True)
    return len(letters.keys()) == len(alphabet)

@version(2)
def has_all_alphabet_v2(query, case_insensitive=False):
    '''
    returns true if input query contains every letter of the alphabet
    '''
    query, alphabet = _handle_case(query, case_insensitive)
    return len(set(alphabet).intersection(set(query))) == len(alphabet)
