hadoop jar /home/uic/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-*streaming*.jar \
-file /home/uic/bd-project/task03/mapper0302.py -mapper /home/uic/bd-project/task03/mapper0302.py \
-file /home/uic/bd-project/task03/reducer0302.py -reducer /home/uic/bd-project/task03/reducer0302.py \
-input /output/bd_project/task03/task0306/part-00000 -output /output/bd_project/task03/task0402/

