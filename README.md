# summer26-water-use-sustainability
How will Phoenix's water supply be affected by climate change and upcoming data centers?

## Problem Definition

Many areas of the Southwest US are expected to face water shortages under climate change. At the same time, data centers are being built across this region, which could further put a strain on water availability. Using the city of Phoenix, AZ and the surrounding county (Maricopa county) as an example, we aim to forecast municipal water demand and supply in the near future. Phoenix receives most its municipal water from the Salt River Project, which manages a system of reservoirs on the Salt river and Verde river. We will model inflow into and outflow from these reservoirs as a function of various factors such as temperature, precipitation, population dependent on the reservoir for water, number of farms in the vicinity, number of data centers, etc. 


## Stakeholders

The stakeholders would be local government, water utility operators, farmers, data center and tech stakeholders, and the populace that depends on these reservoirs for water.

## KPIs

Our primary KPI is RMSE of river flow rate predictions, which we would like to minimize. 

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
  - Current and historical climate for Maricopa County - NOAA Monthly U.S. Climate Gridded Dataset (NClimGrid; https://www.ncei.noaa.gov/data/nclimgrid-monthly/access/), monthly data from Jan 1, 1895 - May 1, 2026. Downloaded data for the entire US (nclimgrid_prcp.nc and	nclimgrid_tavg.nc), then clipped to county boundaries, and then averaged temperature and summed precipitation for each watershed. Temperature in degree Celcius and precipitation in mm.
  - Current and historical climate for river watersheds - NOAA Monthly U.S. Climate Gridded Dataset (NClimGrid; https://www.ncei.noaa.gov/data/nclimgrid-monthly/access/), monthly data from Jan 1, 1895 - May 1, 2026. Downloaded data for the entire US (nclimgrid_prcp.nc and	nclimgrid_tavg.nc), then clipped to each watershed's boundaries, and then averaged temperature and summed precipitation for each watershed. Temperature in degree Celcius and precipitation in mm.
  - Future climate projections - LOCA2 downscaled CMIP6 climate projections based on the ACCESS-CM2 climate model (https://loca.ucsd.edu/). Downloaded monthly data for entire North America, from 2015 - 2044, then summarized over areas of interest (watershed and county boundaries). Temperature in Kelvin and precipitation in kg/m2/s, which we converted to degree Celcius and mm, respectively. 
    
- Human population in Maricopa County, AZ
  - 1920-1970 (decadal data):  National Historical Geographic Information System (https://www.nhgis.org/)
  - 1970-2014 (annual data): National Bureau of Economic Research - U.S. Intercensal County Population Data, 1970-2014 (https://www.nber.org/research/data/census-us-intercensal-county-population-data-1970-2014)
  - 2015-2019 (annual data): US Census Bureau County - Intercensal Population Totals: 2010-2020 (https://www.census.gov/data/datasets/time-series/demo/popest/intercensal-2010-2020-counties)
  - 2020-2025 (annual data): US Census Bureau - Annual Estimates of the Resident Population for Counties: April 1, 2020 to July 1, 2025 (CO-EST2025-POP) (https://www.census.gov/data/datasets/time-series/demo/popest/2020s-counties-total.html)
  - Future population projections - Arizona Office of Economic Statistics County Population Projections 2025 - 2060 (https://oeo.az.gov/population/projections)

- Farmland area/irrigated acres in Maricopa County, AZ
  - USDA Census of Agriculture, 1935-2022; conducted every 5 years. Accessed PDF reports for each census on the USDA National Agriculture Statistics Service (https://www.nass.usda.gov/AgCensus/) and manually wrote down values for total farmland area (acres) and irrigated farmland area (acres).  
    
- Data centers (number, year operational, MW capacity - known to be correlated with water use) - including currently operational and upcoming data centers https://cleanview.co/data-centers/us
  
**Other data**
- Watershed boundaries (used for climate data preprocessing) - USGS StreamStats Basin Delineation tool (https://streamstats.usgs.gov/ss/)
- Map of Arizona counties (used to get the boundaries of Maricopa county for climate data preprocessing) - Arizona Department of Health Services GIS Portal (https://geodata-adhsgis.hub.arcgis.com/datasets/ADHSGIS::county-boundaries-in-arizona)
