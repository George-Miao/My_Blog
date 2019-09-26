$(function () {

    window.onload = function () {
        $('#content').css('opacity', 1)
        $('#content').css('z-index', '101')
        $('.cover').css('opacity', 0)
    }
    var month = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    var list
    $.ajax({
        url: '/api/list',
        async: false,
        success: function(e){
            list = e
        },
        error: function(e){
            alert(e)
        }
    })
    var blocks = []
    for (entry in list){
        var time = new Date(list[entry][1])
        $.ajax({
            url: '/api/content?path=' + list[entry][0],
            async: false,
            success: function(e){
                block = {
                    'day': time.getDate(),
                    'month': month[time.getMonth()],
                    'title': entry.split('.').slice(0, -1).join(),
                    'content': e
                }
                blocks.push(block)
            },
            error: function(e){
                alert(e)
            }
        })
    }



    Vue.component('block-date', {
        props: ['day', 'month'],
        template:"<div class='block-date'><a class='day'>{{day}}</a><a class='month'>{{month}}</a><div class='date-color-bar'></div></div>"
    })

    Vue.component('block-title', {
        props: ['title'],
        template:"<a class='block-title'>{{title}}</a>"
    })

    var block = new Vue({
        el: '#mid-content',
        data: {
            blocks: blocks
        }
    })


})
