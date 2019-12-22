hadoop jar /home/uic/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-*streaming*.jar \
-file /home/uic/bd-project/task02/mapper02.py -mapper /home/uic/bd-project/task02/mapper02.py \
-file /home/uic/bd-project/task02/reducer02.py -reducer /home/uic/bd-project/task02/reducer02.py \
-input /data/bd_project/textcorpus2/ -output /output/bd_project/task02/
