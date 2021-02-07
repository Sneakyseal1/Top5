import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()


def trending_searches(country):
    data = []
    trends = pytrend.trending_searches(country)
    trends = trends.astype(str)
    print(trends.head(5))
    for i in range(0,5):
        data.append(trends.iloc[i][0])
    print(data)



country = "united_states"
trending_searches(country)
