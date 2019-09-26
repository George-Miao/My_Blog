from dropbox import Dropbox
from markdown import Markdown
from . import cache


class DBService(Dropbox):
    def __init__(self, token):
        try:
            self.db = super().__init__(token)
            self.user = self.users_get_current_account()
            self.md = Markdown(extensions=['markdown.extensions.fenced_code', 'markdown.extensions.tables'])
        except Exception as e:
            print('[!]' + e)

    @cache.memoize(make_name=lambda x: f'file_{x}')
    def request_file(self, file_path):
        return self.md.convert(self.files_download(file_path)[1].content.decode('utf-8'))

    def request_file_list(self, start_id=0, end_id=None):
        pass

    @cache.cached(key_prefix='file_list')
    def request_list(self):
        return {file.name: [file.path_lower, file.client_modified] for file in self.files_list_folder('').entries}
