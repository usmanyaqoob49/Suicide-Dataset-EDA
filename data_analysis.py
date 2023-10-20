import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


df= pd.read_csv('master.csv')

#figure 1
#1) Is the suicide rate more prominent in some age categories than others?
suicide_rate_sum= df.groupby('age', as_index=False)['suicides/100k pop'].sum()

suicide_rate_sum_fig = px.bar(data_frame= suicide_rate_sum,
                            x= 'age',
                            y= 'suicides/100k pop')
# Set the background color of the plot and paper to black
suicide_rate_sum_fig.update_layout(
    plot_bgcolor='black',  # Background color of the plot area
    paper_bgcolor='black'  # Background color of the entire graph
)


#figure 2 
#What is the effect of the population on suicide rates?
population_affect_on_suicide_rate_fig = px.scatter(data_frame=df,
           x='population',
            y= 'suicides/100k pop')
# Set the background color of the plot and paper to black
population_affect_on_suicide_rate_fig.update_layout(
    plot_bgcolor='black',  # Background color of the plot area
    paper_bgcolor='black'  # Background color of the entire graph
)
#figure 3
#What is the effect of the GDP of a country on suicide rates?
gdppercapita_effect_on_suicide_rate_fig= px.scatter(data_frame= df,
            x= 'suicides/100k pop',
            y= 'gdp_per_capita ($)')
# Set the background color of the plot and paper to black
gdppercapita_effect_on_suicide_rate_fig.update_layout(
    plot_bgcolor='black',  # Background color of the plot area
    paper_bgcolor='black'  # Background color of the entire graph
)

# figure 4
trend = df.groupby('year', as_index=False)['suicides/100k pop'].mean()
suicide_rate_trend_over_years_fig= px.bar(data_frame= trend,
       x= 'year',
       y= 'suicides/100k pop',)
# Set the background color of the plot and paper to black
suicide_rate_trend_over_years_fig.update_layout(
    plot_bgcolor='black',  # Background color of the plot area
    paper_bgcolor='black'  # Background color of the entire graph
)

#figure 5
male_female_trend = df.groupby('sex', as_index=False)['suicides/100k pop'].mean()
male_female_suicide_rate_fig= px.bar(data_frame= male_female_trend,
       x= 'sex',
       y= 'suicides/100k pop')
# Set the background color of the plot and paper to black
male_female_suicide_rate_fig.update_layout(
    plot_bgcolor='black',  # Background color of the plot area
    paper_bgcolor='black'  # Background color of the entire graph
)
#figure 6
male_female_distribution_fig = px.violin(df, x='sex', y='suicides/100k pop', box=True)# Set the background color of the plot and paper to black
male_female_distribution_fig.update_layout(
    plot_bgcolor='black',  # Background color of the plot area
    paper_bgcolor='black'  # Background color of the entire graph
)