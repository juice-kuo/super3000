from django.shortcuts import render
from django.http import HttpResponse
from super.models import company
from django.db.models import Q
# Create your views here.
def listall(request):  
	companys = company.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
	return render(request, "listall.html", locals())
	

# 查詢

def selecct_list(request):
	cComid = request.POST.get('cComid',False)
	cPosition = request.POST.get('cPosition',False)
	cName = request.POST.get('cName',False)
	cSharemoney = request.POST.get('cSharemoney',False)
	if cSharemoney == '0':
		select_all = company.objects.filter( Q(cComid__icontains=cComid) & Q(cPosition__icontains=cPosition) & Q(cSharemoney__icontains=cSharemoney))
	else:
		select_all = company.objects.filter( Q(cComid__icontains=cComid) & Q(cPosition__icontains=cPosition) & Q(cSharemoney=cSharemoney))
	return render(request,'select_all.html', {'select_all': select_all})
