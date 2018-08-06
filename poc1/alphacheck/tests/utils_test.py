import random
import string


def test_v1():
    from alphacheck import utils
    assert utils.has_all_alphabet_v1(string.ascii_letters)

    assert not utils.has_all_alphabet_v1(string.ascii_lowercase)
    assert utils.has_all_alphabet_v1(string.ascii_lowercase, case_insensitive=True)

    assert not utils.has_all_alphabet_v1(string.ascii_uppercase)
    assert utils.has_all_alphabet_v1(string.ascii_uppercase, case_insensitive=True)

    assert utils.has_all_alphabet_v1(string.ascii_letters * 2)

    r = random.choice(string.ascii_letters)
    s = [x for x in string.ascii_letters if x != r]
    assert len(s) == len(string.ascii_letters) - 1
    assert not utils.has_all_alphabet_v1(''.join(s))
