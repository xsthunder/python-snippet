rss-reborn/nbexp_watcher.py at master · xsthunder/rss-reborn
https://github.com/xsthunder/rss-reborn/blob/master/nb/nbexp_watcher.py

```python
from datetime import datetime
import time
import sys
def now():return datetime.now()
def now_s():
    s = datetime.now().isoformat()
    return s[:s.index('.')]

def timer(slient_mode = False):
    """
    Usage:
    time = iter(timer())
    next(time) # print
    # do something
    next(time) # print
    printing as spliter
    generator, returns (current_timestamp, current_timestamp - last_timestamp)
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
        split_by_time( "total " + dt.__str__() + " spent")
        yield t2, t2 - t1
```
