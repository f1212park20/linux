from pykrx import stock
from pykrx import bond

# Ticker 조회
# get_market_ticker_list 메서드는 지정한 일자(YYYYMMDD)의 코스피 시장에 상장된 ticker를 리스트로 반환
tickers = stock.get_market_ticker_list("20190225")
print(tickers)

# market 옵션을 추가하면 조회 시장을 지정할 수 있습니다. KOSPI, KOSDAQ, KONEX 시장을 지정할 수 있으며, ALL은 모든 시장에서 티커를 조회합니다.
# 입력하지 않을 경우 KOSPI 시장을 조회합니다.
tickers = stock.get_market_ticker_list("20190225", market="KOSDAQ")
print(tickers)

