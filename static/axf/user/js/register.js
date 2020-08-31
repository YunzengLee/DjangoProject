$(function () {
    // 找到username
    var $username = $('#username_input');
    $username.change(function () {
        // 取值并去空格
        var username = $username.val().trim();
        // 如果长度大于0 交给服务器校验
        if (username.length){
            // 传一个json文件，url是axf/checkuser/,需要配置url
            $.getJSON('axf/checkuser/',{'username':username},function (data) {
                 console.log(data);
                 var $username_info = $('#username_info');
                 if (data['status'] === 200){
                     $username_info.html('用户名可用').css('color','green');

                 }else if (data['status']===901){
                     $username_info.html('用户名已存在').css('color','red');
                 }
            })
        }


    })
})
function check() {
    var $username = $('#username_input');
    var username = $username.val().trim();
    // console.log(username);
    if (username === ''){
        // console.log('输入的用户名为空');
        // console.log(username);
        return false
        // 输入的用户名为空就返回false
    }
    var $username_info = $('#username_info');
    var info_color = $username_info.css('color');
    // console.log(info_color);

    // return info_color != 'rgb(255,0,0)';
    if (info_color === 'rgb(255, 0, 0)'){
        console.log('可用啊啊啊啊');
        return false
    }
    // 以下三行是密码在前端post时用md5加密   登录时也用到了这个加密
    var $password_input = $('#password_input');
    var password = $password_input.val().trim();
    $password_input.val(md5(password));

    return true
}