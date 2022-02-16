import jageocoder
import json
jageocoder.init()
result=json.dumps((jageocoder.search('新宿区西新宿２－８－１')), ensure_ascii=False).encode('utf-8')
print(result.decode())