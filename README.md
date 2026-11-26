
# Scratch Final Project Repo

## By: Shelby, Taylor, Kirk, and Seun

## Project Overview

This project examines the role of Sand Canyon Health Center in geographic healthcare accessibility across rural western Nebraska. Our goal is to evaluate how healthcare facilities are distributed relative to population and community-level socioeconomic needs, and to explore how the availability of individual facilities may affect geographic access.

The analysis combines American Community Survey (ACS) data, healthcare facility information, Census geographic data, and population estimates. We are developing a spatial analysis framework to compare healthcare accessibility across communities and evaluate potential changes in access under alternative facility-availability scenarios.

## Research Question

To what extent does Sand Canyon Health Center contribute to geographic healthcare accessibility in rural western Nebraska, particularly for communities with greater socioeconomic and healthcare needs?

## For Project Checkpoint 3 Grading Purposes

Please refer to the [`Agg Data FINAL`](Agg%20Data%20FINAL/) folder, which contains [`Panhandle_Final_Project_Data.csv`](Agg%20Data%20FINAL/Panhandle_Final_Project_Data.csv).

The following notebooks and script contain the main analytical work:

- [`ACS_data_cleaning_code.ipynb`](ACS_data_cleaning_code.ipynb): ACS data preparation and Community Need Index construction.
- [`Distance_calc_code.ipynb`](Distance_calc_code.ipynb): Geographic accessibility analysis, facility distance calculations, census block analysis, and population-weighted accessibility measures.
- [`SandCanyonMC.py`](SandCanyonMC.py): Preliminary Monte Carlo simulation framework.

Additional descriptive statistics and statistical uncertainty estimates are available in the `PUMS stats files` folder.

## Geography

The project focuses on the following 11 counties in the Nebraska Panhandle:

- Banner
- Box Butte
- Cheyenne
- Dawes
- Deuel
- Garden
- Kimball
- Morrill
- Scotts Bluff
- Sheridan
- Sioux

The current aggregate dataset covers 27 census tracts, and the combined healthcare facility inventory contains 17 facility locations, including Sand Canyon Health Center.

The PUMS cleaning notebook selects PUMA code `0100`, which includes northwest and north-central Nebraska. The code reads PUMA numerically, so `0100` appears as `100` in the filtered CSVs.

The PUMA geography extends beyond the 11 study counties. Therefore, PUMS records cannot be directly assigned to individual census tracts within the study area.

The preliminary census block analysis incorporates Census TIGER/Line tract and block geography to examine healthcare accessibility at a more detailed geographic level.

## Data Sources

The repository contains publicly available data from the following sources:

| Data Source | Description |
| --- | --- |
| American Community Survey (ACS) | Demographic, socioeconomic, disability, poverty, and health insurance indicators |
| ACS Public Use Microdata Sample (PUMS) | Person-level and housing-level records |
| Health Resources and Services Administration (HRSA) | Primary care and mental health HPSA designations and health center site information |
| Nebraska Department of Health and Human Services (DHHS) | Rural health clinic information |
| Census Gazetteer Files | County and census tract reference coordinates |
| Census TIGER/Line Files | Census tract and block geography and population attributes |
| Area Deprivation Index (ADI) | Neighborhood socioeconomic disadvantage indicators |
| CDC PLACES | Local population health indicators |
| CDC Social Vulnerability Index (SVI) | Community-level social vulnerability indicators |
| County Health Rankings | County-level health and socioeconomic indicators |
| USDA Food Access Research Atlas (FARA) | Food accessibility and related socioeconomic indicators |

The ACS aggregate data are primarily based on the 2020–2024 five-year estimates.

The ADI, CDC PLACES, SVI, County Health Rankings, and FARA datasets are supplementary resources collected during the project. Not all of these sources have been incorporated into the current integrated analytical dataset.

## Repository Folders

- `ACS Raw Data`
  - Raw ACS aggregate data, NHGIS extracts, and supporting documentation.

- `ADI Raw Data`
  - Area Deprivation Index data and supporting documentation.

- `About PUMS data`
  - A collection of PDFs explaining PUMS data, PUMA names, data dictionaries, and variable documentation.

- `Agg Data FINAL`
  - Cleaned aggregate ACS and HRSA reference workbooks.
  - Community Need Index datasets.
  - Healthcare facility datasets.
  - County and census tract geographic coordinates.
  - Geographic accessibility and distance calculations.
  - Integrated project dataset.

- `CDC Places Raw Data`
  - CDC PLACES population health data and supporting documentation.

- `CDC SVI Raw Data`
  - Social Vulnerability Index data and supporting documentation.

- `County Health Rankings Raw Data`
  - County-level health rankings, socioeconomic indicators, and reference materials.

- `FARA Raw Data`
  - Food Access Research Atlas and SNAP-authorized retailer access datasets, including supporting documentation.

