"""
calculate date range 
end_date = today or specific day
start_date = end_date - delta
"""

import json
import argparse
from datetime import datetime, timedelta, timezone
from pathlib import Path
from collections import defaultdict
from typing import Union

class DateRange:

    DAYS_DELTA = 14

    def __init__(self, file_dir):
        self.json_dir = file_dir

    def get_date_range(self, begin_days=14, start_weekday: Union[str,int] = None, max_day=None) -> tuple[datetime, datetime]:
        begin_date = None
        end_date = None
        return begin_date, end_date


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument("directory", type=Path, help="help text")
    args = parser.parse_args()
    print(f'args={args}')
    
    my_obj = DateRange(args)
    begin, end = my_obj.get_date_range()
    print(f'begin={begin} end={end}')

