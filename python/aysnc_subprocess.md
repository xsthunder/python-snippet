aysnc_subprocess
-----------
[rss-reborn/nbexp_watcher.py at master · xsthunder/rss-reborn](https://github.com/xsthunder/rss-reborn/blob/master/nb/nbexp_watcher.py)
```python
# https://docs.python.org/3/library/asyncio-subprocess.html
import asyncio
import sys
import datetime
import time

# https://stackoverflow.com/questions/44633458/why-am-i-getting-notimplementederror-with-async-and-await-on-windows
# asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

async def async_run(run_args=[sys.executable, '-c', "import time;print('ing',  flush=True);time.sleep(2);print('done')",]
                   , wait_child_sec=3):

    # Create the subprocess; redirect the standard output
    # into a pipe.
    proc = await asyncio.create_subprocess_exec(
        *run_args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    await asyncio.wait_for(proc.wait(), timeout=wait_child_sec)

    line=''

    data = await proc.stdout.read()
    line += data.decode('ascii').rstrip()

    line += '\n'

    data = await proc.stderr.read()
    line += data.decode('ascii').rstrip()

    if line: print(line)
    
date = asyncio.run(get_date([sys.executable, pyf,], 30))
```
