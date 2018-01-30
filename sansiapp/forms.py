#-*- coding:utf-8 -*-
#by msw 20170714

from django import forms
from django.forms import ModelForm
from sansiapp.models import AfterSales

TYPE_CHOICES = (('kong',' '),('zhenggai','整改'),('weixiu','维修'),('tuihuo','退货'))
TYPE_FLAG = (('kong',''),('finished','结束'),('unfinished','未完成'))

# 售后录入登录
class formAfterSalesLogin(forms.Form):
    name = forms.CharField(label='账号',max_length=20)
    passwd = forms.CharField(label='密码',max_length=20,widget=forms.PasswordInput())

# 售后申请单模板
class formAfterSalesRequest(ModelForm):
    class Meta:
        model=AfterSales
        fields=['as_date','as_number','as_type','as_flagtype','as_name','as_client','as_clientname','as_clientphone','as_clientaddress','as_cranetype','as_cranemodel','as_metermodel','as_faultdescribe','as_faultanalyze','as_faultresult']

# 查询
class formSearch(forms.Form):
    searchDateStart = forms.DateField(label='开始日期',required=False)
    searchDateEnd = forms.DateField(label='结束日期',required=False)
    searchNumber = forms.CharField(label='生产单号',required=False,max_length=20,widget=forms.TextInput(attrs={'class':'textinput_special'}))
    searchClient= forms.CharField(label='客户名称',required=False,max_length=40,widget=forms.TextInput(attrs={'class':'textinput_special'}))
    searchClientName = forms.CharField(label='联系人',required=False,max_length=20,widget=forms.TextInput(attrs={'class':'textinput_special'}))
    searchName = forms.CharField(label='销售员姓名',required=False,max_length=20,widget=forms.TextInput(attrs={'class':'textinput_special'}))
    searchKeyWord = forms.CharField(label='关键字查询',required=False,max_length=40,widget=forms.TextInput(attrs={'class':'textinput_special'}))    
    searchType = forms.ChoiceField(label='售后类型',required=False,widget=forms.Select(attrs={'class':'select_special'}),choices=TYPE_CHOICES)    
    searchFlag = forms.ChoiceField(label='结束标志',required=False,widget=forms.Select(attrs={'class':'select_special'}),choices=TYPE_FLAG)    

## 售后申请单模板
#class formAfterSaleRequest(forms.Form):
#    service_type = (('weixiu','维修'),('zhenggai','整改'))
#
#    after_sale = forms.ChoiceField(choices=service_type)#售后类型
#
#    number = forms.CharField(label='售后单号',max_length=20,widget=forms.TextInput(attrs={'class':'textinput_special'}))
#    formdate = forms.DateField(label='日期')
#
#    clientname = forms.CharField(label='客户名称',max_length=20,widget=forms.TextInput(attrs={'class':'textinput_special'}))
#    name = forms.CharField(label='联系人',max_length=20,widget=forms.TextInput(attrs={'class':'textinput_special'}))
#
#    clientaddress = forms.CharField(label='客户地址',max_length=20,widget=forms.TextInput(attrs={'class':'textinput_special'}))
#    phone = forms.CharField(label='联系电话',max_length=20,widget=forms.TextInput(attrs={'class':'textinput_special'}))
#
#    cranetype = forms.CharField(label='起重机类型',max_length=20,widget=forms.TextInput(attrs={'class':'textinput_special'}))   #    metertype = forms.CharField(label='仪表类型',max_length=20,widget=forms.TextInput(attrs={'class':'textinput_special'}))
#
#    cranemodel = forms.CharField(label='起重机型号',max_length=20,widget=forms.TextInput(attrs={'class':'textinput_special'}))
#    metermodel = forms.CharField(label='仪表型号',max_length=20,widget=forms.TextInput(attrs={'class':'textinput_special'}))
#
#    faultdescribe = forms.CharField(label='故障描述',widget=forms.Textarea(attrs={'cols':'58'}))
#    faultanalyze = forms.CharField(label='故障分析',widget=forms.Textarea(attrs={'cols':'58'}))
#    faultresult = forms.CharField(label='处理结果',widget=forms.Textarea(attrs={'cols':'58'}))

## 销售需填写的客户信息和故障描述
#class formAfterSaleInfo(forms.Form):
#    service_type = (('weixiu','维修'),('zhenggai','整改'))
#
#    saler = forms.CharField(label='下单人',max_length=10)
#    after_sale = forms.ChoiceField(choices=service_type)
#
#    number = forms.CharField(label='生产单号',max_length=20)
#    formdate = forms.DateField(label='日期')
#
#    clientname = forms.CharField(label='客户名称',max_length=20)
#    name = forms.CharField(label='联系人',max_length=20)
#
#    clientaddress = forms.CharField(label='客户地址',max_length=20)
#    phone = forms.CharField(label='联系电话',max_length=20)
#
#    cranetype = forms.CharField(label='起重机类型',max_length=20)   
#    metertype = forms.CharField(label='仪表类型',max_length=20)
#
#    cranemodel = forms.CharField(label='起重机型号',max_length=20)
#    metermodel = forms.CharField(label='仪表型号',max_length=20)
#
#    faultdescribe = forms.CharField(label='故障描述',widget=forms.Textarea)
#
## 售后相关人员填写，故障分析和处理结果
#class formAfterSaleResult(forms.Form):
#    faultanalyze = forms.CharField(label='故障分析',widget=forms.Textarea)
#    faultresult = forms.CharField(label='处理结果',widget=forms.Textarea)
