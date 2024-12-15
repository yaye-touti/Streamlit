```python
#import des librerie
import pandas as pd
```


```python
#recuperation des données 
fichierName ='all_commodities_futures_collection.csv'
df = pd.read_csv(fichierName)
```


```python
#Aperçu des données (10 premiers lignes)
df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ticker</th>
      <th>commodity</th>
      <th>category</th>
      <th>date</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HE=F</td>
      <td>Lean Hogs</td>
      <td>Animal Products</td>
      <td>2002-03-04</td>
      <td>59.700001</td>
      <td>59.875000</td>
      <td>59.599998</td>
      <td>59.650002</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>HE=F</td>
      <td>Lean Hogs</td>
      <td>Animal Products</td>
      <td>2002-03-05</td>
      <td>59.150002</td>
      <td>59.150002</td>
      <td>58.700001</td>
      <td>58.799999</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>HE=F</td>
      <td>Lean Hogs</td>
      <td>Animal Products</td>
      <td>2002-03-06</td>
      <td>58.500000</td>
      <td>58.799999</td>
      <td>57.700001</td>
      <td>57.700001</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>HE=F</td>
      <td>Lean Hogs</td>
      <td>Animal Products</td>
      <td>2002-03-07</td>
      <td>58.200001</td>
      <td>58.599998</td>
      <td>58.000000</td>
      <td>58.400002</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>HE=F</td>
      <td>Lean Hogs</td>
      <td>Animal Products</td>
      <td>2002-03-08</td>
      <td>58.250000</td>
      <td>58.250000</td>
      <td>57.900002</td>
      <td>58.049999</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>HE=F</td>
      <td>Lean Hogs</td>
      <td>Animal Products</td>
      <td>2002-03-11</td>
      <td>57.924999</td>
      <td>58.025002</td>
      <td>57.575001</td>
      <td>57.575001</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>HE=F</td>
      <td>Lean Hogs</td>
      <td>Animal Products</td>
      <td>2002-03-12</td>
      <td>57.349998</td>
      <td>57.549999</td>
      <td>57.250000</td>
      <td>57.275002</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>HE=F</td>
      <td>Lean Hogs</td>
      <td>Animal Products</td>
      <td>2002-03-13</td>
      <td>57.200001</td>
      <td>57.200001</td>
      <td>56.625000</td>
      <td>56.700001</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>HE=F</td>
      <td>Lean Hogs</td>
      <td>Animal Products</td>
      <td>2002-03-14</td>
      <td>56.775002</td>
      <td>56.825001</td>
      <td>56.200001</td>
      <td>56.724998</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>HE=F</td>
      <td>Lean Hogs</td>
      <td>Animal Products</td>
      <td>2002-03-15</td>
      <td>55.075001</td>
      <td>55.224998</td>
      <td>55.025002</td>
      <td>55.075001</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Liste des colonnes
for col in df.columns:
    print(f"- {col}")
```

    - ticker
    - commodity
    - category
    - date
    - open
    - high
    - low
    - close
    - volume
    


```python
#Nombre d'observation 
print('Notre jeux de données comporte :')
print(df.shape[0], 'lignes')
print(df.shape[1], 'colonnes')
```

    Notre jeux de données comporte :
    135295 lignes
    9 colonnes
    


```python
#Type de chaque variable
print("types des variables: ")
df.info()
```

    types des variables: 
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 135295 entries, 0 to 135294
    Data columns (total 9 columns):
     #   Column     Non-Null Count   Dtype  
    ---  ------     --------------   -----  
     0   ticker     135295 non-null  object 
     1   commodity  135295 non-null  object 
     2   category   135295 non-null  object 
     3   date       135295 non-null  object 
     4   open       135295 non-null  float64
     5   high       135295 non-null  float64
     6   low        135295 non-null  float64
     7   close      135295 non-null  float64
     8   volume     135295 non-null  int64  
    dtypes: float64(4), int64(1), object(4)
    memory usage: 9.3+ MB
    


```python
# Convertir la colonne 'date' au format datetime
df['date'] = pd.to_datetime(df['date'])
```


```python
#Plage de date
debut = df['date'].min()
fin = df['date'].max()

print("Date de début :", debut)
print("Date de fin :", fin)
```

    Date de début : 2000-01-03 00:00:00
    Date de fin : 2024-06-24 00:00:00
    


```python
#Valeur manquante
df.isnull().sum()
```




    ticker       0
    commodity    0
    category     0
    date         0
    open         0
    high         0
    low          0
    close        0
    volume       0
    dtype: int64




```python
#Creation de nouvelle colonne
#"daily_trend" :indique si le prix de clôture est plus élevé ou plus bas que le prix d’ouverture.

df['daily_trend'] = df.apply(
    lambda row: 'Positive' if row['close'] > row['open'] else ('Negative' if row['close'] < row['open'] else 'Neutral'),
    axis=1
)
```


```python
#'volatility' mesure l'amplitude des variations de prix pour une commodité sur une journée.
df['volatility'] = ((df['high'] - df['low']) / df['open']) * 100
```


