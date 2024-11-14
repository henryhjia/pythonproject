"""
clearn files on disk
"""

import json
import argparse
from datetime import datetime, timedelta, timezone
from pathlib import Path
from collections import defaultdict


class CleanDiskFiles:
    JSON_KEY_TO_FIND = "setLaunchDate"
    DAYS_DELTA = 14

    def __init__(self, file_dir):
        self.json_dir = file_dir

    def compare_datetime(self, index, directory_path, json_file, json_data):
        """
        find setLaunchDate and compare it with current datetime. if it is DAYS_DELTA old, delete it from OS
        """
        pattern = json_file.name.rsplit(".", 2)[0] + "*"
        if CleanDiskFiles.JSON_KEY_TO_FIND in json_data:
            date_str = json_data[CleanDiskFiles.JSON_KEY_TO_FIND]
            json_date_tz = datetime.fromisoformat(date_str)
            current_time = datetime.now(timezone.utc)
            time_diff = current_time - json_date_tz
            if time_diff > timedelta(days=CleanDiskFiles.DAYS_DELTA):
                for file_path in directory_path.glob(pattern):
                    print(
                        f"{index} {json_file.name} {pattern} {json_date_tz} {current_time} > {CleanDiskFiles.DAYS_DELTA} days, REMOVE"
                    )
                    file_path.unlink()
            else:
                print(
                    f"{index} {json_file.name} {pattern} {json_date_tz} {current_time} < {CleanDiskFiles.DAYS_DELTA} days, KEEP"
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
    parser.add_argument("directory", type=Path, help="help text")
    args = parser.parse_args()

    my_obj = CleanDiskFiles(args.directory)
    my_obj.read_remove_json_file()
    my_obj.purge_other_files("aaa*.csv")


print("done")
