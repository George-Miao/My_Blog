$(function () {
    var sample_block = $(".block").clone()
    $(".block").remove()

    if (isMobile()) {
        alert('你正在使用移动客户端，可能会有页面显示bug，推荐使用电脑端访问')
        $('#top').css('height', '960px')
        $('.top-cover').css({ 'top': '700px', 'bottom': 'auto' })
    }

    set_float_pos()

    var mas_container = $('#mid-content').masonry({
        itemSelector: '.block',
        gutter: 15,
        stagger: 30,
        animate: false,
        transitionDuration: 0,
    })

    var article_number

    $.ajax({
        url: "/api/get_count",
        async: false,
        success: function (e) {
            article_number = e
            if (article_number > 10) { article_number = 10 }
        },
        error: function (xhr) {
            alert("Get article number error： " + xhr.status + " " + xhr.statusText)
        }
    })

    for (var aid = 1; aid <= article_number; aid++) {
        $.ajax({
            async: false,
            url: "/api/content?id=" + aid,
            success: function (result) {
                add_block(mas_container, sample_block, result)
            },
            error: function (xhr) {
                alert("Get article error： " + xhr.status + " " + xhr.statusText)
            }
        })
    }
})

window.onload = function () {
    if (true) {
        console.log('load completed')
        $('#content').css('opacity', 1)
        $('#content').css('z-index', '101')
        $('.cover').css('opacity', 0)
    }
}

window.onresize = function () {
    set_float_pos()
}

window.addEventListener('scroll', function () {
    set_float_pos()
})

function add_block(container, outter_block, content) {
    var block = outter_block.clone()
    block.attr("id", content['aid'])
    block.children(".block-date").children(".day").text(content["day"])
    block.children(".block-date").children(".month").text(content["month"])
    block.children(".block-title").text(content["title"])
    var tags = block.children(".block-description").children(".tag")
    for (var tag_index = 0; tag_index < content["tag"].length; tag_index++) {
        $("<a>").text(content["tag"][tag_index]).appendTo(tags)
    }
    block.children(".block-description").children(".view").text(content["viewNumber"])
    block.children(".block-description").children(".comment-number").text(content["commentNumber"])
    block.children(".block-summury").html(content["content"])
    $('.block-description').imagesLoaded(function () {
        container.append(block).masonry('appended', block).masonry()
    });
}

function isMobile() {
    var u = navigator.userAgent.toLowerCase()
    return u.match(/Mobile/i) == 'mobile'
}

function create_new_block(number) {
    var container = document.getElementById('mid-content')
    var new_block = document.createElement('div')
    for (var i = 0; i < number; i++) {
        new_block.className = 'block'
        container.appendChild(new_block)
    }
}

function set_float_pos() {
    var float_x = document.getElementById('nav-bar').getBoundingClientRect().right
    $('#float-window').css('left', float_x - 315)
    if (document.getElementById('float-window').getBoundingClientRect().top <= 100) {
        $('#float-window').attr('class', 'info-window-fixed')
    }
    if (document.getElementById('mid-content').getBoundingClientRect().top >= 100) {
        $('#float-window').attr('class', 'info-window')
    }
}
function getChildElement(cparent, content) { // 得到子集空间
    var contentArr = [];
    var allcontent = cparent.getElementsByTagName('*'); // 获取到所有的元素
    for (var i = 0; i < allcontent.length; i++) {
        if (allcontent[i].className === content) {
            contentArr.push(allcontent[i]);
        }
    }
    return contentArr;
}
