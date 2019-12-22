# bigdata-course-project
There are solutions for three tasks in my Big Data course porject.

## Task 01
There are three files in `task01`.

Please make sure your file path in HDFS, and put your file path of text corpus into the `-input` in `run01.sh`. 

Use `time` command to record the running time:
```
time sh run01.sh
```
By my MapReduce system, the output showed: 
```
real 8m50.352s
user 0m6.884s
sys 0m0.544s
```

## Task 02
There are three files in `task02`. Please make sure your file path in HDFS, and put your file path of text corpus into the `-input` in `run02.sh`.

**What I have to mention is that:**
* First, the function `environ` in package `os`.  
```
import os
```

* Besides, `"mapreduce_map_input_file"` and `"map_input_file"` in `os.environ` are similar. To prove this, I used these two in different files in task02 and task03 separately. 

After setting your file path in `run02.sh`, you could command: 
```
./run02.sh
```

## Task 03
See file `task03`. There are nine files in this three-step task. You could realize it by the file names. 

**What I have to mention is that:**
* The original text corpus cannot be used if you still use commas to split variables. Because of the commas in these filenames, the `.split(',', 1)` function will be confused. 
* So, there are two methods: 
    * Remove these commas in filenames firstly. 
    * **Use another separator which is not in filenames, like `/`. (Better Choice)** 
* Besides, the output from `run0301.sh` is the input of `run0302.sh`, and output of `run0302.sh` is the input of `run0303.sh`. 

Then after setting your file path in these `.sh`, you could separately command: 
```
./run0301.sh
```
```
./run0302.sh
```
```
./run0303.sh
```
