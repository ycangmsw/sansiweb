#!/usr/bin/python
#-*- coding:utf-8 -*-
#mingshwiu 20170714
# 2017年11月4日，增加结束标志查询
# git test

import time
import re
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from sansiapp.models import AfterSales,AfterSalesLogin
from .forms import formAfterSalesRequest,formAfterSalesLogin,formSearch,TYPE_CHOICES,TYPE_FLAG

def home(req):
    form = formAfterSalesRequest()
    return render(req,'home.html',{'form':form})

def asdb_login(req):
    if req.method == 'POST':
        form = formAfterSalesLogin(req.POST)
        if form.is_valid():
            objform = form.cleaned_data
            if AfterSalesLogin.objects.filter(asl_name=objform['name']):
                if AfterSalesLogin.objects.filter(asl_passwd=objform['passwd']):
                    form_input = formAfterSalesRequest(initial={'as_date':'格式：2017-01-01','as_faultdescribe':'字数限制100字','as_faultanalyze':'字数限制100字','as_faultresult':'字数限制100字'})
                    return render(req,'home.html',{'form':form_input }) 
                return render(req,'base_login.html',{'form':form,'error_info':'密码错误！'})
            return render(req,'base_login.html',{'form':form,'error_info':'用户名错误！'})
        else:
            return render(req,'base_login.html',{'form':form,'error_info':form.errors})
    else:
        form = formAfterSalesLogin()
    return render(req,'base_login.html',{'form':form})

def asdb_input(req):
    if req.method == 'POST':
        form = formAfterSalesRequest(req.POST)
        if form.is_valid():
#            info = form.save()
#            info.save()
            form.save()
            return render(req,'home.html',{'form':form,'result_info':'数据保存成功!'})
        else:
            return render(req,'home.html',{'form':form,'error_info':form.errors})
    else:
        form = formAfterSalesRequest(initial={'as_date':'例：2017-01-01','as_faultdescribe':'字数限制100字','as_faultanalyze':'字数限制100字','as_faultresult':'字数限制100字'})
    return render(req,'home.html',{'form':form})

def check_bit_flag(objdb):
    if objdb:
        return True   #按条件搜索到结果
    else:
        return False  #按条件没有搜索到结果

