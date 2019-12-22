hadoop jar /home/uic/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-*streaming*.jar \
-file /home/uic/bd-project/task03/mapper0303.py -mapper /home/uic/bd-project/task03/mapper0303.py \
-file /home/uic/bd-project/task03/reducer0303.py -reducer /home/uic/bd-project/task03/reducer0303.py \
-input /output/bd_project/task03/task0401/part-00000 -output /output/bd_project/task03/task0501/

