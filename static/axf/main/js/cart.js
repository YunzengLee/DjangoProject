$(function () {
    // 商品选中按钮的响应，就是购物车商品前的小圆圈
    $('.confirm').click(function () {
        console.log('change state');
        // 找到cartid 获取对应购物车商品的id
        var $confirm=$(this);
        var $li= $confirm.parents('li');
        var cartid = $li.attr('cartid');

        // 向服务器发起url请求，改变数据库中cart表中对应cart的选中状态
        $.getJSON('/axf/changecartstate/',{'cartid':cartid},function (data) {
            // 由于这个请求的url也是需要验证是否登录的，所以将该路径加入中间件

            // 后端视图函数返回json的data后说明数据库的数据已经修改了
            //接下来要改变显示在页面上的选中状态
            console.log(data);
            if (data['status']===200){
                // # json状态码为200就说明后端视图函数已经完成了数据库数据修改
                //接下来调整该商品页面上的显示
                if (data['c_is_select']){
                    $confirm.find('span').find('span').html('√');
                }else{
                    $confirm.find('span').find('span').html('');
                }

                //判断全选按钮应该是什么状态
                if (data['is_all_select']){
                    $('.all_select span span').html('√');
                }else{
                    $('.all_select span span').html('');
                }

                //改变商品总价的显示，
                $('#total_price').html(data['total_price']);
            }


        })
    })

    // 购物车商品的减按钮的响应
    $('.subShopping').click(function () {
        var $sub = $(this);
        // 获取cartid
        var $li = $sub.parents('li');
        var cartid = $li.attr('cartid');
        // 将cartid传给服务器让它做数量减一操作
        $.getJSON('/axf/subshopping/',{'cartid':cartid},function (data) {
            console.log(data);
            // 返回的data里面有商品当前的数量信息，应当显示在页面上，如果为0，就直接删除
            if (data['status']===200){
                $('#total_price').html(data['total_price']);
                if (data['c_goods_num']>0){
                    var $span = $sub.next('span');
                    $span.html(data['c_goods_num']);
                }else{
                    // 如果返回的data中cart的c_goods_num为0，说明数据库已经删除了这条数据，
                    // 就可以把这条cart对应的li干掉了
                    $li.remove();
                }
            }

        })
    })

    //购物车商品全选按钮的响应
    $('.all_select').click(function () {
        //两种结果：将未选中的商品变选中；当全部商品处于选中状态时，将所有商品变未选中
        var $all_select = $(this);
        var select_list=[];
        var unselect_list=[];
        //将选中与未选中商品分到两个列表里
        $('.confirm').each(function () {
            //each代表遍历
            //如何判断？看span里有没有√号
            var $confirm = $(this);
            var cartid = $confirm.parents('li').attr('cartid');//获取cartid
            if ($confirm.find('span').find('span').html().trim()){
                //判断有没有内容
                //.html是获取内容 .trim是去掉换行符什么的
                select_list.push(cartid);
            }else{
                unselect_list.push(cartid);
            }
        })
        // console.log(select_list);
        // console.log(unselect_list);
        if(unselect_list.length>0){//如果有商品未选中，就将这些商品传给服务器让其处于选中
            $.getJSON('/axf/allselect/',{'cart_list':unselect_list.join('#')},function (data) {
                //注意：无法传递列表，（后端会读取出none）所以将unselect_list转成了字符串
                console.log(data);
                if(data['status']===200){
                    //将所有商品在界面上打钩表示选中，同时全选按钮也显示选中
                    $('.confirm').find('span').find('span').html('√');
                    $all_select.find('span').find('span').html('√');

                    $('#total_price').html(data['total_price']);
                }
            })
            }else {
                if(select_list.length>0){
                        $.getJSON('/axf/allselect/',{'cart_list':select_list.join('#')},function (data) {
                        // 与上面同理，将所有商品状态反转，此时向后端传递的是select_list
                        if(data['status']===200){
                            //将所有商品在界面上去掉打钩表示未选中，同时全选按钮也显示未选中
                            //收到后端返回的json data后将页面上的表示选中的对号去掉
                            $('.confirm').find('span').find('span').html('');
                            $all_select.find('span').find('span').html('');

                            $('#total_price').html(data['total_price']);
                        }
                })
                }
        }

    })

    $('#make_order').click(function () {
        //点击下单 将选中的商品发给服务器
        var select_list=[];
        var unselect_list=[];
        //将选中与未选中商品分到两个列表里
        $('.confirm').each(function () {
            //each代表遍历
            //如何判断？看span里有没有√号
            var $confirm = $(this);
            var cartid = $confirm.parents('li').attr('cartid');//获取cartid
            if ($confirm.find('span').find('span').html().trim()) {
                //判断有没有内容
                //.html是获取内容 .trim是去掉换行符什么的
                select_list.push(cartid);
            } else {
                unselect_list.push(cartid);
            }
        })

        if (select_list.length===0){
            return;
        }else{
            // console.log('下单');
            $.getJSON('/axf/makeorder/',function (data) {
                console.log(data);
                // 此时订单信息已经保存到数据库，应该跳转到订单页了
                if(data['status']===200){
                    window.open('/axf/orderdetail/?orderid='+data['order_id'],target='_self')
                    // # 此时去url配置路由  axf/orderdetail/
                }

            })
        }


    })
})