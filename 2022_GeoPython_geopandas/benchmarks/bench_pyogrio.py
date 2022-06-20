"""
Run with gdal master and pyogrio master


import pandas as pd
import seaborn as sns
sns.set_context("talk")

df1 = pd.read_csv("bench_results.csv", names=["format", "time"])
df1["Case"] = "full file"
df2 = pd.read_csv("bench_results_single_column.csv", names=["format", "time"])
df2["Case"] = "single column"

df = pd.concat([df1, df2])

fig = sns.catplot(data=df, x="format", y="time", kind="bar", hue="Case")
fig.set(ylabel="Time (s)", xlabel="File format")
fig.fig.savefig("../img/bench_geoparquet.png")

sizes = []
for fns in [["nz-buildings-outlines.gpkg"], ["nz-buildings-outlines.fgb"], ["nz-buildings-outlines.shp", "nz-buildings-outlines.dbf"], ["nz-buildings-outlines.parquet"]]:
    fsize = 0
    for fn in fns:
        fsize += os.stat(str(DATA_DIR / fn)).st_size
    sizes.append(fsize)

df = pd.DataFrame({'format': ["gpkg", "fgb", "shp", "parquet"], "size": np.array(sizes) / 1024**2})
fig = sns.catplot(data=df, x="format", y="size", kind="bar", color="C0")
fig.set(ylabel="File size (MB)", xlabel="File format")
fig.fig.savefig("../img/bench_geoparquet_file_size.png")

"""
import pathlib
import sys
import time

import pandas as pd
import geopandas


DATA_DIR = (pathlib.Path("..") / ".." / ".." / "gdal_geoparquet_bechmarks").resolve()
print(DATA_DIR)

cases = {
    "gpkg": "nz-buildings-outlines.gpkg",
    "fgb": "nz-buildings-outlines.fgb",
    "shp": "nz-buildings-outlines.shp",
}


if __name__ == '__main__':
    frmt, engine = sys.argv[1:]
    filename = cases[frmt]
    
    t0 = time.time()
    _ = geopandas.read_file(DATA_DIR / filename, engine=engine)
    time_read = time.time() - t0
    print(frmt, ": ", time_read)

    # with open("bench_results.csv", "a") as f:
    #     f.write(f"{engine},{frmt},{time_read}\n")
