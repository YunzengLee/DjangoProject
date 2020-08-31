from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from App.models import AXFuser
# 为什么将请求的url分成两组呢，一组返回json响应，这种请求是ajax发起的，不能直接返回重定向，应返回json信息，让前端ajax根据json信息进一步处理
# 另一种请求是浏览器发起的，可以直接重定向

REQUIRE_LOGIN_JSON=[
    '/axf/addtocart/',# 添加商品到购物车  ajax发起的请求
    '/axf/changecartstate/',# 改变购物车商品的选中状态，也是ajax发起的请求
    '/axf/makeorder/',#下单
]

REQUIRE_LOGIN=[
    '/axf/cart/',
    '/axf/orderdetail/',
    '/axf/orderlistnotpay/',
]


class LoginMiddleware(MiddlewareMixin):
    def process_request(self,request):
        # process_request 是中间件（本质上是一个python类）的一个方法，名称不可变更否则失效，
        # 这个方法会在在执行视图之前被调用，（对url匹配视图函数之前），
        # 每个请求到来时都会调用，返回None或者HttpResponse对象。
        # 作用之一：匹配前就返回响应，可以反爬虫
        # 这个方法的作用是：在点击了添加商品进购物车的按钮后，前端js发起了url请求，
        # 在这个请求被服务器处理前，判断用户是否登录。
        if request.path in REQUIRE_LOGIN_JSON:  # request.path代表请求的url
            user_id = request.session.get('user_id')# 从请求对应的session里面取出userid
            print('正在执行中间件')
            if user_id:# 如果session里存放了userid，说明用户已登录
                try:
                    user = AXFuser.objects.get(pk=user_id)
                    request.user = user  # 此处是给request添加了一个属性，进行标记
                                        # 这样之后的操作就可以直接从requets.user中获取当前用户，不用再查session
                except:# 如果出异常，去登录页面

                    # return redirect(reverse('axf:login'))
                    data = {
                        'status':302,
                        'msg':'user not available',# 用户id找到了但是用户没找到说明用户状态失效
                    }
                    return JsonResponse(data=data)
            else:  # 如果用户未登录，就返回登录界面
                data={
                    'status':302,
                    'msg':'user not login'
                }
                return JsonResponse(data=data)
                # 可以在这里补充一句request.session【‘error_message’】=‘错误信息’
                # 登录页面的get方法的视图函数可以读取这个错误信息，并做相应处理
                # return redirect(reverse('axf:login')) # 返回给这个前端是没有反应的，原因在下面：

            # 不应该return 重定向，因为这个请求是ajax发起的，不是浏览器发起的，ajax不知道什么是重定向
            # 应该返回一个JsonResponse，让ajax解析json中的信息，若读取到信息中含有重定向的指示，就在前端进行重定向

        if request.path in REQUIRE_LOGIN:
            # 进入购物车页面时看用户是否登录 逻辑与上面一样，这个不用返回json，
            # 是因为发起这个url请求的不是写在js文件里的ajax
            user_id = request.session.get('user_id')
            print('正在执行中间件')
            if user_id:  # 如果用户存在
                try:
                    user = AXFuser.objects.get(pk=user_id)
                    request.user = user  # 此处是给request添加了一个属性，进行标记
                except:  # 如果出异常，去登录页面

                    return redirect(reverse('axf:login'))

            else:  # 如果用户未登录，就返回登录界面
                return redirect(reverse('axf:login'))