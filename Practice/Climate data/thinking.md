# Overview
* Create program that takes data from met office and presents it on a line graph

# Approach
* go to met office
* store data in a dictionary of 2d arrays, each array is the type of data, each key is the time, each value is the data, for example, a temperature array would store the temperature at each hour of the day, a rain array would store rain etc. 
* take the last 5 years of data, put in text file
* analyse structure
* put data into excel and see what the graph would look like 
* year, month, max tempt, min temp, days below 0*C, rainfall, sun hours, * is estimated



# Inputs
* data set from met office, take the year, month, max/min temperature, rainfall
* https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/bradforddata.txt

# Outputs
* line graph / bar graph

# Technical needs
* library to create a graph from the data
* where do fields begin and end
* how to parse
* remove CR(10) and LF(13)

# Test and validate 
* 