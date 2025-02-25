# s = ['Никита', 'Тимофей', 'Ян', 'Борис']
# print(len(max(s, key=len)))
import re
s = '<a id="" class="button" href="/tasks/ofType/ege/4" onclick="reroute(&quot;/tasks/ofType/ege/4&quot;); return false">4</a>'
m = re.findall(r'href\s*=\s*"(.*?)"', s)
print(m)