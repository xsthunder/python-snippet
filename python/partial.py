from functools import partial
import sys 
eprint = partial(print, file=sys.stderr)
eprint("err")