def search(req):

    bitFlag=True

    if req.method == 'GET':
        form = formSearch(req.GET)
        if form.is_valid():
            objforms=form.cleaned_data

            # 日期判断、查询
            if objforms['searchDateStart'] is not None:
                if objforms['searchDateEnd'] is not None:
                    OBJDB = AfterSales.objects.filter(as_date__range=(objforms['searchDateStart'],objforms['searchDateEnd']))
                    bitFlag=check_bit_flag(OBJDB)
                else:
                    # 只填入开始日期
                    OBJDB=AfterSales.objects.filter(as_date=objforms['searchDateStart'])
                    bitFlag=check_bit_flag(OBJDB)
            elif objforms['searchDateEnd'] is not None:
                # 只填入结束日期
                OBJDB = AfterSales.objects.filter(as_date=objforms['searchDateEnd'])
                bitFlag=check_bit_flag(OBJDB)
            else:
                OBJDB=[]
             
            # 生产单号查询
            if objforms['searchNumber'] != '':
                # 判断单号是不是纯数字
                if re.match(r'^\d+$',objforms['searchNumber']) is not None:
                    if OBJDB and bitFlag:
                        OBJDB = OBJDB.filter(as_number__contains = objforms['searchNumber'])
                        bitFlag = check_bit_flag(OBJDB)
                    elif (not OBJDB) and bitFlag:
                        OBJDB = AfterSales.objects.filter(as_number__contains = objforms['searchNumber'])
                        bitFlag = check_bit_flag(OBJDB)
                else:
                    if OBJDB and bitFlag:
                        OBJDB = OBJDB.filter(as_number=objforms['searchNumber'])
                        bitFlag = check_bit_flag(OBJDB)
                    elif (not OBJDB) and bitFlag:
                        OBJDB = AfterSales.objects.filter(as_number=objforms['searchNumber'])
                        bitFlag = check_bit_flag(OBJDB)

            # 客户名称查询
            if objforms['searchClient'] != '':
                if OBJDB and bitFlag:
                    OBJDB = OBJDB.filter(as_client__contains=objforms['searchClient'])
                    bitFlag = check_bit_flag(OBJDB)
                elif (not OBJDB) and bitFlag:
                    OBJDB = AfterSales.objects.filter(as_client__contains=objforms['searchClient'])
                    bitFlag = check_bit_flag(OBJDB)

            # 联系人查询
            if objforms['searchClientName'] != '':
                if OBJDB and bitFlag :
                    OBJDB = OBJDB.filter(as_clientname=objforms['searchClientName'])
                    bitFlag = check_bit_flag(OBJDB)
                elif (not OBJDB) and bitFlag:
                    OBJDB = AfterSales.objects.filter(as_clientname=objforms['searchClientName'])
                    bitFlag = check_bit_flag(OBJDB)

            # 销售员查询
            if objforms['searchName'] != '':
                if OBJDB and bitFlag :
                    OBJDB = OBJDB.filter(as_name=objforms['searchName'])
                    bitFlag = check_bit_flag(OBJDB)
                elif (not OBJDB) and bitFlag:
                    OBJDB = AfterSales.objects.filter(as_name=objforms['searchName'])
                    bitFlag = check_bit_flag(OBJDB)

            # 关键字查询
            if objforms['searchKeyWord'] != '':
                if OBJDB and bitFlag :
                    OBJDB = OBJDB.filter(as_faultanalyze__contains=objforms['searchKeyWord'])
                    bitFlag = check_bit_flag(OBJDB)
                elif (not OBJDB) and bitFlag:
                    OBJDB = AfterSales.objects.filter(as_faultanalyze__contains=objforms['searchKeyWord'])
                    bitFlag = check_bit_flag(OBJDB)

            # 售后类型查询
            if objforms['searchType'] != 'kong' and objforms['searchType'] != '':
                if OBJDB and bitFlag:
                    for n in range(len(TYPE_CHOICES)):
                        if objforms['searchType'] in TYPE_CHOICES[n]:
                            temp=TYPE_CHOICES[n][1]
                            break
                    OBJDB = OBJDB.filter(as_type=temp)
                    bitFlag = check_bit_flag(OBJDB)
                elif (not OBJDB) and bitFlag:
                    for n in range(len(TYPE_CHOICES)):
                        if objforms['searchType'] in TYPE_CHOICES[n]:
                            temp=TYPE_CHOICES[n][1]
                            break
                    OBJDB = AfterSales.objects.filter(as_type=temp)
                    bitFlag = check_bit_flag(OBJDB)

            # 结束标志查询
            if objforms['searchFlag'] != 'kong' and objforms['searchType'] != '':
                if OBJDB and bitFlag:
                    for n in range(len(TYPE_FLAG)):
                        if objforms['searchFlag'] in TYPE_FLAG[n]:
                            temp=TYPE_FLAG[n][1]
                            break
                    OBJDB = OBJDB.filter(as_flagtype=temp)
                    bitFlag = check_bit_flag(OBJDB)
                elif (not OBJDB) and bitFlag:
                    for n in range(len(TYPE_FLAG)):
                        if objforms['searchFlag'] in TYPE_FLAG[n]:
                            temp=TYPE_FLAG[n][1]
                            break
                    OBJDB = AfterSales.objects.filter(as_flagtype=temp)
                    bitFlag = check_bit_flag(OBJDB)


            if OBJDB :
                num = len(OBJDB)
            else:
                OBJDB = AfterSales.objects.filter(id=1)
                num = len(OBJDB) - 1

            req.session['FORM'] = form
            req.session['OBJDB'] = OBJDB
            req.session['NUM'] = num
            #print OBJDB
            #print len(OBJDB)
            return render(req,'base_query.html',{'form':form,'objdbs':OBJDB,'num':num,'item_objdb':OBJDB})
        else:
            return render(req,'base_query.html',{'form':form,'error_info':form.errors})

def search_result(req):
    GLOBAL_FORM=req.session['FORM']
    GLOBAL_OBJDB=req.session['OBJDB']
    GLOBAL_NUM=req.session['NUM']
#    print "into search_resutl"
#    print req.get_full_path()
#    print
#    print req.path
    item = GLOBAL_OBJDB.filter(as_number=req.path[1:])
    return render_to_response('base_query.html',{'form':GLOBAL_FORM,'objdbs':GLOBAL_OBJDB,'num':GLOBAL_NUM,'item_objdb':item})
#
#def is_valid_date(str):
#    '''判断所给字符串是否为有效日期格式'''
#    try:
#        time.strptime(str, "%Y-%m-%d")
#        return True
#    except:
#        return False
#
