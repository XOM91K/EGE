import ipaddress
for x in ipaddress.ip_network('11.92.135.56/255.224.0.0', 0):
    print(x)
# самый первый адрес и самый последний не назнчаются
# компьютерам