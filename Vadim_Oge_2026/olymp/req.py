import requests
url = "http://ctfinf.ru:10019/"
s = requests.Session()
l = [150, 108, 71, 620, 71, 196, 299, 516, 132, 508, 17, 132, 287, 71, 307, 17, 132, 37, 287, 174, 307, 17, 274, 196, 132, 57]
for x in l:
    gt = s.get(url+f"get_by_pos?pos={x}")
    print(chr(int(gt.text.strip('"'), 16)), end='')