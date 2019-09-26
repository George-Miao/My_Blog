import redis
import json
import datetime
import requests
import markdown


class RedisService(object):
    def __init__(self):
        self.host = "localhost"
        self.port = 6379
        self.r = None

    def load_json(self, path):
        if path.suffix != ".json":
            raise FilePathError
        try:
            with open(path) as json_file:
                json_file = json.load(json_file)
                try:
                    self.host = json_file['host']
                    self.port = json_file['port']
                except Exception as e:
                    print(e)
        except:
            raise FileOpenError

    def connect(self, in_password=None):
        try:
            self.r = redis.Redis(
                host=self.host,
                port=self.port,
                decode_responses=True
            )
        except Exception as e:
            print("Error: Redis connect failed:\n")
            print(e)

    def get_article_by_id(self, aid):
        if self.r == None:
            raise RedisNotConnected('''
                You need to connect to a redis server first\n
                Use connect() to connect
            ''')
        error_dict = {
            'aid': 0,
            'day': "error",
            'month': "error",
            'title': "error",
            'tag': ["error"],
            'viewNumber': "error",
            'commentNumber': "error",
            'content': "error",
        }
        try:
            ret_dict = self.r.hgetall(aid)
            if ret_dict == None:
                return error_dict
            ret_dict['tag'] = ret_dict['tag'].split(",")
            return ret_dict
        except Exception as e:
            print(f"Error: Redis get_article_by_id failed:   {str(e)}")
            return error_dict

    def add_new_article(self, article):
        if self.r == None:
            raise RedisNotConnected('''
                You need to connect to a redis server first\n
                Use connect() to connect    
            ''')
        try:
            self.r.incr('count')
            aid = self.r.get('count')
            time = datetime.datetime.strptime(
                article['time'], '%Y-%m-%dT%H:%M:%SZ')
            content = requests.get(article['content']).text
            content = markdown.markdown(content)
            new_article = {
                'aid': aid,
                'day': time.day,
                'month': self.month2str(time.month),
                'title': article['name'],
                'tag': 'Testing',
                'viewNumber': 0,
                'commentNumber': 0,
                'content': content,
                'src': article['content']
            }
            self.r.hmset(aid, new_article)
        except Exception as e:
            print(str(e))

    def get_count(self):
        return self.r.get('count')

    def month2str(self, int):
        a = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
             'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        return a[int-1]


class RedisNotConnected(Exception):
    pass


class FilePathError(Exception):
    pass


class FileOpenError(Exception):
    pass
