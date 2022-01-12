#%%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("GDPlist.csv")
df['Country']= df['Country'].map(lambda x:x.lstrip('�'))
df

# %%
df.info()

#%%
df['GDP (millions of US$)'].max()

# %%
df['GDP (millions of US$)'].min()

# %%
df['GDP (millions of US$)'].hist()

# %%
df['Continent'].value_counts()

# %%
continent_df_sum = df.groupby(["Continent"])["GDP (millions of US$)"].sum()
continent_df_sum

# %%
continent_df_mean = df.groupby(["Continent"])["GDP (millions of US$)"].mean()
continent_df_mean

# %%
df2=pd.concat([continent_df_sum,continent_df_mean], axis=1)
df2 = df2.rename({'Continent': 'Tên châu lục', 'GDP (millions of US$)': 'Tổng GDP', 'GDP (millions of US$)': 'TBC GDP'}, axis=1)
df2
# %%
