import jageocoder
import json
jageocoder.init()
search_string='新宿区西新宿２－８－１'
result=json.dumps((jageocoder.search(search_string)), ensure_ascii=False).encode('utf-8')
print(result.decode())