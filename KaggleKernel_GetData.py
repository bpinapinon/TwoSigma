import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
print(os.listdir("../input"))

from kaggle.competitions import twosigmanews
env = twosigmanews.make_env()

(market_train_df, news_train_df) = env.get_training_data()

market_train_df.count()
market_train_df.to_csv("market_train.csv")
# news_train_df.to_csv("news_train.csv")