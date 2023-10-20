from dash import Dash, html, dcc

#now we need to imoprt the visualization figure we have created in the data analysis.py\
from data_analysis import suicide_rate_sum_fig
#effect of poplation image
from data_analysis import population_affect_on_suicide_rate_fig
#effect of gdp per capita
from data_analysis import gdppercapita_effect_on_suicide_rate_fig
#Trend of suicide rate over the years
from data_analysis import suicide_rate_trend_over_years_fig
#male and female suicide rate
from data_analysis import male_female_suicide_rate_fig
#male and female distribution
from data_analysis import male_female_distribution_fig

#making the app as an instance of the dash
app= Dash(__name__)

app.layout = html.Div([
    #using div which is a html tag
    html.H1('Suicide Rate Analysis', id= 'fig1', style= {'textAlign': 'center'}),
    #-------------------------------------------------Row 1---------------------------------------------------------------------------------------------------------
    html.Div([
        #column 1 of the row 1  
        html.Div([
            html.H2('Suicide Rate in Different Age Groups', style={'textAlign': 'center'}),
            #using dash core component--->Graph is to show the figure in dash
            dcc.Graph(figure= suicide_rate_sum_fig),
            #writing the insight in Bold
            html.P(html.B('As you can see from sum of the suicides/100 pop("Suicide rate"), it is higher in 75+ year people and with age it reduces much and lowest suicide rate is in youngest age catregory'))
            ], style= {'flex': 1, 'width': '50%'}),

        #column 2 of the row 1
        html.Div([
            html.H2('Effect of Population on Suicide Rate', style={'textAlign': 'center'}),
            dcc.Graph(figure= population_affect_on_suicide_rate_fig),
            html.P(html.B('Highest Population is not a major cause of high suicide rate.'))
            ], style= {'flex' : 1, 'width': '50%'}),], style= {'display':'flex', 'flex-direction': 'row'}),
    #----------------------------------------------------Row 1 end---------------------------------------------------------------------------------------------------

        
    #----------------------------------------------------Row 2--------------------------------------------------------------------------------------------------------
    html.Div([
        #Column 1 of row 2----->effect of gdp_per_capita on suicide rate
        html.Div([
            html.H2('Effect of GDP_per_Capita on Suicide Rate', style={'textAlign': 'center'}),
            dcc.Graph(figure= gdppercapita_effect_on_suicide_rate_fig),
            html.P(html.B('We are seeing Effect of gpd_per_capita on suicide rate , as you can when Suicide rate is low, gpd_per_capita is pretty high. And when Suicide Rate start Increasing gpd_per_capita is coming down with it.'))
            ], style= {'flex': 1, 'width': '50%'}),

        #Column 2 of row 2
        html.Div([
            html.H2('Trend of Suicide Rate Across all Years', style= {'textAlign': 'center'}),
            dcc.Graph(figure= suicide_rate_trend_over_years_fig),
            html.P(html.B('From the above graph we can see upward trend till 1995 and then there is downward trend till the very last where a upward spike is present.'))
        ], style= {'flex': 1, 'width': '50%'}),
        ], style= {'display': 'flex', 'flex-direction': 'row'}),
    
    #-------------------------------------------------------Row 2 end------------------------------------------------------------------------------------------------


    #----------------------------------------------------------Row 3-------------------------------------------------------------------------------------------------
    html.Div([
        #column1 of row 3
        html.Div([
            html.H2('Males and Females Suicide Rates', style= {'textAlign': 'center'}),
            dcc.Graph(figure= male_female_suicide_rate_fig),
            html.P(html.B('Suicide Rate in Males is way higher than females.'))
        ], style= {'flex': 1, 'width': '50%'}),

        #column 2 of row 3
        html.Div([
            html.H2('Distribution of Males and Females Suicide Rate', style={'textAlign': 'center'}),
            dcc.Graph(figure= male_female_distribution_fig),
            html.P(html.B('Distribution of both genders is shown above.'))
        ], style= {'flex': 1, 'width': '50%'}),
        ],style= {'display': 'flex', 'flex-direction': 'row'}),
])
    #----------------------------------------------------------End of Row 3---------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug= True)