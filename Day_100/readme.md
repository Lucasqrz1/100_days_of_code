# US Police Fatalities Data Analysis

## Project Overview
This project analyzes data from The Washington Post's database of fatal shootings by police officers in the United States since January 1, 2015. The analysis explores various aspects of these incidents, including demographic patterns, geographical distribution, and correlations with socioeconomic factors.

## Data Sources
The analysis uses several datasets:
1. **Deaths_by_Police_US.csv**: Main dataset containing information about fatal shootings
2. **Median_Household_Income_2015.csv**: US census data on median household income
3. **Pct_People_Below_Poverty_Level.csv**: Poverty rate statistics by state
4. **Pct_Over_25_Completed_High_School.csv**: Educational attainment data
5. **Share_of_Race_By_City.csv**: Racial demographic information by city

## Analysis Topics
The notebook explores:
- Poverty rates across US states
- High school graduation rates and their correlation with poverty
- Racial demographics of US states
- Analysis of police shooting victims by:
  - Race
  - Gender
  - Age
  - Mental illness status
  - Armed vs. unarmed status
- Geographical distribution of incidents
- Temporal trends in police shootings

## Technologies Used
- Python
- Pandas for data manipulation
- Matplotlib and Seaborn for visualization
- Plotly for interactive charts
- NumPy for numerical operations

## Setup Instructions
1. Install required Python packages:
```bash
pip install pandas numpy matplotlib seaborn plotly
```
2. Ensure all CSV data files are in the same directory as the notebook
3. Open `Fatal_Force_(start).ipynb` in Jupyter Notebook or VS Code

## Data Source
The primary data is sourced from [The Washington Post's Fatal Force database](https://www.washingtonpost.com/graphics/investigations/police-shootings-database/), which has been tracking fatal shootings by on-duty police officers since 2015. Census data is from the US Census Bureau's American Community Survey.

## Key Findings
- Explores relationships between poverty and education levels
- Analyzes demographic patterns in police shootings
- Identifies geographical patterns and trends
- Examines factors such as mental illness and armed status

## Note
- This analysis is based on reported incidents and available data. Some incidents may be unreported or missing from the database.
- This project was made for educational purposes related to data analysis only.
