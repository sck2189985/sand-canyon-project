# Scratch Final Project Repo
## By: Shelby, Taylor, Kirk, and Seun

This repository contains American Community Survey (ACS) Public Use Microdata Sample (PUMS) housing and person records, notebooks for cleaning and analyzing these records, aggregate reference data, and supporting ACS documentation.

## For Project Checkpoint 2 Grading Purposes

Please refer to the `PUMS Data FINAL` and `Agg Data FINAL` folders for our cleaned datasets. Our basic statistical analysis for Checkpoint 2 is in the `PUMS stats files` folder

## Repository Folders

 * `About PUMS data`
    * A collection of pdfs explaining PUMS data, PUMA names, data dictionary, and variable documentation
 * `Agg Data FINAL`
    * Aggregate reference workbooks: DP02 (social), DP03 (economic), DP05 (demographic and housing), and HRSA mental-health and primary care data. Different than PUMS data.
 * `PUMS Data FINAL`
    * Final filtered housing and person CSVs used in analysis (PUMA 0100)
 * `PUMS intermediate data files`
    * CSVs written during preparation: cleaned housing and person files, plus filtered versions of both
 * `PUMS raw data files`
    * Housing file: household/housing records
    * Person file: person-level records
 * `PUMS stats files`
    * Summary statistics, weighted person-variable distributins, successive-difference replication (SDR) tables for selected variables (for uncertainty estimates), and missingness summary from notebook

## Repository Files

 * `PUMS_data_cleaning_code-Jup.ipynb`
    * Notebook that reads the raw CSVs, writes intermediate copies, filters records, and generates final CSVs and statistics, including measures of uncertainty
 * `PUMS_housing_data_stats.ipynb`
    * Notebook that loads final housing data and analyzes structure, descriptive statistics, missingness, and housing weights

## Geography

The cleaning notebook selects PUMA code `0100`. It includes northwest and north-central Nebraska. The code reads PUMA numerically, so `0100` appears as `100` in the filtered CSVs

## Data Workflow

1. Start with the two CSVs in `PUMS raw data files`
2. Run `PUMS_data_cleaning_code-Jup.ipynb` from the repository root. It writes intermediate files, filters housing and person records, and saves the final data and statistics in their respective folders
3. Use the CSVs in `PUMS Data FINAL` for later analysis. `PUMS_housing_data_stats.ipynb` demonstrates analysis of the final housing datasets
4. Consult `About PUMS data` when interpreting variable codes, special values, weights, or geographic definitions

The notebooks use paths relative to the repository root. Run them with the repository root as the working directory so that their input and output paths resolve

## Dependencies

The notebooks import Python packages including `pandas`, `numpy`, and `dateutil`, and require Jupyter Notebook support. No dependency list is included in the repository, so install those packages in the Python environment used to run the notebooks