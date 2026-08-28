import pickle, base64
print(pickle.loads(base64.b64decode('gASVwAAAAAAAAABdlCh9lCiMBG5hbWWUjCrQntCx0YvRh9C90YvQuSDQvNC+0YDRgdC60L7QuSDQvtCz0YPRgNC10YaUjAVjb3VudJRLAowEZ2xvd5SJdX2UKGgCjDDQodCy0LXRgtGP0YnQuNC50YHRjyDQvNC+0YDRgdC60L7QuSDQvtCz0YPRgNC10YaUaARLAWgFiHV9lChoAowh0JrQvtGA0LDQu9C70L7QstGL0Lkg0L7Qs9GD0YDQtdGGlGgESwNoBYl1ZS4=')))
import pickle, base64
lst = [{'name': '{{4*9}}', 'count': 'config', 'glow': False}, {'name': 'Светящийся морской огурец', 'count': 1, 'glow': True}, {'name': 'Коралловый огурец', 'count': 3, 'glow': False}]
print(base64.b64encode(pickle.dumps(lst)).decode())
print(eval('2 + 2 + 2'))