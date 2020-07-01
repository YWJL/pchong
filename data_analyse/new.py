import get_world_data
import re
import requests
import numpy as np
import json
import os
from collections import OrderedDict
import pandas as pd
import json
import datetime
import time
url = 'https://coronavirus.1point3acres.com/_next/static/chunks/048b3367bf0866c1bfa583e5703156bc319151cf.1e1f57467fe378e70ad6.js'
headers = {
    'User-Agent':'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
}

end_1=get_world_data.getworld_data(url,headers)

data_relative_confirmed_json=get_world_data.count_time(end_1)

get_world_data.write_json_to_csv(data_relative_confirmed_json,end_1)

