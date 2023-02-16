import eia
import pandas as pd

api_key = "api-key"
api = eia.API(api_key)

keyword_search = api.search_by_keyword(keyword=['crude oil', 'price'],
                                       rows=15, 
                                       return_list=False)


df = pd.DataFrame(keyword_search)
print(df.shape)
