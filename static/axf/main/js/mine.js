$(function () {
    // 在js文件中定义未登录按钮的功能 不在视图函数中定义
    $('#not_login').click(function () {

        window.open('/axf/login/',target="_self");//在当前页面打开，如果去掉target就会跳转到新页面
    })
    //给注册加个点击事件
    $('#regis').click(function () {
        window.open('/axf/register/',target='_self');
    })

    //给未付款加点击事件
    $('#not_pay').click(function () {
        console.log('点击未付款');
        window.open('/axf/orderlistnotpay/',target='_self');
        // 接下来去写这个路径匹配

    })
})