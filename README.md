# CST435

run this command to test result: `python mapper.py daily.csv | python reducer.py`

read this [guide](https://medium.com/@rrfd/your-first-map-reduce-using-hadoop-with-python-and-osx-ca3b6f3dfe78) to know what are these two mapper and reducer doing

run this command to test `mapreduce.py`: `python mapreduce.py daily.csv`


## What's the difference `mapper.py` & `reducer.py` VS `mapreduce.py`?


`mapper.py` and `reducer.py` are lightweight standalone mappreduce manual script which is ideal for integration into traditional Hadoop Streaming pipelines or custom workflows without requiring external libraries.

`mapreduce.py`: A comprehensive, self-contained MapReduce implementation leveraging mrjob, suitable for developers looking for ease of use, flexibility, and local testing.