```python
#relative_gap est l'écart moyen relatif entre les prix de clôture et d’ouverture, 
#qui montre la variation relative en pourcentage :
df['relative_gap'] = ((df['close'] - df['open']) / df['open']) * 100
```


```python
#Apperçu des nouvelles colonnes
df[['volatility', 'daily_trend', 'relative_gap']].head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>volatility</th>
      <th>daily_trend</th>
      <th>relative_gap</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.460639</td>
      <td>Negative</td>
      <td>-0.083751</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.760779</td>
      <td>Negative</td>
      <td>-0.591720</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.880339</td>
      <td>Negative</td>
      <td>-1.367520</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.030925</td>
      <td>Positive</td>
      <td>0.343644</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.600856</td>
      <td>Negative</td>
      <td>-0.343349</td>
    </tr>
  </tbody>
</table>
</div>




```python
#statistique
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
      <th>volatility</th>
      <th>relative_gap</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>135295</td>
      <td>135295.000000</td>
      <td>135295.000000</td>
      <td>135295.000000</td>
      <td>135295.000000</td>
      <td>1.352950e+05</td>
      <td>135295.000000</td>
      <td>135295.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2012-09-22 04:45:27.373517056</td>
      <td>430.655889</td>
      <td>434.262222</td>
      <td>427.086024</td>
      <td>430.646209</td>
      <td>3.398976e+04</td>
      <td>2.100853</td>
      <td>-0.013889</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2000-01-03 00:00:00</td>
      <td>-14.000000</td>
      <td>0.507000</td>
      <td>-40.320000</td>
      <td>-37.630001</td>
      <td>0.000000e+00</td>
      <td>-218.571424</td>
      <td>-312.239154</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2006-10-23 00:00:00</td>
      <td>20.224999</td>
      <td>20.400000</td>
      <td>20.041000</td>
      <td>20.193000</td>
      <td>1.040000e+02</td>
      <td>0.879423</td>
      <td>-0.768389</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2012-11-02 00:00:00</td>
      <td>110.500000</td>
      <td>111.529999</td>
      <td>109.500000</td>
      <td>110.500000</td>
      <td>2.663000e+03</td>
      <td>1.791280</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2018-09-12 00:00:00</td>
      <td>588.750000</td>
      <td>593.000000</td>
      <td>584.000000</td>
      <td>588.500000</td>
      <td>3.070650e+04</td>
      <td>2.877327</td>
      <td>0.748876</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2024-06-24 00:00:00</td>
      <td>11967.000000</td>
      <td>12261.000000</td>
      <td>11132.000000</td>
      <td>11878.000000</td>
      <td>2.288230e+06</td>
      <td>328.087995</td>
      <td>48.108743</td>
    </tr>
    <tr>
      <th>std</th>
      <td>NaN</td>
      <td>667.196460</td>
      <td>674.097564</td>
      <td>660.621961</td>
      <td>667.494880</td>
      <td>8.315627e+04</td>
      <td>2.155053</td>
      <td>2.004861</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 135295 entries, 0 to 135294
    Data columns (total 12 columns):
     #   Column        Non-Null Count   Dtype         
    ---  ------        --------------   -----         
     0   ticker        135295 non-null  object        
     1   commodity     135295 non-null  object        
     2   category      135295 non-null  object        
     3   date          135295 non-null  datetime64[ns]
     4   open          135295 non-null  float64       
     5   high          135295 non-null  float64       
     6   low           135295 non-null  float64       
     7   close         135295 non-null  float64       
     8   volume        135295 non-null  int64         
     9   daily_trend   135295 non-null  object        
     10  volatility    135295 non-null  float64       
     11  relative_gap  135295 non-null  float64       
    dtypes: datetime64[ns](1), float64(6), int64(1), object(4)
    memory usage: 12.4+ MB
    


```python
#Liste des commodity et des catégorie
print(df['commodity'].unique())
print(df['category'].unique())
```

    ['Lean Hogs' 'Live Cattle' 'Cocoa' 'Coffee' 'Cotton'
     'Random Length Lumber' 'Orange Juice' 'Sugar' 'Crude Oil' 'Heating Oil'
     'Natural Gas' 'RBOB Gasoline' 'Brent Crude Oil' 'Gold' 'Silver'
     'Platinum' 'Copper' 'Palladium' 'Corn' 'Oat' 'KC HRW Wheat' 'Rough Rice'
     'Soybean Oil' 'Soybean']
    ['Animal Products' 'Agricultural Commodities' 'Fossil Fuels'
     'Precious Metals' 'Grains and Cereals']
    


```python
chemin ='C:/Users/yayet/OneDrive/Documents/Paris_1_panthéon_Sorbonne/DataViz/Projet_Streamlit/Data/data_net/commodities_market.csv'
df.to_csv(chemin, index=False, encoding="utf-8")
print(f"Fichier enregistré avec succès à : {chemin}")
```

    Fichier enregistré avec succès à : C:/Users/yayet/OneDrive/Documents/Paris_1_panthéon_Sorbonne/DataViz/Projet_Streamlit/Data/data_net/commodities_market.csv
    


```python

```
