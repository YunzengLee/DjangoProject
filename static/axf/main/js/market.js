$(function(){
    $("#all_types").click(function () {
            console.log("已经点击");
            var $all_types_container = $('#all_types_container');
            $all_types_container.show();
            // 将图标变向上的
            var $all_type = $(this);
            var $span = $all_type.find('span').find('span');
            $span.removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up');

            // 点击这个全部分类时，要把综合排序收回去
            var $sort_rule_container = $("#sort_rule_container");
            $sort_rule_container.slideUp();
            var $sort_rule = $('#sort_rule');
            var $span_sort_rule = $sort_rule.find('span').find('span');
            $span_sort_rule.removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down');

        })
    $("#all_types_container").click(function () {
        var $all_type_container  = $(this);
        // 点击空白出之后把展示出来的选项藏起来
        $all_type_container.hide();
        // 把图标变回去
        var $all_type = $('#all_types');
        var $span = $all_type.find('span').find('span');
        $span.removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down');

    })
    $("#sort_rule").click(function () {
        console.log("排序规则");
        var $sort_rule_container = $("#sort_rule_container");
        $sort_rule_container.slideDown();
        var $sort_rule = $(this);
        var $span = $sort_rule.find('span').find('span');
        $span.removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up');

        var $all_type_container  = $('#all_types_container');
        // 点击空白出之后把展示出来的选项藏起来
        $all_type_container.hide();
        // 把图标变回去
        var $all_type = $('#all_types');
        var $span_all_type = $all_type.find('span').find('span');
        $span_all_type.removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down');


    })

    $("#sort_rule_container").click(function () {
        // 收回
        var $sort_rule_container  = $(this);
        // 点击空白出之后把展示出来的选项藏起来
        $sort_rule_container.slideUp();
        // 把图标变回去
        var $sort_rule = $('#sort_rule');
        var $span = $sort_rule.find('span').find('span');
        $span.removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down');


    })

    // 加减按钮的点击事件：往购物车里加减商品
    $('.subShopping').click(function () {
        console.log('sub');

    })
    $('.addShopping').click(function () {
        console.log('add');
        // 将商品id传给服务器，js怎么拿到商品id呢
        var $add = $(this);
        //获得goodsid
        var goodsid = $add.attr('goodsid');
        // var goodid = $add.prop('goodsid');这个语句只能获取内置属性

        //通过ajax发送给服务器
        // 通过get方法 post需要防csrf
        //以下函数有三个参数， 第一个是请求的url，第二个是传递的参数，data是服务器返回的字典数据
        //接下来要去urls.py中写路由了：/axf/addtocart/
        $.get('/axf/addtocart/',{'goodsid':goodsid},function (data) {
            console.log(data);
            // 如果返回的json数据包里面的状态码是302就进行重定向
            if (data['status'] === 302){
                window.open('axf/login/',target='_self');
            }else if(data['status']===200){
                // 如果商品在后台成功添加进购物车，那么应该显示在前端页面上，
                // 也就是加减按钮之前那个数字加1
                //关键是怎么找到那个数字并更改，由于那个数字是for循环生成的因此不能加id或class
                $add.prev('span').html(data['c_goods_num']); //找当前按钮的前一个标签，用.prev方法
            }
        })



    })
})