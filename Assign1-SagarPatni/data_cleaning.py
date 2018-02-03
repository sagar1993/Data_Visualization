import pandas as pd

df = pd.read_csv('10years.csv')

df['firstServe1'] = df['firstServe1'].str.replace('%','').astype('int64')
df['firstServe2'] = df['firstServe2'].str.replace('%','').astype('int64')
df['return1'] = df['return1'].str.replace('%','').astype('int64')
df['return2'] = df['return2'].str.replace('%','').astype('int64')
df['break1'] = df['break1'].str.replace('%','').astype('int64')
df['break2'] = df['break2'].str.replace('%','').astype('int64')
#df['total1'] = df['total1'].str.replace('%','').astype('int64')
#df['total2'] = df['total2'].str.replace('%','').astype('int64')
df['firstPointWon1'] = df['firstPointWon1'].str.replace('%','').astype('int64')
df['firstPointWon2'] = df['firstPointWon2'].str.replace('%','').astype('int64')
df['secPointWon1'] = df['secPointWon1'].str.replace('%','').astype('int64')
df['secPointWon2'] = df['secPointWon2'].str.replace('%','').astype('int64')

df_winner= df[[['year', 'player1', 'country1', 'firstServe1',
        'ace1', 'double1', 'firstPointWon1',
        'secPointWon1', 'fastServe1(km)',
        'avgFirstServe1', 'avgSecServe1',
        'break1', 'return1', 'total1',
        'winner1','error1', 'winner']
]]


df_runner = df[['year', 'player2', 'country2', 
       'firstServe2', 'ace2', 'double2',
       'firstPointWon2', 'secPointWon2',
       'fastServe2(km)', 'avgFirstServe2',
       'avgSecServe2', 'break2', 'return2',
       'total2', 'winner2', 'error2', 'winner']]
	   
df_runner_1 = pd.DataFrame(df_runner.as_matrix(), columns=df_winner.columns)

df_winner = df_winner.append(df_runner_1,ignore_index=True)

df_winner['win'] = (df_winner.player1 == df_winner.winner).astype('int64')

df_winner['total1'] = df_winner['total1'].str.replace('%','') 


df_winner[['firstServe1', 'ace1', 'double1',
       'firstPointWon1', 'secPointWon1', 'fastServe1(km)', 'avgFirstServe1',
       'avgSecServe1', 'break1', 'return1', 'total1', 'winner1', 'error1', 'win']] = df_winner[['firstServe1', 'ace1', 'double1',
       'firstPointWon1', 'secPointWon1', 'fastServe1(km)', 'avgFirstServe1',
       'avgSecServe1', 'break1', 'return1', 'total1', 'winner1', 'error1', 'win']].apply(pd.to_numeric)
	   


df_winner.columns = ['year', 'player', 'country', 'firstServe', 'ace', 'double',
       'firstPointWon', 'secPointWon', 'fastServe(km)', 'avgFirstServe',
       'avgSecServe', 'break', 'return', 'total', 'winn', 'error','winner', 'win']
	   
	   
	   """
	   correlation plot
	   
	   """

	   
import seaborn as sns
import numpy as np

corr = df_winner.corr()

mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

f, ax = plt.subplots(figsize=(11, 9))

cmap = sns.diverging_palette(220, 10, as_cmap=True)


sns.heatmap(corr,  cmap=cmap, mask=mask, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
			
			
			
