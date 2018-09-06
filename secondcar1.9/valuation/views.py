from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm
from .models import Users
from .models import *
from django.db import connection
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# 主网页
def index_views(request):
    return render(request, 'psm.html')

# 二手车市场统计分析的echarts表格页面
def page2_views(request):
    return render(request, 'page2.html')

# 关于我们页面
def about_views(request):
    return render(request, 'about.html')

# 各省市二手车分布map
def citycarnum(request):
    return render(request,'psm.html')

'''
处理估值窗口里的ajax_province请求,
返回给请求页面id,省二元数组
'''
@csrf_exempt
def ajax_province(request):
    if request.method == 'POST':
        with connection.cursor() as c:
            c.execute("select id,name from district_info where p_id=0")
            provinces = c.fetchall()      # 是二元元组((11, '北京'), (12, '天津'), (13, '河北'), (14, '山西'),...
        return JsonResponse(provinces,safe=False)

'''
处理估值窗口里的ajax_city请求,传入省id
返回给请求页面id,市二元数组
'''
@csrf_exempt
def ajax_city(request):
    if request.method == 'POST':
        rec = json.loads(request.body.decode())
        p_id = int(rec['p_id'])
        with connection.cursor() as c:
            c.execute("select id,name from district_info where p_id=%d" %p_id)
            citys = c.fetchall()
        return JsonResponse(citys,safe=False)

''' 
所有品牌查询,处理估值窗口里ajax_brand请求
    给返回首字母+车品牌
'''
@csrf_exempt
def ajax_brand(request):
    if request.method == 'POST':
        with connection.cursor() as c:
            c.execute("select * from car_brand")
            brands = c.fetchall()
        return JsonResponse(brands,safe=False)

'''
某品牌下车系查询,处理估值窗口里ajax_style请求,需要传入品牌id
返回该品牌下的所有车系
'''
@csrf_exempt
def ajax_style(request):
    if request.method == 'POST':
        rec = json.loads(request.body.decode())
        p_id = int(rec['id'])
        with connection.cursor() as c:
            c.execute("select id,name from carmodel_info where p_id=%d" %p_id)
            styles = c.fetchall()
        return JsonResponse(styles,safe=False)

'''
某品牌下车系查询,处理估值窗口里ajax_model请求,需要传入车系id
返回该品牌下的所有车型
'''
@csrf_exempt
def ajax_model(request):
    if request.method == 'POST':
        rec = json.loads(request.body.decode())
        p_id = int(rec['id'])
        with connection.cursor() as c:
            c.execute("select id,name from carmodel_info where p_id=%d" %p_id)
            models = c.fetchall()
        return JsonResponse(models,safe=False)

'''
某车型的起售年份查询,处理估值窗口下ajax_time请求,需要传入车型id
返回该车型的可选年份
'''
@csrf_exempt
def ajax_year(request):
    if request.method == 'POST':
        rec = json.loads(request.body.decode())
        p_id = int(rec['id'])
        with connection.cursor() as c:
            c.execute("select name from carmodel_info where id=%d" %p_id)
            models = c.fetchall()
            model = models[0][0]
            saleyear = int(model[:4])-1
            saleyears = [n for n in range(saleyear,2019)]

            return JsonResponse(saleyears,safe=False)

'''
某车型的起售月份查询,处理估值窗口下ajax_time请求,需要传入上牌年份
返回可选月份列表
'''
@csrf_exempt
def ajax_month(request):
    if request.method == 'POST':
        rec = json.loads(request.body.decode())
        year = int(rec['year'])
        if year == 2018:
            salemonth = ["1月","2月","3月","4月","5月","6月","7月"]
        else:
            salemonth = ["1月","2月","3月","4月","5月","6月","7月","8月",\
                        "9月","10月","11月","12月"]

        return JsonResponse(salemonth,safe=False)

'''
 汽车估值,传入上牌省，市，车型，车型id，上牌时间月份，行驶里程
 返回估值，同款车本城市平均卖价，同款车全国平均卖价
 '''
