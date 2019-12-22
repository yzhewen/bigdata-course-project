hadoop jar /home/uic/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-*streaming*.jar \
-file /home/uic/bd-project/task01/mapper01.py -mapper /home/uic/bd-project/task01/mapper01.py \
-file /home/uic/bd-project/task01/reducer01.py -reducer /home/uic/bd-project/task01/reducer01.py \
-input /data/bd_project/textcorpus2/ -output /output/bd_project/task01/
