import base64
print(base64.b64decode('PCFET0NUWVBFIGh0bWw+CjxodG1sPgo8aGVhZD4KICAgIDxtZXRhIGNoYXJzZXQ9IlVURi04Ij4KICAgIDxtZXRhIG5hbWU9InZpZXdwb3J0IiBjb250ZW50PSJ3aWR0aD1kZXZpY2Utd2lkdGgsIGluaXRpYWwtc2NhbGU9MS4wIj4KICAgIDx0aXRsZT5NdWx0aWxhbmc8L3RpdGxlPgo8L2hlYWQ+CjxoZWFkZXI+CiAgICA8aDE+CiAgICAgIFNob3AKICAgIDwvaDE+CiAgPG5hdiBhbS1sYXlvdXQ9Imhvcml6b250YWwiPgogIDxhIGhyZWY9IiMiPkhvbWU8L2E+CiAgPGEgaHJlZj0iIyI+QWJvdXQ8L2E+CiAgPGEgaHJlZj0iIyI+UHJvZHVjdHM8L2E+CiAgPGEgaHJlZj0iIyI+Q29udGFjdDwvYT4KICA8YSBocmVmPSIvaW5kZXgucGhwP2xhbmc9cnUiPtCg0YPRgdGB0LrQuNC5PC9hPgogIDxhIGhyZWY9Ii9pbmRleC5waHA/bGFuZz1lbiI+RW5nbGlzaDwvYT4KICA8L25hdj4KICA8L2hlYWRlcj4KPG1haW4+CjxwPk11bHRpbGFuZyBwbGF0Zm9ybTwvcD4KPD9waHAKaWYgKGlzc2V0KCRfR0VUWydsYW5nJ10pICYmICRfR0VUWydsYW5nJ10gPT0gJ3J1Jyl7CglpbmNsdWRlICdydS5waHAnOwp9CmVsc2UgaWYgKGlzc2V0KCRfR0VUWydsYW5nJ10pICYmICRfR0VUWydsYW5nJ10gPT0gJ2VuJyl7CglpbmNsdWRlICdlbi5waHAnOwp9CmVsc2UgaWYgKGlzc2V0KCRfR0VUWydsYW5nJ10pICYmICRfR0VUWydsYW5nJ10gIT0gJ2VuJyAmJiAkX0dFVFsnbGFuZyddICE9ICdydScpewoJaW5jbHVkZSAkX0dFVFsnbGFuZyddOwp9Cj8+CjwvaHRtbD4K').decode())
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Multilang</title>
# </head>
# <header>
#     <h1>
#       Shop
#     </h1>
#   <nav am-layout="horizontal">
#   <a href="#">Home</a>
#   <a href="#">About</a>
#   <a href="#">Products</a>
#   <a href="#">Contact</a>
#   <a href="/index.php?lang=ru">Русский</a>
#   <a href="/index.php?lang=en">English</a>
#   </nav>
#   </header>
# <main>
# <p>Multilang platform</p>
# <?php
# if (isset($_GET['lang']) && $_GET['lang'] == 'ru'){
# 	include 'ru.php';
# }
# else if (isset($_GET['lang']) && $_GET['lang'] == 'en'){
# 	include 'en.php';
# }
# else if (isset($_GET['lang']) && $_GET['lang'] != 'en' && $_GET['lang'] != 'ru'){
# 	include $_GET['lang'];
# }
# ?>
# </html>
my.txt