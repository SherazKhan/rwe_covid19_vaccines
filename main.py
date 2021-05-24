import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
sns.set(style='whitegrid', context='talk')


path = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
df = pd.read_csv(path)
df['date'] = df['date'].apply(lambda x: dt.datetime.strptime(x,'%Y-%m-%d'))


locations = ['United States', 'Israel', 'United Kingdom', 'United Arab Emirates', 'Bahrain', 'Chile', 'Hungary']
sns.color_palette("bright", len(locations))

start_date = dt.datetime(2020, 12, 14)
end_date = df['date'].max()

start_time = pd.to_datetime(start_date)
end_time = pd.to_datetime(end_date)
columns=['location','date', 'new_cases_smoothed_per_million',
         'new_deaths_smoothed_per_million', 'total_vaccinations_per_hundred']
time_idx = (df['date']>=start_time) & (df['date']<=end_time - dt.timedelta(days=1))

plt.figure()
for location in locations:
    print(location)
    df_plt = df[(time_idx) & (df['location'].isin([location]))][columns].set_index('date')
    df_plt['tv'] = df_plt['total_vaccinations_per_hundred']/100
    df_plt['new_cases_smoothed_per_million'] = df_plt['new_cases_smoothed_per_million'].rolling(7).mean() # futher smooting of 7 days, 14 days in total
    df_plt['nc'] = np.log10(df_plt['new_cases_smoothed_per_million'].div(df_plt['new_cases_smoothed_per_million'].iloc[:42].mean()))
    sns.lineplot(x="tv", y="nc", data=df_plt, linewidth=5, label=location)
    plt.xlabel('Total Vaccinations per Total Population')
    plt.ylabel('Log-Change in New Cases (14 days moving average) Since 14th December 2020')



plt.figure()
for location in locations:
    print(location)
    df_plt = df[(time_idx) & (df['location'].isin([location]))][columns].set_index('date')
    df_plt['tv'] = df_plt['total_vaccinations_per_hundred']/100
    df_plt['new_deaths_smoothed_per_million'] = df_plt['new_deaths_smoothed_per_million'].rolling(7).mean() # futher smooting of 7 days, 14 days in total
    df_plt['nc'] = np.log10(df_plt['new_deaths_smoothed_per_million'].div(df_plt['new_deaths_smoothed_per_million'].iloc[:42].mean()))
    sns.lineplot(x="tv", y="nc", data=df_plt, linewidth=5, label=location)
    plt.xlabel('Total Vaccinations per Total Population')
    plt.ylabel('Log-Change in New Deaths (14 days moving average) Since 14th December 2020')


