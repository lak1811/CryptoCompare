import requests
import pandas as pd
from dateutil.parser import ParserError
def link(url,parameters,headers):
    # Make the API request
    

    # Make the request
    r = requests.get(url, params=parameters, headers=headers)
    pd.set_option('display.max_columns', None)
    if r.status_code==200:

        data = r.json()
        
        
        df=pd.DataFrame(data['data'])

        return df

        

        
        
    else:
        print(f"Error: {r.status_code}, {r.text}")
        

