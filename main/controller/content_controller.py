from . import controller
from flask import request


@controller.route("/content")
def get_content():
    ret_dict = {
    day: 4,
    month: "jul",
    title: "一个很长很长很长很长很长很长很长很长的测试标题",
    tag: ["测试", "中文"],
    viewNumber: 10,
    commentNumber: 0,
    content: "<a>这一个测试</a><img alt = 'test pic' src = 'https://restver.me/assets/images/js-app-invoke/res.jpg'/>",
    }
    id = request.args['id']
    return ret_dict
