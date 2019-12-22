# bigdata-course-project
There are solutions for three tasks in my Big Data course porject. 

**Mention: The punctuations in texts are not considered. You could use `.replace()` or `re.sub()` in these `mapper.py` files to realize some transformation.**

## Task 01
There are three files in `task01`.

Please make sure your file path in HDFS, and put your file path of text corpus into the `-input` in `run01.sh`. 

Use `time` command to record the running time:
```
time sh run01.sh
```
By my MapReduce System, the output showed: 
```
real 8m50.352s
user 0m6.884s
sys 0m0.544s
```
Use `hdfs dfs -cat OUTPUT_PATH/part-00000` command to check the outputs: 
```
...
a	330283
aaron	113
...
abductions	2
abductor	3
abductors	2
...
```

## Task 02
There are three files in `task02`. 

Please make sure your file path in HDFS, and put your file path of text corpus into the `-input` in `run02.sh`.

**What I have to mention is that:**
* Firstly, the function `environ` in package `os`.  
```
import os
```

* Besides, `"mapreduce_map_input_file"` and `"map_input_file"` in `os.environ` are similar. To prove this, I used these two in different files in `task02` and `task03` separately. 

After setting your file path in `run02.sh`, you could command: 
```
./run02.sh
```
Use `hdfs dfs -cat OUTPUT_PATH/part-00000` command: 
```
...
trouvent	{'Andrew-Lang___Old-Friends---Essays-in-Epistolary-Parody.txt': [2664, 2652]}
...
remarks?    {'Anthony-Trollope___He-Knew-He-Was-Right.txt': [34777]}
remarks;    {'Abraham-Lincoln___The-Writings-of-Abraham-Lincoln-Volume-5--1858-1862.txt': [6824], 'Beatrix-Potter___The-Tale-of-Johnny-Town-Mouse.txt': [61], 'Ambrose-Bierce___The-Devilss-Dictionary.txt': [571], 'Andrew-Lang___John-Knox-and-the-Reformation.txt': [7700], 'Anthony-Trollope___Miss-Mackenzie.txt': [8592]}
...
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
Use `hdfs dfs -cat OUTPUT_PATH/part-00000` command: 
```
...
lowering,Anthony-Trollope___The-Prime-Minister.txt	7.28318916935e-07
lowering,Andrew-Lang___The-Grey-Fairy-Book.txt	2.08061697229e-06
lowering,Anthony-Trollope___Life-of-Cicero-Volume-One.txt	1.68287839521e-06
unlearned,Andrew-Lang___Essays-in-Little.txt	8.18022675589e-06
unlearned,Andrew-Lang___Letters-to-Dead-Authors.txt	1.36579266053e-05
unlearned,Alexander-Pope___The-Works-of-Alexander-Pope,-Volume-1.txt	2.48569619932e-06
unlearned,Anthony-Trollope___Lady-Anna.txt	3.42462756224e-06
...
```