- `PUMS Data FINAL`
  - Final filtered housing and person CSVs used in analysis for PUMA `0100`.

- `PUMS intermediate data files`
  - CSVs written during preparation, including cleaned housing and person files and filtered versions of both.

- `PUMS raw data files`
  - Raw housing and person-level records.
  - DHHS rural health clinic data.
  - HRSA health center site data.
  - Census Gazetteer files.

- `PUMS stats files`
  - Summary statistics, weighted person-variable distributions, successive-difference replication (SDR) tables for uncertainty estimates, and missingness summaries.

- `tl_2025_31_tract (1)`
  - Nebraska census tract TIGER/Line shapefile and supporting geographic files.

- `tl_2026_31_tabblock20`
  - Nebraska census block TIGER/Line geographic files and 2020 Census population attributes used in the more detailed accessibility analysis.

## Repository Files

- `ACS_data_cleaning_code.ipynb`
  - Cleans and prepares ACS aggregate data, extracts selected socioeconomic and healthcare need indicators, and constructs the Community Need Index.

- `ADI_data_cleaning.ipynb`
  - Contains preliminary documentation and preparation notes for the Area Deprivation Index data.

- `Comb_DHHS_and_UDS.ipynb`
  - Combines DHHS rural health clinic records and HRSA health center site records and incorporates Sand Canyon Health Center into the facility inventory.

- `DHHS_data_cleaning_code.ipynb`
  - Filters rural health clinic records to the 11 Nebraska Panhandle counties and prepares relevant facility information.

- `Distance_calc_code.ipynb`
  - Calculates straight-line distances between census tract reference locations and healthcare facilities.
  - Compares nearest-facility distances with and without Sand Canyon Health Center.
  - Combines geographic accessibility measures with community need and HPSA indicators.
  - Incorporates Census TIGER/Line geographic data for spatial visualization.
  - Contains preliminary census block-level distance calculations and population-weighted accessibility analysis.

- `FARA_data_cleaning.ipynb`
  - Contains preliminary documentation and preparation notes for food accessibility data.

- `GAZETTE_data_cleaning_code.ipynb`
  - Prepares county and census tract geographic reference coordinates for the accessibility analysis.

- `PUMS_data_cleaning_code-Jup.ipynb`
  - Reads raw PUMS CSVs, writes intermediate copies, filters records, and generates final CSVs and statistics, including measures of uncertainty.

- `PUMS_housing_data_stats.ipynb`
  - Loads final housing data and examines data structure, descriptive statistics, missingness, and housing weights.

- `SVI_data_cleaning.ipynb`
  - Contains preliminary documentation and preparation notes for the Social Vulnerability Index data.

- `SandCanyonMC.py`
  - Contains the developing Monte Carlo simulation framework for examining potential changes in modeled accessibility under alternative facility-availability scenarios.

- `UDS_data_cleaning_code.ipynb`
  - Filters HRSA health center service delivery and look-alike site records to the study area.

## Main Analysis Files

The following datasets are located in the `Agg Data FINAL` folder:

| File | Description |
| --- | --- |
| `Panhandle_ACS_Community_Need.csv` | Selected ACS community need indicators for the study tracts |
| `Panhandle_Community_Need_Index.csv` | Community need indicators, standardized scores, and composite index |
| `Panhandle_Rural_Health_Clinics.xlsx` | Filtered rural health clinic records |
| `Panhandle_FQHCs.xlsx` | Filtered HRSA health center site records |
| `Panhandle_All_Facilities.csv` | Combined healthcare facility inventory |
| `Panhandle_All_Facilities.xlsx` | Excel version of the combined facility inventory |
| `Panhandle_County_Locations.csv` | County geographic reference coordinates |
| `Panhandle_Census_Tracts.csv` | Census tract geographic reference coordinates |
| `Panhandle_Tract_Facility_Distances.csv` | Nearest-facility distances with and without Sand Canyon |
| `Panhandle_Need_and_Access.csv` | Combined community need and geographic accessibility measures |
| `Panhandle_Final_Project_Data.csv` | Integrated tract-level dataset containing community need, geographic accessibility, and HPSA indicators |

The folder also contains the cleaned DP02, DP03, DP05, primary care HPSA, and mental health HPSA reference workbooks.

The current integrated project dataset contains 27 observations and 23 variables.

## Analytical Methodology

### Community Need Index

The Community Need Index is constructed using five ACS indicators:

- Poverty rate
- Uninsured rate
- Percentage of the population aged 65 years and older
- Disability rate
- SNAP participation rate

Each indicator is standardized using a z-score. The standardized indicators are then averaged using equal weights to construct the composite Community Need Index.

Higher index values indicate greater relative socioeconomic and healthcare-related need among the study tracts. The index is a relative measure of community need rather than a direct measure of observed healthcare demand.

### Geographic Accessibility Analysis

