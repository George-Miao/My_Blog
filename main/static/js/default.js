var test_content = {
    day: 4,
    month: "jul",
    title: "测试",
    tag: ["测试", "中文"],
    commentNumber: 0,
    content: "container, day, month, title, tag, comment-number, content",
}

$(function () {
    var $block = $(".block").clone()
    $(".block").remove()

    if (isMobile()) {
        alert('你正在使用移动客户端，可能会有页面显示bug')
        $('#top').css('height', '960px')
        $('.top-cover').css({ 'top': '700px', 'bottom': 'auto' })
    }

    set_float_pos()
    
    var $container = $('#mid-content').masonry({
        itemSelector: '.block',
        gutter: 15,
        stagger: 30,
        animate: false
    })
    $container.masonry('layout')
    add_block($container, $block, test_content)
    add_block($container, $block, test_content)
    add_block($container, $block, test_content)
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

function add_block(container, outter_block, con) {
    var block = outter_block.clone()
    block.children(".block-date").children(".day").text(con["day"])
    block.children(".block-date").children(".month").text(con["month"])
    block.children(".block-title").text(con["title"])
    var tags = block.children(".block-description").children(".tag")
    for(var tag_index = 0; tag_index < con["tag"].length; tag_index++){
        $("<a>").text(con["tag"][tag_index]).appendTo(tags)
    }
    block.children(".block-description").children(".comment-number").text(con["commentNumber"])
    block.children(".block-summury").text(con["content"])
    container.append(block)
    .masonry('appended', block);
    container.masonry('layout');
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
