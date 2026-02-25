import requests
from bs4 import BeautifulSoup

def get_google_finance_price(ticker):
    # Google Finance 的台股格式通常是 TPE:2330
    url = f"https://www.google.com/finance/quote/{ticker}:TPE"
    
    # 模擬瀏覽器標頭，避免被 Google 判定為機器人
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return "無法連線至網頁"

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Google Finance 目前常用的股價 Class 名稱為 'YMlKec' 且字體較大者為 'fxKbKc'
        # 我們使用 select_one 尋找特定的 CSS Class
        price_element = soup.select_one('div.YMlKec.fxKbKc')
        
        if price_element:
            return price_element.text
        else:
            return "找不到價格標籤，可能是網頁結構已更換"
            
    except Exception as e:
        return f"發生錯誤: {e}"

# 執行抓取台積電 (2330)
stock_no = "2330"
current_price = get_google_finance_price(stock_no)

print(f"2.0版本")
print(f"--- 查詢結果 ---")
print(f"股票代碼: {stock_no}")
print(f"目前股價: {current_price}")