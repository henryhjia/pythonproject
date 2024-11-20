"""
Clearn files on disk

CASE 1:
Read datetime from json "setLaunchDate", 
if it is less than 2 weeks from provided last_date, keep it
if it is older than 2 weeks from provided last_date, delete it (as well as any
    other files with the same pattern, e.g. cm2*)

pattern: if file is cm2.csv.json, the patten is cm2*.  

input files:
cm1.csv.json:

{"a": 1, "b":2, "setLaunchDate": "2024-11-06T12:57:39+00:00"}

cm1.csv
- a csv file


cm2.xml.json
{"a": 1, "b":2, "setLaunchDate": "2024-11-12T12:57:39+00:00"}

cm2.xml
 - a xml file

CASE 2: 
-rw-rw-r-- 1 henryjia henryjia  8 Nov 20 10:24 aaa1_2024-10-10.csv
-rw-rw-r-- 1 henryjia henryjia 10 Nov 20 10:24 aaa1_2024-11-02.csv
-rw-rw-r-- 1 henryjia henryjia 11 Nov 20 10:24 aaa1_2024-11-08.csv
-rw-rw-r-- 1 henryjia henryjia 11 Nov 20 10:24 aaa2_2024-11-01.csv
-rw-rw-r-- 1 henryjia henryjia 11 Nov 20 10:24 aaa2_2024-11-08.csv
-rw-rw-r-- 1 henryjia henryjia 11 Nov 20 10:24 aaa3_2024-10-30.csv
-rw-rw-r-- 1 henryjia henryjia 11 Nov 20 10:24 aaa3_2024-11-08.csv

It will keep the file with latest datetime in the file name.  In this case,
these are kept:

aaa1_2024-11-08.csv
aaa2_2024-11-08.csv
aaa3_2024-11-08.csv

Rest files are deleted.
File contents can be anything

All data are backed up in ../data/

"""

import json
import argparse
from datetime import datetime, timedelta, timezone
from pathlib import Path
from collections import defaultdict


class CleanDiskFiles:
    JSON_KEY_TO_FIND = "setLaunchDate"
    DAYS_DELTA = 14

    def __init__(self, file_dir:str, last_date:str):
        self.json_dir = file_dir
        self.last_date = last_date

    def compare_datetime(self, index, directory_path, json_file, json_data):
        """
        find setLaunchDate and compare it with current datetime. if it is DAYS_DELTA old, delete it from OS
        """
        pattern = json_file.name.rsplit(".", 2)[0] + "*"
        if CleanDiskFiles.JSON_KEY_TO_FIND in json_data:
            date_str = json_data[CleanDiskFiles.JSON_KEY_TO_FIND]
            json_date_tz = datetime.fromisoformat(date_str)
            current_time = datetime.fromisoformat(self.last_date).replace(tzinfo=timezone.utc)
            time_diff = current_time - json_date_tz
            if time_diff > timedelta(days=CleanDiskFiles.DAYS_DELTA):
                for file_path in directory_path.glob(pattern):
                    print(
                        f"{index} {json_file.name} pattern={pattern} {json_date_tz} {current_time} > {CleanDiskFiles.DAYS_DELTA} days, REMOVE"
                    )
                    file_path.unlink()
            else:
                print(
                    f"{index} {json_file.name} pattern={pattern} {json_date_tz} {current_time} < {CleanDiskFiles.DAYS_DELTA} days, KEEP"
                )

    def read_remove_json_file(self):
        """
        read json file one at the time, retrieve json content
        """
        directory_path = Path(self.json_dir)
        for i, json_file in enumerate(directory_path.glob("*.json")):
            with open(json_file) as file:
                json_data = json.load(file)
                self.compare_datetime(i, directory_path, json_file, json_data)

    def purge_other_files(self, filename):
        """
        remove older files based on the date in the filename
        """
        directory_path = Path(self.json_dir)
        date_file_dict = defaultdict(list)
        latest_date = None
        for i, to_be_deleted_file in enumerate(directory_path.glob(filename)):
            date_str = to_be_deleted_file.name.split(".")[0].split("_")[-1]
            this_date = datetime.strptime(date_str, "%Y-%m-%d")
            date_file_dict[this_date].append(to_be_deleted_file)
            if latest_date is None or this_date >= latest_date:
                latest_date = this_date

        for key, value in date_file_dict.items():
            if key != latest_date:
                for item in value:
                    item.unlink()
                    print(f"{key} {item} deleted")
            else:
                for item in value:
                    print(f"{key} {item} kept")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=Path, help="directory where data locates")
    parser.add_argument("last_date", type=str, help="Date of last report e.g. '2024-11-15'")
    args = parser.parse_args()

    my_obj = CleanDiskFiles(args.directory, args.last_date)
    my_obj.read_remove_json_file()
    my_obj.purge_other_files("aaa*.csv")


print("done")
