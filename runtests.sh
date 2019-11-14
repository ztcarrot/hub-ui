# -m Major for Major test cases
# -n 2 for thread number
# --count 1 for repeat times
# -s
# -v
python3 -m pytest -m Major tests -s -v -n 2 --html=report.html --count 1
