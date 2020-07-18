from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.db.models import Count
from . import models
# Create your views here.
from django.shortcuts import get_object_or_404

def index(request):
    ''':arg
        显示仪表盘
    '''
    return render(request, 'assets/index.html')
def srclist(request):
    src_list = []
    result = models.Company.objects.all()

    for re in result:
        ip_count = models.Target_ip.objects.filter(company_ips__company__company_name=re.company_name).count()
        subdomain_count = models.Target_sudomain.objects.filter(company_domain__company__company_name=re.company_name).count()
        assert_count = ip_count + subdomain_count

        src_list.append([re.src_platform.src_platform_name,re.company_name,assert_count,re.c_time,re.m_time])

    return render(request,'assets/srclist.html',{'src_list':src_list})
def add(request):
    if request.method == "POST":
        pass
    else:
        src_platform = models.SRC_platform.objects.all()
        return render(request,'assets/add.html',locals())
def chksrcname(request):
    if request.method == 'POST':
        src_platform_name = request.POST.get('src_platform_name')
        data = models.SRC_platform.objects.filter(src_platform_name=src_platform_name).count()
        if data == 0:
            return JsonResponse({'data':0})
        else:
            return JsonResponse({'data':1})
    else:
        pass

def chkcomname(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        data = models.Company.objects.filter(company_name=company_name).count()
        if data == 0:
            return JsonResponse({'data':0})
        else:
            return JsonResponse({'data':1})
    else:
        pass


def addsrc(request):
    if request.method == 'POST':
        src_platform_name = request.POST.get('src_platform_name')
        src_platform_url = request.POST.get('src_platform_url')
        chkname = models.SRC_platform.objects.filter(src_platform_name=src_platform_name).count()
        if chkname != 0:
            return JsonResponse({"data":1})
        else:
            new_src_platform = models.SRC_platform()
            new_src_platform.src_platform_name = src_platform_name
            new_src_platform.src_platform_url = src_platform_url
            new_src_platform.save()
            return JsonResponse({"data": 0})
    else:
        pass
def addcom(request):

    if request.method == 'POST':
        src_platform_name = request.POST.get('src_platform_name')
        company_name = request.POST.get('company_name')
        company_domain_domains = request.POST.get('company_domain_domains')
        company_ips_ips = request.POST.get('company_ips_ips')
        chkname = models.Company.objects.filter(company_name=company_name).count()
        if chkname != 0:
            return JsonResponse({"data":1})
        else:
            src_platform = models.SRC_platform.objects.get(src_platform_name=src_platform_name)
            com_result = models.Company(company_name=company_name,src_platform=src_platform)
            com_result.save()
            com = models.Company.objects.get(company_name=company_name)
            if company_domain_domains == '':
                pass
            else:
                for company_domain in company_domain_domains.strip().splitlines():
                    com_domain = models.Company_domain(company=com,company_domain_domains=company_domain)
                    com_domain.save()
            if company_ips_ips == '':
                pass
            else:
                for company_ip in company_ips_ips.strip().splitlines():
                    com_ip = models.Company_ips(company=com,company_ips_ips=company_ip)
                    com_ip.save()
            return JsonResponse({"data": 0})
    else:
        pass
def domain(request):

    domains = models.Target_sudomain.objects.all()

    return render(request,'assets/domain.html',locals())
def ips(request):
    ips = models.Target_ip.objects.all()
    return render(request,'assets/ips.html',locals())

def company(request):
    companys = models.Company.objects.all()

    return render(request,'assets/company.html',locals())