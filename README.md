# summer26-water-use-sustainability
Team project: summer26-water-use-sustainability

## Problem Definition

We will model the amount of water in the Salt River Project reservoirs as a function of various factors such as temperature, snowpack, precipitation, cloud cover, evaporation rate, population dependent on the reservoir for water, number of farms in the vicinity, number of data centers, etc. The Salt River Project consists of a group of reservoirs on the Salt River and the Verde River, near Phoenix, AZ. It is a major source of drinking water for Phoenix, as well as irrigation water for farms in Maricopa County, AZ. Like many other areas of the Southwest, it has been affected by droughts in recent years, and these droughts are expected to worsen under climate change. At the same time, several data centers were recently built or are scheduled to be built in Phoenix, which could further put a strain on the city's water supply. 


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
Each of the two rivers have water gages which measure water flow rate. For each river, we will look at the flow rate from a gage that is upstream of the reservoirs, and another that is downstream. The upstream gage is a measure of water input to the reservoirs from rainfall etc. The downstream gage measures how much water is released from the reservoirs, which should be roughly correlated with the demand for water (not all water released from the reservoirs is consumed by humans, some of it is just released to keep the river flowing and protect natural habitats etc. So this is not a perfect measure for water demand, but it should be good enough). Thus we will use data from four river gages in total. 

Water gage Data: from USGS water data
Feature data:
Climate - need to finalize source 
Human population - US Census Bureau? 
Farmland area/irrigated acres - need to finalize source
Data centers (number, year operational, MW capacity - known to be correlated with water use) - https://cleanview.co/data-centers/us
