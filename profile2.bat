SETLOCAL
set timestamp=%DATE:/=-%_%TIME::=-%
set timestamp=%timestamp: =%
pprofile --threads 0 --format callgrind --statistic 0 --verbose --out ./performance/%timestamp%.callgrind run.py
pause