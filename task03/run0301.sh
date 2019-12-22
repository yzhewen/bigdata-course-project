hadoop jar /home/uic/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-*streaming*.jar \
-file /home/uic/bd-project/task03/mapper0301.py -mapper /home/uic/bd-project/task03/mapper0301.py \
-file /home/uic/bd-project/task03/reducer0301.py -reducer /home/uic/bd-project/task03/reducer0301.py \
-input /data/bd_project/textcorpus/ -output /output/bd_project/task03/task0301/

