import os
from whoosh.index import create_in,open_dir
from whoosh.fields import *
import json
# 创建schema, stored为True表示能够被检索
schema = Schema(title=ID(unique=True,stored=True,),
                dynasty=ID(stored=True),
                poet=ID(stored=True),
                content=TEXT(stored=False)
                )
indexdir = './indexdir'
if not os.path.exists(indexdir):
    os.mkdir(indexdir)
ix = open_dir(indexdir, schema=schema)
writer = ix.writer()
writer.update_document(title="title2", dynasty="dynasty", poet="poet", content="content")
writer.commit()
searcher = ix.searcher()
# 检索content中出现'明月'的文档
results = searcher.find("content", "content")
print('一共发现%d份文档。' % len(results))
for i in results:
    print(results)