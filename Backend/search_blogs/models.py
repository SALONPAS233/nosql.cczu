from elasticsearch_dsl import Text, Date, Keyword, Integer, Document, Completion, Double, Float
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import analyzer
import sys
sys.path.append("C:/Users/15747/Desktop/xiu-search-main")
from config import ES_HOST


# Create your models here.
connections.create_connection(hosts=ES_HOST)

my_analyzer = analyzer('ik_smart')

class BlogsIndex(Document):
    suggest = Completion(analyzer=my_analyzer)
    title = Text(analyzer="ik_max_word")
    keywords = Text(analyzer="ik_max_word")
    description = Text(analyzer="ik_max_word")
    content = Text(analyzer="ik_max_word")
    PR = Float()
    publish_time = Date()

    class Index:
        name = 'blogs'

if __name__=='__main__':
    BlogsIndex.init()