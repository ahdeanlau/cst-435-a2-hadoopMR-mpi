# CST435

run this command to test result: `python mapper.py daily.csv | python reducer.py`

read this [guide](https://medium.com/@rrfd/your-first-map-reduce-using-hadoop-with-python-and-osx-ca3b6f3dfe78) to know what are these two mapper and reducer doing

run this command to test `mapreduce.py`: `python mapreduce.py daily.csv`


## What's the difference `mapper.py` & `reducer.py` VS `mapreduce.py`?

`mapper.py` and `reducer.py` simple scripts designed to manually handle the "map" and "reduce" phase of the MapReduce process. It processes input data line by line, emits key-value pairs.

`mapreduce.py`: A complete MapReduce job implemented using the `mrjob` library, which abstracts much of the complexity of running MapReduce.
