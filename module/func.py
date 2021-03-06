from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, TemplateSendMessage, ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn, QuickReply, QuickReplyButton, MessageAction

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
#https://raw.githubusercontent.com/juice-kuo/super3000/master/static/images/TemplateSendMessage/
#http://120.125.72.233/~survey/static_images/
baseurl = 'https://raw.githubusercontent.com/juice-kuo/super3000/master/static/images/TemplateSendMessage/'
#'https://i.imgur.com/qUCe1UF.png'  baseurl + 'asisline.png'
def sendButton(event):  #關於我們
    
        message = TemplateSendMessage(
            alt_text='關於我們',
            template=ButtonsTemplate(
                thumbnail_image_url=baseurl + 'asisline.png',  #顯示的圖片
                title='關於我們',  #主標題
                text='請選擇：',  #副標題
                actions=[
                    URITemplateAction(  #開啟網頁
                        label='銘傳大學網站',
                        uri='https://web.mcu.edu.tw/'
                    ),
                    URITemplateAction(  #開啟網頁
                        label='應用統計與資料科學學系網站',
                        uri='http://web.asis.mcu.edu.tw/zh-hant'
                    ),
                    
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    
def sendCarousel(event):  #經濟部商業司相關網站
    
        message = [
            TextSendMessage(
                text = '利害關係人相關網頁'
            ),
            TextSendMessage(
                text = 'https://corp.104.com.tw/indexdda3.html?m=article&mid=102'
            ),
        ]
        line_bot_api.reply_message(event.reply_token,message)
    
def sendImgCarousel(event):  #金融相關網站
    
        message = TemplateSendMessage(
            alt_text='金融相關網站',
            template=ButtonsTemplate(
                thumbnail_image_url=baseurl + '金管會.png',  #顯示的圖片
                title='金融相關網站',  #主標題
                text='請選擇：',  #副標題
                actions=[
                    URITemplateAction(  #開啟網頁
                        label='金管會',
                        uri='https://www.fsc.gov.tw/ch/index.jsp'
                    ),
                    URITemplateAction(  #開啟網頁
                        label='證券期貨局',
                        uri='https://www.sfb.gov.tw/ch/home.jsp?id=882&parentpath=0,8'
                    ),
                    
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    
def sendPizza(event):

        message = TextSendMessage(
            text='請選擇想查詢之商業司相關網站',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="商工行政服務相關網站入口網", text="https://gcis.nat.gov.tw/mainNew/index.jsp")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="商工登記公示資料查詢服務", text="https://findbiz.nat.gov.tw/fts/query/QueryBar/queryInit.do")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="縣市別與近十年度公司設立登記案件統計", text="https://serv.gcis.nat.gov.tw/StatisticQry/cmpy/StaticFunction4.jsp")
                    ),
                    
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)






