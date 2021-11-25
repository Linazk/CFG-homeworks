import pandas_datareader as pdr
import datetime
from matplotlib import pyplot as plt
import pandas as pd

# TASK 1
# getting the google api
goog_api = pdr.get_data_yahoo('GOOG',
                              start=datetime.datetime(2020, 1, 1),
                              end=datetime.datetime(2021, 1, 1))

#saving it
df_goog = pd.DataFrame(goog_api)
df_goog.to_csv('google_stock', index=False) # turning it to dataframe
#reading it 
df_goog = pd.read_csv('google_stock') # to csv

# displaying data saved
pd.set_option('display.max_rows', df_goog.shape[0]+1)
print(df_goog)


# plotting
fig = plt.figure(dpi=300) # increasing the quality
df_goog['Close'].plot(grid=True,)
# adding a title
plt.title('Google Stock Prices')
plt.show()

# TASK 2

#getting the microsoft api 
msft_api = pdr.get_data_yahoo('MSFT',
                              start=datetime.datetime(2020, 1, 1),
                              end=datetime.datetime(2021, 1, 1))

#saving it
df_msft = pd.DataFrame(msft_api) 
df_msft.to_csv('msft_stock', index=False)
#reading it 
df_msft = pd.read_csv('msft_stock') 

# displaying data saved
pd.set_option('display.max_rows', df_goog.shape[0]+1)
print(df_goog)

#plotting
fig2 = plt.figure(dpi=300)
df_msft['Close'].plot(grid=True,color='green')
plt.title('Microsoft Stock Prices')
plt.show()



