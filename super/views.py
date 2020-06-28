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


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
                    if mtext == '@關於我們':
                        func.sendButton(event)

                    elif mtext == '@公司利害關係人相關網站':
                        func.sendCarousel(event)
    
                    elif mtext == '@金融相關網站':
                        func.sendImgCarousel(event)
    
                    elif mtext == '@經濟部商業司相關網站':
                        func.sendPizza(event)
    
                    
    
            if isinstance(event, PostbackEvent):  #PostbackTemplateAction觸發此事件
                backdata = dict(parse_qsl(event.postback.data))  #取得Postback資料
                if backdata.get('action') == 'buy':
                    func.sendBack_buy(event, backdata)
                elif backdata.get('action') == 'sell':
                    func.sendBack_sell(event, backdata)

        return HttpResponse()

    else:
        return HttpResponseBadRequest()
