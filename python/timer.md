```
from datetime import datetime
import sys
def now():return mktime(datetime.now().timetuple())
def now_s():
    s = datetime.now().isoformat()
    return s[:s.index('.')]

def timer(slient_mode = False):
    """
    generator, returns (current_timestamp, current_timestamp - last_timestamp)
    support printing as spliter
    """
    pf = print
    def empty_func(*args):
        pass
    pf = empty_func if slient_mode else print
    
    def split_by_time(*args):
        pf("-"*60 , now_s(), *args)
    
    split_by_time()
    t1 = now()
    yield t1, 0
    
    while True:
        t2 = now()
        split_by_time("time costs %2d secs"%(t2 - t1))
        yield t2, t2 - t1
```
