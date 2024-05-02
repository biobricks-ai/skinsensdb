import pandas as pd, pathlib, numpy as np, os

# read the tsvs in cache/01_download
tsvs = list(pathlib.Path('cache/01_download').rglob('*.tsv'))

# get the most recent tsv, it seems like skinsensdb stores old versions of the workbook
# the tsvs have names like 'data-YYYYMMDD.tsv' so we can take the last one in the sorted list
df = pd.read_csv(sorted(tsvs)[-1],sep="\t")
df.replace('ND', np.nan, inplace=True)

convert_dict = {
  'Chemical_Name': str,
  'CAS No': str,
  'PubChem CID': str,
  'Canonical SMILES': str,
  'DPRA_PPRA_Cys': float,
  'DPRA_PPRA_Lys': float,
  'KeratinoSens_LuSens_EC15': str,
  'h-CLAT_EC150': str,
  'h-CLAT_EC200': str,
  'h-CLAT_CV75': str,
  'LLNA_EC3': str,
  'Human_Data': str
}

df = df.astype({k: v for k, v in convert_dict.items() if k in df.columns})

# write to brick/skinsens.parquet
os.makedirs('brick', exist_ok=True)
df.to_parquet('brick/skinsens.parquet', index=False)
