SETLOCAL
set timestamp=%DATE:/=-%_%TIME::=-%
set timestamp=%timestamp: =%
yappi -f pstat -o ./performance/%timestamp%.pstat run.py
snakeviz ./performance/%timestamp%.pstat
