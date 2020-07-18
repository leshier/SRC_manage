from django.db import models

# Create your models here.
class SRC_platform(models.Model):
    '''
        SRC 平台名称
    '''
    src_platform_name = models.CharField(max_length=254,verbose_name='SRC平台名称',unique=True)
    src_platform_url = models.URLField(verbose_name="SRC平台链接",unique=True)
    src_platform_avatar = models.ImageField(verbose_name="SRC平台logo",blank=True,default='')

    c_time = models.DateTimeField(auto_now_add=True, verbose_name='增加日期')
    m_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    def __str__(self):
        return self.src_platform_name
    class Meta:
        verbose_name = "SRC平台表"
        verbose_name_plural = "SRC平台表"
        ordering = ['-m_time']

class Company(models.Model):
    ''':arg
        厂商资产页
    '''
    src_platform = models.ForeignKey('SRC_platform',on_delete=models.CASCADE,verbose_name="与SRC平台连结")
    company_name = models.CharField(max_length=255,unique=True,verbose_name="厂商名称")

    c_time = models.DateTimeField(auto_now_add=True, verbose_name='增加日期')
    m_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')
    scan_time = models.DateTimeField(auto_now_add=True,verbose_name='上次扫描日期')

    def __str__(self):
        return self.company_name
    class Meta:
        verbose_name = "厂商表"
        verbose_name_plural = "厂商表"
        ordering = ['-m_time']

class Company_domain(models.Model):
    company = models.ForeignKey('Company',on_delete=models.CASCADE,verbose_name='与厂商对应')
    company_domain_domains = models.CharField(max_length=254,verbose_name='厂商的域名资产')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='增加日期')
    m_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')
    def __str__(self):
        return self.company_domain_domains
    class Meta:
        verbose_name = "厂商域名资产总表"
        verbose_name_plural = "厂商域名资产总表"
        ordering = ['-m_time']

class Company_ips(models.Model):
    company = models.ForeignKey('Company',on_delete=models.CASCADE,verbose_name='与厂商对应')
    company_ips_ips = models.CharField(max_length=254,verbose_name='厂商IP资产总表')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='增加日期')
    m_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    def __str__(self):
        return self.company_ips_ips
    class Meta:
        verbose_name = "厂商IP资产总表"
        verbose_name_plural = "厂商IP资产总表"
        ordering = ['-m_time']

class Target_sudomain(models.Model):
    '''
        厂商资产的子域名部分
    '''
    company_domain = models.ForeignKey('Company_domain', on_delete=models.CASCADE, verbose_name="与对应的厂商主域名对应")
    target_subdomain_subdomain = models.URLField(verbose_name="子域名", unique=True,null=False)
    target_subdomain_ip = models.GenericIPAddressField(verbose_name="IP")
    target_subdomain_localtion = models.CharField(max_length=254, default='', verbose_name="归属地")
    target_subdomain_port = models.CharField(max_length=32, verbose_name="端口")
    target_subdomain_service = models.CharField(max_length=256, blank=True,default='', verbose_name="服务")
    target_subdomain_title = models.CharField(max_length=500, blank=True,default='', verbose_name="标题")
    target_subdomain_statuscode = models.IntegerField(default=200, blank=True,verbose_name="状态码")
    target_subdomain_length = models.IntegerField(default=0,verbose_name='响应包大小')
    target_subdomain_middleware = models.CharField(max_length=500,blank=True,default='', verbose_name="中间件")

    c_time = models.DateTimeField(auto_now_add=True, verbose_name='增加日期')
    m_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')
    def __str__(self):
        return self.target_subdomain_subdomain
    class Meta:
        verbose_name = "厂商子域名资产详细表"
        verbose_name_plural = "厂商子域名资产详细表"
        ordering = ['-m_time']

class Target_ip(models.Model):

    '''
        IP资产详情表，当某一资产没有对应的域名时，入库，当某一IP有对应的一个或多个域名对应时，则重复，不入库
    '''

    company_ips = models.ForeignKey('Company_ips',on_delete=models.CASCADE,verbose_name="与对应的厂商IP资产对应")
    target_ip_ip = models.GenericIPAddressField(verbose_name="IP")
    target_ip_localtion = models.CharField(max_length=254, default='', verbose_name="归属地")
    target_ip_port = models.CharField(max_length=32,verbose_name="端口")
    target_ip_service = models.CharField(max_length=256,default='',blank=True,verbose_name="服务")
    target_ip_title = models.CharField(max_length=500,default='',blank=True,verbose_name="标题")
    target_ip_statuscode = models.IntegerField(default=200, verbose_name="状态码")
    target_ip_length = models.IntegerField(default=0,verbose_name="响应包大小")
    target_ip_middleware = models.CharField(max_length=500,blank=True,default='',verbose_name="中间件")
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='增加日期')
    m_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    def __str__(self):
        return self.target_ip_ip+':'+self.target_ip_port
    class Meta:
        verbose_name = "厂商IP资产详细表"
        verbose_name_plural = "厂商IP资产详细表"
        ordering = ['-m_time']

class Bug_info(models.Model):
    submit = (
        ('0','未提交'),
        ('1','已提交'),
    )
    target_subdomain = models.ForeignKey('Target_sudomain',on_delete=models.CASCADE,verbose_name="与对应的子域名连结",default='',blank=True,null=True)
    target_ip = models.ForeignKey('Target_ip',on_delete=models.CASCADE,verbose_name="与对应的IP链接",default='',blank=True,null=True)

    bug_info_url = models.CharField(max_length=500,verbose_name="漏洞URL")
    bug_info_type = models.CharField(max_length=255,verbose_name="漏洞类型")
    bug_info_text = models.TextField(max_length=65535,blank=True,default='',verbose_name="漏洞详细")
    bug_info_submit = models.CharField(max_length=32,choices=submit,default='0',verbose_name="漏洞是否提交")
    bug_info_money = models.FloatField(max_length=32,default=0,blank=True,verbose_name="漏洞奖金")

    c_time = models.DateTimeField(auto_now_add=True, verbose_name='增加日期')
    m_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    def __str__(self):
        return self.bug_info_url
    class Meta:
        verbose_name = "漏洞详细表"
        verbose_name_plural = "漏洞详细表"
        ordering = ['-m_time']



