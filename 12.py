import requests
import itertools
from bs4 import BeautifulSoup
from collections import defaultdict 
from math import comb
import math
from functools import reduce # Valid in Python 2.6+, required in Python 3
import operator

resp = requests.get('https://t5k.org/lists/small/100000.txt')
soup = BeautifulSoup(resp.text, 'html.parser')
primes = soup.get_text().strip().splitlines()[8:-1]
for i,val in  enumerate(primes):
    primes[i] = [int(_) for _ in val.strip().split() if _ is not None and len(_)>0]

primes = list(itertools.chain.from_iterable(primes))
number = 0
origin_number = 0
n = 5
while True:
    current_primes = defaultdict(lambda : 0)
    origin_number = number = int(n*(n+1)/2 )
    for i in primes: 
        if i > math.sqrt(origin_number):
            break
        while number % i == 0:
            number /= i
            current_primes[i] += 1
        if i > number:
            break
    keys    = current_primes.keys()
    values = current_primes.values()
    if reduce(operator.mul, [_ + 1 for _ in values],1)>=500 :
        break
    n+=1
print(n,origin_number)
