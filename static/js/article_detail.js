$('.digg-down').on('click',function () {

            if ($('#t1').attr('user-username')) {
            var $now =$(this);
            is_up = $now.hasClass('diggit');
            // article_id = '{{ article_obj.pk }}'
            article_id = $('#t1').attr('article_id')
            $.ajax({
                url:'/blog/up_down/',
                type:'POST',
                data:{is_up:is_up,article_id:article_id},
                success:function (data) {
                    console.log(data)
                    if (data.status){
                        if (data.fisrt_action) {
                            $('#digg_tips').text('你已经推荐过了')
                        }
                        else {
                            $('#digg_tips').text('你已经踩过了')
                        }
                       setTimeout(function () {
                           $('#digg_tips').text('')
                       },1000)
                    }
                    else {
                        var val = $now.children().first().text()
                        $now.children().first().text(parseInt(val)+1)
                    }
                }

            })
            }else {
                location.href='/login/'
            }


        })