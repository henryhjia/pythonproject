#!/usr/bin/python3
import io

def get_occurrence_count(to_search, stream):
    """
    :param to_search: (String) The text to search for
    :param stream: (StringIO) An in-memory stream for text I/O
    :returns: (int) The number of lines that contain to_search
    """
    count = 0
    for str in stream:
      if to_search in str:
        count += 1
      
    return count

if __name__ == "__main__":
    stream = io.StringIO("Hey! How are you?\nI am good, how about you?\nI am good too.")
    print(get_occurrence_count('good', stream))
    stream.close()