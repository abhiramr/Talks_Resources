import seaborn as sns
import Morpheus
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import logging

logger = logging.getLogger('Aphrodite')
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger.setLevel(logging.INFO)

sleep_id = '1EjOt3vPyDVsMzkCAfFxdqVGpRrRXdCbHBIsttpBcxGWHzDpIu1UHCbsbuAm1mg'

sleep_df = Morpheus.everything(sleep_id)
df = pd.pivot_table(data=sleep_df, index='day', values='sleep_duration', columns='month')
df = df.reindex(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][::-1])
df = df[["Jun", "Jul", "Aug", "Sep", "Oct"]]
f, ax = plt.subplots(figsize=(12, 10))
ax = sns.heatmap(df, annot=True, fmt="0.1f", linewidths=.5, cmap='Purples_r', ax=ax, robust=True)

figure = ax.get_figure()
time_now = str(datetime.now().strftime("%d_%b_%y_%H_%M_%S"))
figure.savefig("outputs/"+time_now+".png", dpi=400)
logger.info("Output saved at : {}".format("outputs/"+time_now+".png"))
