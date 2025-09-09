# Space Missions Analysis

This project analyzes global space missions from 1957 to 2025 using Python, pandas, matplotlib, seaborn, and plotly. The dataset was scraped from nextspaceflight.com and covers launches by various organizations and countries.

## Features
- **Data Cleaning & Exploration:**
  - Handles missing values and duplicates
  - Explores mission status, costs, and organizations
- **Visualizations:**
  - Launches per organization and country
  - Choropleth maps of launches and failures by country
  - Sunburst chart of country → organization → mission status
  - Spending analysis by organization and per launch
  - Launches per year and month, with rolling averages and heatmaps
  - Price trends over time
  - Top 10 organizations' launches over time
  - Cold War space race: USA vs USSR/Soviet Bloc
  - Year-by-year leadership in launches by country and organization
  - Mission failure rates and trends

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Open `Space_Missions_Analysis_(start).ipynb` in Jupyter or VS Code.
3. Run cells sequentially to explore the analysis and visualizations.

## Data Source
- [nextspaceflight.com](https://nextspaceflight.com/launches/past/?page=1)
- `mission_launches.csv` contains all missions since 1957.

## Key Insights
- The USA and USSR led the space race, with leadership changing over decades.
- Organizations like NASA, Roscosmos, and SpaceX dominate launches and spending.
- Mission failures have decreased over time, showing improved reliability.
- Launch activity varies by month and year, with clear trends and peaks.

## Visualizations
- Bar charts, line charts, pie charts, scatter plots, sunburst, choropleth maps, and heatmaps.
- Interactive charts using plotly for deeper exploration.

## License
This project is for educational purposes as part of the "100 Days of Code Python Pro Bootcamp".
