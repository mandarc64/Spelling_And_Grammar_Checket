# from gingerit.gingerit import GingerIt
import streamlit as st
import sys
import os

st.title('Spelling & Grammar Checker')
text = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)

#Added path to sys.path
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(MODULE_DIR))

#relative import 
from local.gingerit import GingerIt 

#from gingerit.gingerit import GingerIt
parser = GingerIt()
if st.button('Correct Sentence'):
    if text == '':
        st.write('Please enter text for checking') 
    else: 
        result_dict = parser.parse(text)
        st.markdown('Corrected Sentence: ' + str(result_dict["result"]))
else: pass