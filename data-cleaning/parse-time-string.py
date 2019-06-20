# conda install python-dateutil
# @see https://dateutil.readthedocs.io/en/stable/
import dateutil.parser
from dateutil import rrule
(START_TIME, END_TIME)=('出生日期', '首诊MCU时间')
def  per_row(r):
    parse = dateutil.parser.parse
    index, row  = r
    start_time = row.get(START_TIME)
    end_time = row.get(END_TIME)
    start_time = parse(start_time)
    end_time = parse(end_time)
    return rrule.rrule(rrule.YEARLY, dtstart=start_time, until=end_time).count()
list(map(per_row, df.iterrows()))
