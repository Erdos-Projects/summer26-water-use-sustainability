# summer26-water-use-sustainability
Team project: summer26-water-use-sustainability

## Problem Definition

We will model the amount of water in a specific reservoir as a function of various factors such as temperature, snowpack, precipitation, cloud cover, evaporation rate, population dependent on the reservoir for water, number of farms in the vicinity, number of data centers, etc. 

Note: it could also be interesting to model several reservoirs with a lot of data centers nearby to see if there are similarities in how they all behave wrt data centers.

## Stakeholders

The stakeholders would be local government, water utility operators, farmers, data center and tech stakeholders, and the populace that depends on the reservoir for data.

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

We have not gathered data yet. We can probably find water volume data at the [US Bureau of Reclamation website](https://data.usbr.gov/).
