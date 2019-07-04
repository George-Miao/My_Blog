window.onload = function () {
    if (true) {
        console.log("load completed")
        $("#content").css("opacity", 1)
        $("#content").css("z-index", "101")
        $(".cover").css("opacity", 0)
    }

    if (isMobile()){
        alert("你正在使用移动客户端，可能会有页面显示bug")
        $('#top').css("height", "960px")
        $('.top-cover').css({"top": "700px", "bottom": "auto"})
    }

    set_float_pos()
    var $container = $('#mid-content').masonry({
        itemSelector: '.block',
    })
    $container.masonry('layout');}

window.onresize = function () {
    set_float_pos()
}

window.addEventListener('scroll', function () {
    set_float_pos()
})

function isMobile(){
    var u = navigator.userAgent.toLowerCase()
    return u.match(/Mobile/i) == "mobile"
}


function create_new_block(number) {
    var container = document.getElementById('mid-content')
    var new_block = document.createElement("div")
    for (var i = 0; i < number; i++) {
        new_block.className = "block"
        container.appendChild(new_block)
    }
}

function set_float_pos() {
    var float_x = document.getElementById('nav-bar').getBoundingClientRect().right
    $("#float-window").css("left", float_x - 315)
    if (document.getElementById('float-window').getBoundingClientRect().top <= 100) {
        $("#float-window").attr("class", "info-window-fixed")
    }
    if (document.getElementById('mid-content').getBoundingClientRect().top >= 100) {
        $("#float-window").attr("class", "info-window")
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

/*
function checkFlag() {
    var cparent = document.getElementById('mid-content');
    var ccontent = getChildElement(cparent, "block");

    var lastContentHeight = ccontent[ccontent.length - 1].offsetTop;
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    var pageHeight = document.documentElement.clientHeight || document.body.scrollHeight;
    if (lastContentHeight < scrollTop + pageHeight) {
        return true;
    }
}
*/