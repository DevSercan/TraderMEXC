from src.utils.helper import getConfig, clear, getLanguage, getAPIKeys
from src.classes.Color import Color # Konsolda renkli yazı yazma özelliği sunar.
from src.classes.Log import Log # Günlük tutma (Loglama) işlemleri için kullanılan sınıfı içe aktarıyoruz.
import ccxt

log = Log() # Log sınıfını nesne olarak tutar.
CONFIG = getConfig()
LANG = getLanguage(CONFIG["language"])

def main():
    """ Ana fonksiyondur. """
    try:
        clear()
        apiKeys = getAPIKeys()
        accessKey = apiKeys["accessKey"]
        secretKey = apiKeys["secretKey"]
        exchange = ccxt.mexc({
            'apiKey': accessKey,
            'secret': secretKey,
            'enableRateLimit': True,  # API istek sınırlarına uyulmasını sağlar
        })
        symbol = 'BTC/USDT'
        quantity = 0.001
        print(f"accessKey: {accessKey}\nsecretKey: {secretKey}")
        print(exchange.fetch_ticker(symbol)["last"])
        orderType = "market"
        orderSide = "buy"
        order = exchange.create_market_order(symbol, orderType, orderSide, quantity)
        print(order)
    except Exception as e:
        log.error(f"Unexpected error in 'main' function:\n{e}")

if __name__ == "__main__":
    main()
    input(f"{Color.lblack}\n{LANG['enterToExit']}{Color.reset}")
