import streamlit as st
import pandas as pd
import joblib
import json

with open('pipe.pkl', 'rb') as file_1:
    pipe = joblib.load(file_1)

with open('list_num_cols.txt', 'r') as file_2:
  list_num_cols = json.load(file_2)

with open('list_cat_columns.txt', 'r') as file_3:
  list_cat_cols = json.load(file_3)

def run():
    st.title ('Predict Online Shopper Intention')
    # Membuat form
    with st.form(key='form_parameters'):
        administrative = st.number_input('Administrative Pages Visited', min_value=0, max_value=30, value=0)
        adm_dur = st.number_input('Administrative Pages Duration ', min_value=0, max_value=36000, value=0)
        informational = st.number_input('Informational Pages Visited', min_value=0, max_value=30, value=0)
        info_dur = st.number_input('Informational Pages duration', min_value=0, max_value=36000, value=0)
        product = st.number_input('Product-Related Pages Visited', min_value=0, max_value=250, value=0)
        prod_dur = st.number_input('Product-Related Duration', min_value=0, max_value=36000, value=0)

        st.markdown('---')

        bounce_rate = st.number_input('Bounce Rates', min_value=0.0, max_value=0.5, value=0.2)
        exit_rate = st.number_input('Exit Rates', min_value=0.0, max_value=0.5, value=0.2)
        page_value = st.number_input('Page Values', min_value=0.0, max_value=1000.0, value=300.0)
        specialday = st.number_input('Special Day', min_value=0.0, max_value=1.0, value=0.2)

        st.markdown('---')

        os =st.selectbox('Operating Systems Used ', ['1', '2', '3', '4', '5', '6', '7', '8'], index=1)
        browser =st.selectbox('Browser Used ', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'], index=1)
        region  =st.selectbox('Region ', ['1', '2', '3', '4', '5', '6', '7', '8', '9'], index=1)
        visitor =st.selectbox('Visitor Type ', ['Returning Visitor', 'New Visitor', 'Other'], index=1)
        weekend =st.selectbox('Weekend', ['True', 'False'], index=1)
        month   =st.selectbox('Month of Visit', ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Des'] )
        st.markdown('---')

        submitted=st.form_submit_button('Predict')

    df_inf = {
        'Administrative' : administrative,
        'Administrative_Duration' : adm_dur,
        'Informational' : informational,
        'Informational_Duration' : info_dur,
        'ProdutRelated' : product,
        'ProductRelated_Duration' : prod_dur,
        'BounceRates' : bounce_rate,
        'ExitRates' : exit_rate,
        'PageValues' : page_value,
        'SpecialDay' : specialday,
        'OperatingSystems' : os,
        'Browser' : browser,
        'Region' : region,
        'VisitorType' : visitor,
        'Weekend' : weekend,
        'Month' : month}

    df_inf = pd.DataFrame([df_inf])
    st.dataframe(df_inf)

    if submitted:
        df_inf_final = df_inf[list_num_cols + list_cat_cols]

        # Predict using model
        y_pred_inf = pipe.predict(df_inf_final)

        st.write('## Revenue : ' + str((y_pred_inf)))

if __name__ =='__main__':
    run()