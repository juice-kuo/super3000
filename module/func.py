from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, TemplateSendMessage, ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendButton(event):  #關於我們
    try:
        message = TemplateSendMessage(
            alt_text='關於我們',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',  #顯示的圖片
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
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))


def sendCarousel(event):  #經濟部商業司相關網站
    try:
        message = [
            TextSendMessage(
                text = '利害關係人相關網頁'
            ),
            TextSendMessage(
                text = 'https://corp.104.com.tw/indexdda3.html?m=article&mid=102'
            ),
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendImgCarousel(event):  #金融相關網站
    try:
        message = TemplateSendMessage(
            alt_text='金融相關網站',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',  #顯示的圖片
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
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendPizza(event):
    try:
        message = TextSendMessage(
            text='請選擇想查詢之商業司相關網站',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="商工行政服務相關網站入口網", uri='https://gcis.nat.gov.tw/mainNew/index.jsp')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="商工登記公示資料查詢服務", uri='https://findbiz.nat.gov.tw/fts/query/QueryBar/queryInit.do')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="縣市別與近十年度公司設立登記案件統計", uri='https://serv.gcis.nat.gov.tw/StatisticQry/cmpy/StaticFunction4.jsp')
                    ),
                    
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))





