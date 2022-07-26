from httpx import get

def cli():
    print(get('http://httpbin.org/get?arg=abacate').json()['args']['arg'])