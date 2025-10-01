import pandas as pd
import numpy as np
#%%
df = pd.DataFrame ({
    'A': [1,2,np.nan,4],
    'B': [5,np.nan,np.nan,8],
    'C': [10,11,12,13]
})
#%%
print(df.isnull())
#%%
df_sin_nulos = df.dropna()
df_sin_nulos
#%%
#Rellenar valores nulos
df_rellena_nulos = df.fillna(value = 0)
df_rellena_nulos
#%%
df_relleno = df.fillna(method = 'ffill')
df_relleno
