import streamlit as st
import time
import numpy as np
import pandas as pd

#main code 
st.title("My First app")
st.write("Her is our first attempt at using data to create a table!!: ")
st.write(pd.DataFrame(
    {
        'first column':[1,2,3,4],
        'second column':[10,20,30,40]
    }
))