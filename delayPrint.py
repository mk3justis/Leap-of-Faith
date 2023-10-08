import sys
import time


def delay_print(*s) :
    for string in s :
        for c in string:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.02)
            
def delay_print_slow(*s) :
    for string in s :
        for c in string:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.08)            
            
def delay_print_slowest(*s) :
    for string in s :
        for c in string:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.14)