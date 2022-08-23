"""
Run with gdal master and pyogrio master


import pandas as pd
import seaborn as sns
sns.set_context("talk")

df = pd.read_csv("bench_results.csv", names=["engine", "format", "time"])

df = df.replace({
    "fiona": "geopandas+fiona", "pyogrio": "geopandas+pyogrio",
    "pyogrio-arrow": "geopandas+pyogrio+arrow",
    "gpkg": "nz-buildings-outlines.gpkg"
})


fig = sns.catplot(data=df, x="format", y="time", kind="bar", hue="engine", hue_order=["geopandas+fiona", "geopandas+pyogrio", "geopandas+pyogrio+arrow"])
fig.set(ylabel="Time (s)", xlabel="")
fig.fig.savefig("../img/bench_pyogrio_read2.png")

fig.fig.savefig("../img/bench_pyogrio_read.png")


# run with `fil run bench_pyogrio.py`
memory = np.array([10056500624, 6390508959]) / 1000**2
df = pd.DataFrame({'format': ["nz-buildings-outlines.gpkg"]*2, 'engine': ["geopandas+fiona", "geopandas+pyogrio"], "memory": memory})
fig = sns.catplot(data=df, x="format", y="memory", kind="bar", hue="engine")
fig.set(ylabel="Peak Memory Usage (MB)", xlabel="")
fig.fig.savefig("../img/bench_pyogrio_memory.png")

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

    with open("bench_results.csv", "a") as f:
        f.write(f"{engine},{frmt},{time_read}\n")
