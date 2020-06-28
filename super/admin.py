from django.contrib import admin
from super.models import company

# Register your models here.


class companyAdmin(admin.ModelAdmin):
    # 第三種方式，加入 ModelAdmin 類別，定義顯示欄位、欄位過濾資料、搜尋和排序
	list_display=('id','cComid','cPosition','cName','cSharemoney')
	ordering=('id',)
	
admin.site.register(company,companyAdmin)
