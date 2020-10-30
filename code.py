import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.figure_factory import create_table


#Gapminder data is already on plotly, so we don't need to import a dataset.
gapminder = px.data.gapminder()

#Let's see the first 10 row of our data
table= create_table(gapminder.head(10))
py.iplot(table)

#Visualization of Population over the Years
data_canada = px.data.gapminder().query("country=='Canada'")
fig=px.bar(data_canada, x='year', y='pop',
hover_data=['lifeExp', 'gdpPercap'], #when your mouse is over the data it also shows you Life Expectancy and GdpPerCap
color = 'lifeExp',
labels={'Population of Canada'}, 
height=400)
fig.show()

#Scatter plot of Gdp vs Life Expectancy for all countries for 2007
gapminder2007 = gapminder.query("year==2007")
px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", 
           color="continent", hover_name="country",
           )

#Turning Scatter plot to a Bubble Chart
px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", 
           color="continent", hover_name="country",
           size="pop", size_max=60, 
           )

#Facet Plots
px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", color="continent",
           size="pop", size_max=40,
           hover_name="country",
           facet_col="continent", log_x=True)

#Creating Animation
fig= px.scatter(gapminder, x="gdpPercap", y="lifeExp", color='continent',
          size="pop", size_max=60, hover_name="country", animation_frame='year',
          animation_group="country", log_x=True, range_x=[100,100000], range_y=[25,90],
          labels=dict(pop='Population', gdpPercap="GDP per Capita", lifeExp="Life Expectancy"))
fig.show()
# to make animation work on VSCode use this: fig.show(renderer="notebook")


#Geographical Visualization on World Map
fig=px.choropleth(gapminder, locations="iso_alpha", color="lifeExp", hover_name="country",
             animation_frame="year", color_continuous_scale=px.colors.sequential.Plasma,
             projection="natural earth")
fig.show()
# to make animation work on  VSCode use this: fig.show(renderer="notebook")


#Geographical Visualization on Eath 
fig= px.choropleth(gapminder, locations="iso_alpha", color="lifeExp", hover_name="country",
             animation_frame="year", color_continuous_scale=px.colors.sequential.Plasma,
             projection="orthographic")
fig.show()
# to make animation work on  VSCode use this: fig.show(renderer="notebook")
