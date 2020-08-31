from django.db import models

# Create your models here.
from App.views_constant import ORDER_STATUS_NOT_PAY


class Main(models.Model):
    img = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField(default=1)  # 在原表中的id
    class Meta:
        abstract =True

class MainWheel(Main):
    '''
    轮播
    axf_wheel  img,name,trackid
    '''

    class Meta:
        db_table = 'axf_wheel'
class MainNav(Main):
    """
    轮播下面的导航栏
    """
    class Meta:
        db_table = 'axf_nav'
class MainMustBuy(Main):
    """
    必买
    """
    class Meta:
        db_table = 'axf_mustbuy'
class MainShop(Main):
    class Meta:
        db_table = 'axf_shop'
class MainShow(Main):
    categoryid = models.IntegerField()
    brandname = models.CharField(max_length=64)
    img1 = models.CharField(max_length=255)
    childcid1 = models.IntegerField(default=1)
    productid1 = models.IntegerField(default=1)
    longname1 = models.CharField(max_length=128)
    price1 = models.FloatField(default=1)
    marketprice1 = models.FloatField(default=0)

    img2 = models.CharField(max_length=255)
    childcid2 = models.IntegerField(default=1)
    productid2 = models.IntegerField(default=1)
    longname2 = models.CharField(max_length=128)
    price2 = models.FloatField(default=1)
    marketprice2 = models.FloatField(default=0)

    img3 = models.CharField(max_length=255)
    childcid3 = models.IntegerField(default=1)
    productid3 = models.IntegerField(default=1)
    longname3 = models.CharField(max_length=128)
    price3 = models.FloatField(default=1)
    marketprice3 = models.FloatField(default=0)

    class Meta:
        db_table='axf_mainshow'
class FoodType(models.Model):
    typeid = models.IntegerField(default=1)
    typename = models.CharField(max_length=32)
    childtypenames = models.CharField(max_length=255)
    typesort = models.IntegerField(default=1)
    class Meta:
        db_table = 'axf_foodtype'

class Goods(models.Model):
    productid=models.IntegerField(default=1)
    productimg= models.CharField(max_length=255)
    productname = models.CharField(max_length=128)
    productlongname=models.CharField(max_length=255)
    isxf = models.BooleanField(default=False)# 是否先锋推荐
    pmdesc = models.BooleanField(default=False)
    specifics = models.CharField(max_length=64)
    price = models.FloatField(default=0)
    marketprice = models.FloatField(default=1)
    categoryid = models.IntegerField(default=1)
    childcid = models.IntegerField(default=1)
    childcidname = models.CharField(max_length=128)
    dealerid = models.IntegerField(default=1)
    storenums = models.IntegerField(default=1)
    productnum=models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_goods'

# 用户类
class AXFuser(models.Model):
    # 在保存的用户的数据表中，用户名和邮件都不可重复，也就是不能用相同的用户名和邮箱注册该网站
    u_username = models.CharField(max_length=32, unique=True)
    u_password = models.CharField(max_length=256)
    u_emial = models.CharField(max_length=64, unique=True)
    # static文件夹下创建uploads文件夹，参数uploads_to就代表上传文件在uploads文件夹下的存放位置
    u_icon = models.ImageField(upload_to='icons/%Y/%m/%d/')
    is_active =models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    class Meta:
        db_table = 'axf_user'#定义数据库中的表名


# 购物车模型类
class Cart(models.Model):
    c_user = models.ForeignKey(AXFuser,on_delete=models.CASCADE)
    c_goods = models.ForeignKey(Goods,on_delete=models.CASCADE)
    c_goods_num= models.IntegerField(default=1)
    c_is_select=models.BooleanField(default=True)
    class Meta:
        db_table='axf_cart'

# 订单模型类
class Order(models.Model):
    o_user = models.ForeignKey(AXFuser,on_delete=models.CASCADE)
    o_price = models.FloatField(default=0)
    o_time=models.DateTimeField(auto_now=True)
    o_status = models.IntegerField(default=ORDER_STATUS_NOT_PAY)

    class Meta:
        db_table='axf_order'

# 订单中的各个商品
class OrderGoods(models.Model):
    o_order = models.ForeignKey(Order,on_delete=models.CASCADE)
    o_goods = models.ForeignKey(Goods,on_delete=models.CASCADE)
    o_goods_num = models.IntegerField(default=1)
    class Meta:
        db_table='axf_ordergoods'
