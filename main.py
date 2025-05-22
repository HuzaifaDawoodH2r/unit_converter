import streamlit as st 

st.markdown("""
    <style>
    .title {
        color: #4CAF50;
        font-size: 50px;
        font-weight: bold;
        text-align: center;}
    .heading {
            color: #2E86C1;
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;}
            </style>
""",unsafe_allow_html=True)

def convert_unit(value, unit_from, unit_to):
    conversion = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000
    }

    key = f"{unit_from}_{unit_to}"
    if key in conversion:
        conversion = conversion[key]
        return value * conversion
    else:
        return 'Conversion not found'

st.markdown(f'<div class = title>convert_machine</div>', unsafe_allow_html=True)
st.title(f'unit_converter')

value = st.number_input('Enter your value')
unit_from = st.selectbox('Convert from:', ['meters', 'kilometers', 'grams', 'kilograms'])
unit_to = st.selectbox('Convert to:', ['meters', 'kilometers', 'grams', 'kilograms'])

if st.button('Convert'):
    result = convert_unit(value, unit_from, unit_to)
    st.write(f'Converted value: {result}')
