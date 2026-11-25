from __future__ import division, print_function, absolute_import
import os
import sys
import numpy as np
import pandas as pd
import argparse
from multiprocessing import Pool
from itertools import product

"""great circle distance in miles between coords"""
def Haversine(lat1, lon1, lat2, lon2): # haversine does sacrifice some accuracy for speed
  Radius = 3963  # avg earth radius in miles
  lat1_r, lon1_r = np.radians(lat1), np.radians(lon1)
  lat2_r, lon2_r = np.radians(lat2), np.radians(lon2)

  dlat = lat2_r - lat1_r
  dlon = lon2_r - lon1_r

  hav = lambda coord: np.sin(coord / 2)**2

  theta = (hav(dlat) + np.cos(lat1_r) * np.cos(lat2_r) * hav(dlon))
  return Radius * theta

"""load and merge tracts and calculate before and after distances"""
def LoadTracts(dist_path, data_path, site_lat, site_lon):
  df_dist = pd.read_csv(dist_path)
  df_data = pd.read_csv(data_path)

  overlap = [c for c in df_data.columns if c in df_dist.columns and c != "Tract_GEOID"]
  df = pd.merge(df_dist, df_data.drop(columns=overlap), on="Tract_GEOID", how="inner")

  df_before = df["Nearest_Facility_Miles"].to_numpy(dtype=float)
  df_new = Haversine(
      df["Latitude"].to_numpy(dtype=float),
      df["Longitude"].to_numpy(dtype=float),
      site_lat,
      site_lon,
  )
  df_after = np.minimum(df_before, df_new)

  hpsa_count = (
      df["PC_Geographic_HPSA"]
      + df["PC_Population_HPSA"]
      + df["PC_Facility_HPSA"]
      + df["MH_Geographic_HPSA"]
      + df["MH_Population_HPSA"]
      + df["MH_Facility_HPSA"]
  ).to_numpy(dtype=float)

  return {
      "n_tracts": len(df),
      "d_before": df_before,
      "d_after": df_after,
      "pov": df["Poverty_Rate"].to_numpy(dtype=float),
      "unins": df["Uninsured_Rate"].to_numpy(dtype=float),
      "disab": df["Disability_Rate"].to_numpy(dtype=float),
      "snap": df["SNAP_Rate"].to_numpy(dtype=float),
      "hpsa": hpsa_count,
  }

"""single monte carlo generation on all tracts before vs after"""
def GenerateTract(rng, tracts, beta):
  n = tracts["n_tracts"]

  shock = rng.lognormal(mean=0.0, sigma=0.15, size=n)
  before_tract = np.exp(-beta * tracts["d_before"]) * shock
  after_tract = np.exp(-beta * tracts["d_after"]) * shock

  tot_before = float(before_tract.sum())
  tot_after = float(after_tract.sum())
  denom = max(tot_before, 1e-12)
  demand_inc = ((tot_after - tot_before) / denom) * 100.0
  return tot_before, tot_after, demand_inc

"""run R monte carlo runs for one scenario"""
def Simulation(tracts, beta, R, seed):
  rng = np.random.default_rng(seed)
  records = [GenerateTract(rng, tracts, beta) for _ in range(R)]
  return pd.DataFrame(records, columns=["before", "after", "demand_inc"])

"""compute summary stats and quantiles for specific column"""
def SummarizeCol(df_sim, col, beta):
  s = df_sim[col]
  q90_cut = s.quantile(q=0.90)
  q95_cut = s.quantile(q=0.95)

  q90_val = float(s[s <= q90_cut].max()) if (s <= q90_cut).any() else float(q90_cut)
  q95_val = float(s[s <= q95_cut].max()) if (s <= q95_cut).any() else float(q95_cut)

  return {
      "beta": beta,
      "mean": float(s.mean()),
      "q90": q90_val,
      "q95": q95_val,
      "ci25": float(s.quantile(q=0.025)),
      "ci975": float(s.quantile(q=0.975)),
  }


def ManageProcess(task):
  beta = task["beta"]
  R = task["R"]
  seed = task["seed"]
  tracts = task["tracts"]

  sim_df = Simulation(tracts, beta, R, seed)

  return {
      "before": SummarizeCol(sim_df, "before", beta),
      "after": SummarizeCol(sim_df, "after", beta),
      "demand_inc": SummarizeCol(sim_df, "demand_inc", beta),
  }