
from whoosh.index import open_dir
 
ix = open_dir("./indexdir")
# 创建一个检索器
searcher = ix.searcher()
# 检索content中出现'明月'的文档
results = searcher.find("content", "content2")
print('一共发现%d份文档。' % len(results))
print(results)