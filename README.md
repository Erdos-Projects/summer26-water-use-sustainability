# summer26-water-use-sustainability
Team project: summer26-water-use-sustainability

## Problem Definition

We will model the amount of water in the Salt and Verde River Reservoir System as a function of various factors such as temperature, snowpack, precipitation, cloud cover, evaporation rate, population dependent on the reservoir for water, number of farms in the vicinity, number of data centers, etc. This system consists of a group of reservoirs on the Salt River and the Verde River, near Phoenix, AZ. It is a major source of drinking water for Phoenix, as well as irrigation water for farms in Maricopa County, AZ. Like many other areas of the Southwest, it has been affected by droughts in recent years, and these droughts are expected to worsen under climate change. At the same time, several data centers were recently built or are scheduled to be built in Phoenix, which could further put a strain on the city's water supply. 


## Stakeholders

The stakeholders would be local government, water utility operators, farmers, data center and tech stakeholders, and the populace that depends on these reservoirs for water.

## KPIs

Our primary KPI is RMSE, which we would like to minimize. 

I'm not really sure what to put for secondary KPIs. Chat GPT suggests $R^2$ variance (maximize), critical threshold recall (maximize), and inference latency (minimize). Here is a summary table that Chat GPT made:

| KPI Type | Specific Metric | Formula | Improvement Direction | Stakeholder Value |
| :--- | :--- | :--- | :--- | :--- |
| **Primary** | Root Mean Squared Error (RMSE) | $\sqrt{\frac{1}{n}\sum(y - \hat{y})^2}$ | ⬇️ **Minimize** | Penalizes large, dangerous prediction misses. |
| **Secondary (Hydrology)** | $R^2$ Variance Explained | $1 - \frac{SS_{res}}{SS_{tot}}$ | ⬆️ **Maximize** | Proves data center/farm data adds predictive value over a naive mean guess. |
| **Secondary (Safety)** | Critical Threshold Recall | $\frac{\text{True Shortages Captured}}{\text{Total Actual Shortages}}$ | ⬆️ **Maximize** | Guarantees the model successfully flags upcoming droughts before they happen. |
| **Technical** | Inference Latency | Time ($t_{\text{end}} - t_{\text{start}}$) | ⬇️ **Minimize** | Ensures the script runs fast enough for live software dashboards. |

## Data Gathering
Each of the two rivers have water gages which measure water flow rate. For each river, we will look at the flow rate from a gage that is upstream of the reservoirs, and another that is downstream. The upstream gage is a measure of water input to the reservoirs from snowpack, rainfall etc. The downstream gage measures how much water is released from the reservoirs, which should be roughly correlated with the demand for water (Note: not all water released from the reservoirs is consumed by humans, some of it is just released to keep the river flowing and protect natural habitats etc. So this is not a perfect measure for water demand, but it should be good enough). Thus we will use data from four river gages in total (one upstream + one downstream for each river). 

Note that data on reservoir water levels is not available, hence we are using flow rates instead. Upstream minus downsteam flow rate gives an estimate of the rate of change of water storage in the reservoir system, but the absolute water storage cannot be calculated from this data.

**Water gage data**

From USGS water data
- Salt River upstream gage
  - Name: Salt River Near Roosevelt, AZ
  - Gage number: USGS-09498500
  - Link: https://waterdata.usgs.gov/monitoring-location/USGS-09498500
- Salt River downstream gage
  - Name: Salt River Blw Stewart Mountain Dam, AZ
  - Gage number: USGS-09502000
  - Link: https://waterdata.usgs.gov/monitoring-location/USGS-09502000
- Verde River upstream gage
  - Name: Verde Rvr Blw Tangle Creek, Abv Horseshoe Dam, AZ
  - Gage number:  USGS-09508500
  - Link: https://waterdata.usgs.gov/monitoring-location/USGS-09508500
- Verde River downstream gage
  - Name: Verde River Below Bartlett Dam, AZ
  - Gage number: USGS-09510000
  - Link: https://waterdata.usgs.gov/monitoring-location/USGS-09510000

**Feature data**
- Climate
  - Climate for Phoenix: Daily data for January 1, 1985 to January 1, 2025 for the coordinates 33.43, -112 (a somewhat arbitrary location in the middle of Phoenix, AZ) is in [PRISM_climate_data_33.4300_-112.0000.csv](Data/RawData/PRISM_climate_data_33.4300_-112.0000.csv). The data is precipitation (in) and mean temperature (degrees F).
  - Climate for Maricopa County - NOAA Monthly U.S. Climate Gridded Dataset (NClimGrid; https://www.ncei.noaa.gov/data/nclimgrid-monthly/access/), monthly data from Jan 1, 1895 - May 1, 2026. Downloaded data for the entire US (nclimgrid_prcp.nc and	nclimgrid_tavg.nc), then clipped to county boundaries, and then averaged temperature and summed precipitation for each watershed. Temperature in degree Celcius and precipitation in mm.
  - Climate for river watersheds - NOAA Monthly U.S. Climate Gridded Dataset (NClimGrid; https://www.ncei.noaa.gov/data/nclimgrid-monthly/access/), monthly data from Jan 1, 1895 - May 1, 2026. Downloaded data for the entire US (nclimgrid_prcp.nc and	nclimgrid_tavg.nc), then clipped to each watershed's boundaries, and then averaged temperature and summed precipitation for each watershed. Temperature in degree Celcius and precipitation in mm.
- Human population - Federal Reserve Bank of St. Louis (https://fred.stlouisfed.org/series/PHXPOP)
  - Havi: I could only find population data starting in 2000. The data is given yearly, units are thousands of people.
- Farmland area/irrigated acres - need to finalize source
- Data centers (number, year operational, MW capacity - known to be correlated with water use) - https://cleanview.co/data-centers/us
  - Havi: I got Gemini to generate a CSV file with data center information. I checked a few entries for correctness but we should make sure all of the information is correct! This is in [phoenix_datacenters_chronological.csv](Data/RawData/phoenix_datacenters_chronological.csv).

**Other data**
- Watershed boundaries - USGS StreamStats Basin Delineation tool (https://streamstats.usgs.gov/ss/)
- Map of Arizona counties (used to get the boundaries of Maricopa county for climate data preprocessing) - Arizona Department of Health Services GIS Portal (https://geodata-adhsgis.hub.arcgis.com/datasets/ADHSGIS::county-boundaries-in-arizona)