The geographic accessibility analysis uses the Haversine formula to calculate straight-line distances between geographic reference locations and healthcare facilities.

The tract-level analysis compares two scenarios:

1. Nearest healthcare facility with Sand Canyon Health Center included.
2. Nearest healthcare facility with Sand Canyon Health Center excluded.

The difference between these scenarios is used to examine whether the availability of Sand Canyon changes the distance to the nearest healthcare facility.

### Preliminary Census Block and Population-Weighted Analysis

To improve geographic detail beyond the tract-level analysis, the distance notebook also incorporates Census TIGER/Line tract and block data.

The census block analysis uses block reference coordinates and the `POP20` population attribute to examine geographic accessibility at a more detailed level.

Population-weighted accessibility measures account for differences in the number of residents across census blocks rather than treating every geographic location equally.

The `POP20` variable represents population counts from the 2020 Census, rather than a current-year population estimate.

The block-level calculations are currently contained within the distance notebook. Their integration into the final project dataset is ongoing.

### Health Professional Shortage Areas (HPSA)

Primary care and mental health HPSA data are used to provide additional information about healthcare shortages within the study area.

County-level HPSA indicators are merged into the tract-level dataset to supplement the Community Need Index and geographic accessibility measures.

These indicators represent designations identified under the current filtering rules and should not be interpreted as independently verified tract-level shortage designations.

### PUMS Statistical Analysis

The PUMS analysis includes data cleaning, filtering, descriptive statistics, weighted distributions, and missingness assessments.

Person and housing survey weights are used where appropriate to account for the survey sampling structure.

Successive-difference replication (SDR) is also used to estimate statistical uncertainty for selected person-level variables.

### Monte Carlo Simulation

The Monte Carlo script contains functions for loading tract data, applying distance-decay relationships and random shocks, repeating simulations, and summarizing simulation results.

The simulation framework is being developed to examine potential changes in modeled healthcare accessibility under alternative facility-availability scenarios.

Integration with the current geographic distance data, population information, and Community Need Index is ongoing.

## Data Workflow

### Aggregate and Geographic Data

1. Use `ACS_data_cleaning_code.ipynb` to prepare ACS community need indicators and construct the Community Need Index.

2. Use `DHHS_data_cleaning_code.ipynb` and `UDS_data_cleaning_code.ipynb` to prepare the healthcare facility datasets.

3. Use `Comb_DHHS_and_UDS.ipynb` to combine facility records and incorporate Sand Canyon Health Center.

4. Use `GAZETTE_data_cleaning_code.ipynb` to prepare county and census tract geographic reference coordinates.

5. Use `Distance_calc_code.ipynb` to calculate geographic accessibility measures and combine distance calculations with community need and HPSA indicators.

6. Use the Census TIGER/Line files within the distance notebook to examine census block-level accessibility and population-weighted measures.

7. Refer to `SandCanyonMC.py` for the developing Monte Carlo simulation framework.

The cleaned datasets and intermediate analytical outputs are available in the `Agg Data FINAL` folder.

The Monte Carlo script and the newer block-level analysis are still being refined and integrated with the existing analytical datasets.

### PUMS Data

1. Start with the person and housing CSVs in `PUMS raw data files`.

2. Run `PUMS_data_cleaning_code-Jup.ipynb` from the repository root. It writes intermediate files, filters housing and person records, and saves the final data and statistics in their respective folders.

3. Use the CSVs in `PUMS Data FINAL` for further analysis.

4. Use `PUMS_housing_data_stats.ipynb` to examine the final housing dataset.

5. Consult `About PUMS data` when interpreting variable codes, special values, survey weights, or geographic definitions.

The notebooks should generally be run with the repository root as the working directory so that input and output paths resolve correctly.

Some file paths may require adjustment depending on the operating system and local directory structure. The CSV and Excel versions of the facility inventory should also remain consistent when facility information is updated.

## Dependencies

The project uses Python and a Jupyter-compatible environment.

Python packages used by the notebooks and scripts include:

- `pandas`
- `numpy`
- `python-dateutil`
- `matplotlib`
- `pyshp` (imported as `shapefile`)
- `IPython`

Excel file operations also require an appropriate Excel engine, such as `openpyxl`.

No separate dependency or environment file is currently included in the repository. Required packages should be installed in the Python environment used to run the notebooks.

The components of each TIGER/Line shapefile should remain together in their original folders.

## Current Project Status

The repository currently contains:

- Cleaned aggregate and PUMS datasets.
- Weighted descriptive statistics and uncertainty estimates.
- Community Need Index calculations.
- A combined healthcare facility inventory.
- Tract-level geographic accessibility calculations.
- Integrated community need, accessibility, and HPSA data.
- Preliminary census block-level and population-weighted accessibility analysis.
- A developing Monte Carlo simulation framework.

Further integration, validation, and interpretation of the analytical results are ongoing.
