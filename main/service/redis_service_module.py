import redis
import json


class redis_service(object):
    def __init__(self):
        self.host = "localhost"
        self.port = 6379

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
            ret_dict['aid'] = aid
            ret_dict['tag'] = ret_dict['tag'].split(",")
            return ret_dict
        except Exception as e:
            print(f"Error: Redis get_article_by_id failed:\n{str(e)}")
            return error_dict


class FilePathError(Exception):
    pass

class FileOpenError(Exception):
    pass
