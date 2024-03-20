
import math
import os
import random
import re
import sys
from collections import Counter

def sockMerchant(n, ar):
    counter = 0
    for val in Counter(ar).values():
        counter+=val//2
    return counter

print(sockMerchant(input(), input()))

