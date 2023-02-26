

#Code to fetch the data from The Graph's endpoint for analysis. The transactions are filtered with Token ID = 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2
#This is the token ID for Wrapped ETH (WETH) : https://etherscan.io/token/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2
import requests
import json
import pandas as pd
from datetime import datetime

# Point to correct subgraph URL
#Uniswap V3 GraphQL endpoint link - https://thegraph.com/hosted-service/subgraph/uniswap/uniswap-v3
url = 'https://api.thegraph.com/subgraphs/name/messari/opensea-v1-ethereum'

# initialize full_data
df1_fulldata = pd.DataFrame()
df2_fulldata = pd.DataFrame()
df_data = pd.DataFrame()

#Fetching top records ordered by date
for i in range(0,2) :
    # Set query (which uses text input to specify ETH wallet addresses)
    query = '''query {
        trades( first: 1000, skip: %s, where: {collection: "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"}) {
            
            tokenId
            priceETH
            timestamp
            

            }
            }''' % (i*1000)


    # Make the request
    r = requests.post(url, json={'query': query})
    
    # JSON adjustment
    json_data = json.loads(r.text)
    
    # extract JSON to convert to a dataframe
    df_data = json_data['data']['trades']
    df1_fulldata = pd.DataFrame(df_data)
        
    df2_fulldata = pd.concat([df2_fulldata,df1_fulldata])
    

#Removing NULLS - Data Cleaning
df1 = df2_fulldata.dropna()

#Converting from Unix timestamp to datetime
df1['timestamp'] = pd.to_datetime(df1['timestamp'],unit='s')
df1['timestamp'] = pd.to_datetime(df1['timestamp']).dt.date

print(df1)


#Code to fetch the data from The Graph's endpoint for analysis. The transactions are filtered with Token ID = 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2
#This is the token ID for Wrapped ETH (WETH) : https://etherscan.io/token/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2
import requests
import json
import pandas as pd
from datetime import datetime

# Point to correct subgraph URL
#Uniswap V3 GraphQL endpoint link - https://thegraph.com/hosted-service/subgraph/uniswap/uniswap-v3
url = 'https://api.thegraph.com/subgraphs/name/messari/opensea-v2-ethereum'

# initialize full_data
df1_fulldata = pd.DataFrame()
df2_fulldata = pd.DataFrame()
df_data = pd.DataFrame()

#Fetching top records ordered by date
for i in range(0,2) :
    # Set query (which uses text input to specify ETH wallet addresses)
    query = '''query {
        trades( first: 1000, skip: %s, where: {collection: "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"}) {
            
            tokenId
            priceETH
            timestamp
            

            }
            }''' % (i*1000)


    # Make the request
    r = requests.post(url, json={'query': query})
    
    # JSON adjustment
    json_data = json.loads(r.text)
    
    # extract JSON to convert to a dataframe
    df_data = json_data['data']['trades']
    df1_fulldata = pd.DataFrame(df_data)
        
    df2_fulldata = pd.concat([df2_fulldata,df1_fulldata])
    

#Removing NULLS - Data Cleaning
df2 = df2_fulldata.dropna()

#Converting from Unix timestamp to datetime
df2['timestamp'] = pd.to_datetime(df2['timestamp'],unit='s')
df2['timestamp'] = pd.to_datetime(df2['timestamp']).dt.date

print(df2)


#Code to fetch the data from The Graph's endpoint for analysis. The transactions are filtered with Token ID = 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2
#This is the token ID for Wrapped ETH (WETH) : https://etherscan.io/token/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2
import requests
import json
import pandas as pd
from datetime import datetime

# Point to correct subgraph URL
#Uniswap V3 GraphQL endpoint link - https://thegraph.com/hosted-service/subgraph/uniswap/uniswap-v3
url = 'https://api.thegraph.com/subgraphs/name/messari/opensea-seaport-ethereum'

# initialize full_data
df1_fulldata = pd.DataFrame()
df2_fulldata = pd.DataFrame()
df_data = pd.DataFrame()

#Fetching top records ordered by date
for i in range(0,2) :
    # Set query (which uses text input to specify ETH wallet addresses)
    query = '''query {
        trades( first: 1000, skip: %s, where: {collection: "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"}) {
            
            tokenId
            priceETH
            timestamp
            

            }
            }''' % (i*1000)


    # Make the request
    r = requests.post(url, json={'query': query})
    
    # JSON adjustment
    json_data = json.loads(r.text)
    
    # extract JSON to convert to a dataframe
    df_data = json_data['data']['trades']
    df1_fulldata = pd.DataFrame(df_data)
        
    df2_fulldata = pd.concat([df2_fulldata,df1_fulldata])
    

#Removing NULLS - Data Cleaning
df3 = df2_fulldata.dropna()

#Converting from Unix timestamp to datetime
df3['timestamp'] = pd.to_datetime(df3['timestamp'],unit='s')
df3['timestamp'] = pd.to_datetime(df3['timestamp']).dt.date

print(df3)


#Merging the above 3 dataframes into one
frames = [df1, df2, df3]

data = pd.concat(frames)
data.reset_index(inplace=True)
data = data.drop(['index'], axis=1)

print(data)



data.to_csv('Data_BoredApe.csv',index='False')

