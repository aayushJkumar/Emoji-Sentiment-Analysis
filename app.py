import streamlit as st
from functions import file_input, txt_input, txt_to_csv

# Streamlit Web Application

def main():
    with st.sidebar:
        st.title("Input")
        file = st.file_uploader("Load your file", type=["txt", "csv"])
    with st.sidebar:
        number1 = st.number_input('Index', min_value=0, step=1)
    if file and number1 :
        if file.name[-3:] == 'csv':
            file.seek(0)
            file_base_name = file.name.replace('.csv', '')
            df=file_input(file)
#             st.checkbox("Use container width", value=False, key="use_container_width")
            score="Sentiment Score : "+str(df.loc[number1-1,'score'])
            
            st.dataframe(df.head(10))
            st.info(score)
            st.download_button("Download", df.to_csv(index=False),file_name='{0}.csv'.format(file_base_name))
        elif file.name[-3:] == 'txt' :
            file.seek(0)
            file_base_name = file.name.replace('.txt', '')
            df=txt_to_csv(file)
            df2=txt_input(df)
#             st.checkbox("Use container width", value=False, key="use_container_width")
            st.dataframe(df2.head(10))
            score="Sentiment Score : "+str(df2.loc[number1-1,'score'])
            st.info(score)
            st.download_button("Download", df2.to_csv(index=False),file_name='{0}.csv'.format(file_base_name))


if __name__ == '__main__':
    main()