@csrf_exempt
def valuation(request):
    if request.method == 'POST':
        rec = json.loads(request.body.decode())
        proid = int(rec['proid'])
        cityid = int(rec['cityid'])
        with connection.cursor() as c:
            c.execute("select name from district_info where id=%d" %cityid)
            citys = c.fetchall()
            city = citys[0][0]
        modelid = int(rec['modelid'])
        brand = rec['brandname']
        style = rec['stylename']
        model = rec['modelname']
        year = int(rec['year'])
        month = int(rec['month'].replace("月",''))
        mileage = float(rec['mileage'])
        with connection.cursor() as c:
            c.execute("select price from carmodel_info where id=%d" %modelid)
            ps = c.fetchall()
            newprice = float(str(ps[0][0]))# 不含税

        x = (2018-year)*12+(7-month)
        y = mileage
        z = newprice
        vprice = -0.50846588-0.01019893*x+0.21104641*y+0.82346503*\
        z-0.00251885*x*y-0.00545057*x*z-0.01658697*y*z+0.00021015*x*x+\
        0.00636647*y*y+0.00012589*z*z+0.00012544*x*y*z
        vprice=round(vprice,2)

        dict={}
        dict['newprice']=newprice
        dict['vprice']=vprice
        with connection.cursor() as c:
            sql1 = "select avg(sec_price) from sec_carinfo where car_model like '%s' "% ('%%%s%%%s%%%s%%' % (brand,style,model))
            c.execute(sql1)
            avgp = c.fetchall()
            avgprice = round(avgp[0][0],2)
        dict['avgprice']=avgprice

        return JsonResponse(dict,safe=False)

'''
处理谁更保值ajax_value请求,返回保值最高的
前二十个车品牌及万公里价格折损率(该值越低保值性越好)
'''
@csrf_exempt
def ajax_value(request):
    if request.method == 'POST':
        with connection.cursor() as c:
            c.execute("select id,name,cvalue from carvalue where num>100 order by cvalue limit 20")
            cvalues = c.fetchall()
        return JsonResponse(cvalues,safe=False)

'''
处理供给最大ajax_carcount请求,返回车数量最多的
前二十个车品牌及车数量
'''
@csrf_exempt
def ajax_carcount(request):
    if request.method == 'POST':
        with connection.cursor() as c:
            c.execute("select id,name,num from carvalue where num>100 order by num desc limit 20")
            ccounts = c.fetchall()
        return JsonResponse(ccounts,safe=False)

'''
处理价位偏好ajax_pricenum请求,返回每个价位的车数量、占比及平均价格
'''
@csrf_exempt
def ajax_pricenum(request):
    if request.method == 'POST':
        with connection.cursor() as c:
            c.execute("select * from pricenum")
            pricenums = c.fetchall()
        return JsonResponse(pricenums,safe=False)

'''
处理多久卖车ajax_sellage请求,返回每个车龄段的车辆数量、占比、平均车龄
'''
@csrf_exempt
def ajax_sellage(request):
    if request.method == 'POST':
        with connection.cursor() as c:
            c.execute("select * from pricenum")
            agenums = c.fetchall()
        return JsonResponse(agenums,safe=False)

# 处理登录请求
def login_views(request):
    if request.method == 'POST':
        # 处理post请求
        # 　实现登录操作
        uphone = request.POST['uphone']
        upwd = request.POST['upwd']
        uList = Users.objects.filter(uphone=uphone, upwd=upwd)
        # 判断登录成功　or　失败
        if uList:
            # 登录成功
            resp = HttpResponse('登录成功，去往首页')
            expires = 60 * 60 * 24 * 365
            # 将登录信息保存进　session
            request.session['uphone'] = uphone
            request.session['id'] = uList[0].id
            # 是否记住密码
            if 'isSaved' in request.POST:
                resp.set_cookie('id', uList[0].id, expires)
                resp.set_cookie('uphone', uphone, expires)
            return resp
        else:
            # 　登录失败
            # 继续展示登录页面
            form = LoginForm()
            return render(request, 'login.html', locals())
    else:
        # 处理get请求
        # 判断　session 中是否有　id 和　uphone
        if 'id' in request.session and 'uphone' in request.session:
            # session 中有登录信息，直接去首页
            return HttpResponse('去往首页')
        else:
            # session 中没有登录信息
            # 查看cookie中有没有登录信息
            if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
                # 曾经登录过，而且保存了信息在cookies，取出数据保存进session
                uid = request.COOKIES['id']
                uphone = request.COOKIES['uphone']
                request.session['id'] = uid
                request.session['uphone'] = uphone
                return HttpResponse('去往首页')
            else:
                # cookie中没有登录信息
                form = LoginForm()
                return render(request, 'login.html', locals())

# 处理注册请求
def register_views(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        uphone = request.POST['uphone']
        upwd = request.POST['upwd']
        uname = request.POST['uname']
        uemail = request.POST['uemail']
        # 验证手机号是否存在
        uList = Users.objects.filter(uphone=uphone)
        if uList:
            # 为真，手机号已存在，给出错误提示
            return render(request,
                          'register.html',
                          {'errMsg': '手机号已存在!',
                           'uname': uname,
                           'uemail': uemail,
                           })
        dic = {
            'uphone': uphone,
            'upwd': upwd,
            'uname': uname,
            'uemail': uemail,
        }
        Users(**dic).save()
        return HttpResponse('注册成功')