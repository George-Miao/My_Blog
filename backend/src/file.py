import logging
from typing import Union
from pathlib import Path

from marko import convert
from bs4 import BeautifulSoup
from aiofile import AIOFile
from result import Ok, Err, Result

lg = logging.getLogger("Glog")
logging.basicConfig(format="[%(asctime)s][%(name)s] %(message)s", level="INFO")

FILE_PATH = Union[Path, str]
GET_RESULT = Result['FileMeta', Exception]


class FileMeta:
    __slots__ = ("__name", "__cat", "__dir")

    def __new__(cls, *args, **kwargs):
        if cls == FileMeta:
            raise NotImplementedError("Do not use FileMeta directly, use `CategorizedFile` or `UnCategorizedFile`")

    def __init__(self, fp: FILE_PATH):
        if not fp.exists():
            raise FileNotFoundError("Cannot find {}".format(fp))
        self.__name = fp.name
        lg.info(f"Found Markdown file {self.__name}")
        self.__dir = fp

    @staticmethod
    async def __get_desc(content, limit: int = 30):
        content = BeautifulSoup(content, features="lxml")
        ret = []
        leng = 0
        for x in content.strings:
            if x := x.replace("\n", "").strip().split():
                if leng > limit:
                    if not ret[-1].endswith("."):
                        ret.append("...")
                    break
                ret.extend(x)
                leng += x.__len__()
        return repr(" ".join(ret))

    @property
    async def md(self) -> Result:
        try:
            async with AIOFile(self.__dir, 'r') as f:
                return Ok(await f.read())
        except Exception as e:
            return Err(e)

    @property
    async def content(self) -> Result:
        try:
            md = await self.md
            if md.is_err():
                return md
            else:
                md = md.unwrap()
            html = convert(md)
            desc = self.__get_desc(html)
            return Ok((html, await desc))
        except Exception as e:
            return Err(e)

    def __repr__(self):
        return "FileMeta<{}>".format(self.__name)


class CategorizedFile(FileMeta):
    __slots__ = "__cat"

    def __init__(self, fp):
        super().__init__(fp)
        self.__cat = fp.parent.name


class UnCategorizedFile(FileMeta):
    __slots__ = "__cat"

    def __init__(self, fp):
        super().__init__(fp)
        self.__cat = "uncategorized"


class FileService:
    def __init__(self, fp: FILE_PATH = Path.home() / "Dropbox"):
        if isinstance(fp, str):
            fp = Path(fp)
        if not fp.exists():
            raise RuntimeError(f"{fp.absolute()} doest not exists")
        if not fp.is_dir():
            raise RuntimeError(f"{fp.absolute()} is not a directory")
        self._fp: Path = fp
        self._file_list = self._load_file_list()
        lg.info("FileService @ `{}`".format(self._fp.absolute()))

    @staticmethod
    def __format(fn: str):
        return fn.replace(" ", "_").lower()

    @staticmethod
    def __unformat(fn: str):
        return fn.replace("_", " ")

    def __format_all(self, *string):
        return (self.__format(x) for x in string)

    """
    def __init_files(self):
        self._file_dict = {"uncategorized": {}}
        for f in self._fp.glob("*/*.md"):
            self.__new_file(f)
        for f in self._fp.glob("*.md"):
            self.__new_file(f, True)

    def __new_file(self, f: FP, uncat=False):
        stem = self.__format(f.stem)
        if uncat:
            self._file_dict["uncategorized"][stem] = FileMeta(f)
        else:
            parent = self.__format(f.parent.name)
            if parent in self._file_dict:
                self._file_dict[parent][stem] = FileMeta(f)
            else:
                self._file_dict[parent] = {stem: FileMeta(f)}

    def get(self, name: str, cat: str = "uncategorized") -> Result[Union[FileMeta, Exception]]:
        try:
            cat, name = self.__format_all(cat, name)
            return Ok(self._file_dict[cat][name])
        except Exception as e:
            return Err(e)

    def delete(self, pt: Path) -> Result:
        if not self._is_md(pt): return Err("Not a markdown file")
        if (stem := pt.stem) in self._file_dict["uncategorized"]:
            del self._file_dict["uncategorized"][stem]
        elif (cat := pt.parent.name) in self._file_dict:
            del self._file_dict[cat][pt.stem]
        else:
            return Err("Cannot find {}".format(pt.absolute()))
        return Ok()
        
    def _get_event_handler(self):
            class Handler(FileSystemEventHandler):
                def on_created(sf, event: FileSystemEvent):
                    pt = Path(event.src_path)
                    if pt.suffix.lower() != ".md": return
                    self.__new_file(pt)
    
                def on_update(sf, event: FileSystemEvent):
                    pt = Path(event.src_path)
                    if pt.suffix.lower() != ".md": return
                    self.__new_file(pt)
    
                def on_deleted(self, event: FileSystemEvent):
                    pt = Path(event.src_path)
                    if
        """

    @staticmethod
    def _is_md(pt):
        return pt.suffix.lower() == ".md"

    def get(self, name: str, cat: str = None) -> GET_RESULT:
        try:
            if cat:
                return Ok(CategorizedFile(self._fp / cat / name))
            else:
                return Ok(UnCategorizedFile(self._fp / name))
        except Exception as e:
            return Err(e)


""""""


@property
def dict(self):
    return self._file_dict
