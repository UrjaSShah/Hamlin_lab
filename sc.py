from pymatgen import MPRester
m=MPRester("mhZFpeEy6dioJg19")
import numpy as np
import pandas as pd
from pandas import ExcelWriter
file = open("a_assay_Petretto.txt","r")
data=file.read()
print(data)
