#-*- coding:utf-8 -*-
from django.db import models

# 售后登录账号表
class AfterSalesLogin(models.Model):
    asl_name=models.CharField(max_length=10)
    asl_passwd=models.CharField(max_length=20)

    def __unicode__(self):
        return self.asl_name

# 售后单表 
class AfterSales(models.Model):
    SERVICE_TYPE = (('weixiu','维修'),('zhenggai','整改'),('tuihuo','退货'))
    FLAG_TYPE = (('finished','结束'),('unfinished','未完成'))
    as_date=models.DateField()#日期
    as_number=models.CharField(max_length=20)#单号
    as_type=models.CharField(max_length=10,choices=SERVICE_TYPE)#售后类型
    as_flagtype=models.CharField(max_length=10,choices=FLAG_TYPE)#是否完成标识
    as_name=models.CharField(max_length=20)#业务员姓名
    as_client=models.CharField(max_length=60,blank=True,null=True)#客户公司名称
    as_clientname=models.CharField(max_length=40,blank=True,null=True)#客户姓名
    as_clientphone=models.CharField(max_length=40,blank=True,null=True)#客户电话
    as_clientaddress=models.CharField(max_length=100,blank=True,null=True)#客户地址
    as_cranetype=models.CharField(max_length=20,blank=True,null=True)#起重机类型
    as_metertype=models.CharField(max_length=20,blank=True,null=True)#仪表类型
    as_cranemodel=models.CharField(max_length=20,blank=True,null=True)#起重机型号规格
    as_metermodel=models.CharField(max_length=20,blank=True,null=True)#仪表型号
    as_faultdescribe=models.TextField(max_length=200,blank=True,null=True)#故障描述
    as_faultanalyze=models.TextField(max_length=200,blank=True,null=True)#故障分析
    as_faultresult=models.TextField(max_length=200,blank=True,null=True)#处理结果

    def __unicode__(self):
        return self.as_number

# 存储临时表单
class FormTemp(models.Model):
    TYPE_CHOICES = (('kong',' '),('zhenggai','整改'),('weixiu','维修'),('tuihuo','退货'))
    TYPE_FLAG = (('kong',''),('finished','结束'),('unfinished','未完成'))

    searchDateStart = models.DateField(blank=True,null=True)
    searchDateEnd = models.DateField(blank=True,null=True)
    searchNumber = models.CharField(max_length=20,blank=True,null=True)
    searchClient= models.CharField(max_length=60,blank=True,null=True)
    searchClientName = models.CharField(max_length=40,blank=True,null=True)
    searchName = models.CharField(max_length=20,blank=True,null=True)
    searchKeyWord = models.CharField(max_length=40,blank=True,null=True)    
    searchType = models.CharField(max_length=10,choices=TYPE_CHOICES,blank=True,null=True)    
    searchFlag = models.CharField(max_length=10,choices=TYPE_FLAG,blank=True,null=True)    
