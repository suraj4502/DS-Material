import streamlit as st



# methods for showing data
# st.title("Streamlit app")

# st.header("hdsk")
# st.subheader("thisis a subheading")

# st.write("this is a statement")

# st.markdown("tis is a mrkown code")

# st.metric("metric tilte",value=500,delta=+1)

# # inputs

# inp = st.text_input("Enter something")

# radio_inp = st.radio("this is a radiobutton",options=['1','2','3'])

# if radio_inp == '2':
#     st.title("2 was clicked")
    
# check = st.checkbox("this is a checkbox:")

# if check:
#     st.write("checked")
    


# st.selectbox('selectbox',['a','b'])

# st.slider('slider',0, 100)


# a = st.number_input("Enter a number:")

# st.write(a)

st.set_page_config(page_title="st app",page_icon='🎮',layout='centered',initial_sidebar_state='auto')

st.title("streamlit Calculator app.")
st.markdown("---")


st.sidebar.title("Sidebars Title.")
# st.sidebar.image("img.png",use_column_width=True)
st.sidebar.write("HERE we can provide additional data about our app.")

st.sidebar.button("Sidbar button.")
col1, col2 = st.columns([1,1])

with col1:
    a = st.number_input("Enter a number",0,500)

with col2:
    b = st.number_input("Enter a number: ",0,100000)
op = st.selectbox("Select Operation :", ['+','-','*','/'])

bt = st.button("Calculate")

if op == '+':
    ans = a+b
elif op == "-":
    ans = a-b
elif op == "*":
    ans = a*b
elif op == "/":
    ans = a/b

if bt :
    st.success(f"THe result is {ans}")