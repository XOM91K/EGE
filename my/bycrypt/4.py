import requests, re
#http://ctfinf.ru:10004
[hex(d)[2:] d for d in list('YEAH'.encode())]
s = requests.session()
for x in range(1, 101):
    gt = s.get("http://ctfinf.ru:10014/").text
    counts = re.findall(r'<h3>.+?</h3>', gt)
    print(counts[0])
    #print(gt)
    evals = re.findall(r'<div style="text-align: center;">\s+(.+?)\s+</div>', gt, re.DOTALL)
    evalss = eval(evals[0])
    print(evals, evalss)
    pst = s.post("http://ctfinf.ru:10014/", data={'answer': evalss})
    #print(evals, evalss, pst.text)
gt = s.get("http://ctfinf.ru:10014/").text
print(gt)