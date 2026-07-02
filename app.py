# import streamlit as st
# import pandas as pd
# import plotly.express as px

# def sample():
#     st.title("WelcomE 👨‍💻")
#     st.header("AI Dashboard 🤖")
#     uploaded_file = st.file_uploader("Please Upload File 🗂️",type=["csv", "xlsx"])

#     if uploaded_file is not None:
#         try:
#             #READ FILE
#             if uploaded_file.name.endswith(".csv"):
#                 df = pd.read_csv(uploaded_file)
#             else:
#                 df = pd.read_excel(uploaded_file)

#             # HANDLE MISSING VALUES
#             for col in df.columns:
#                 if pd.api.types.is_numeric_dtype(df[col]):
#                     df[col] = df[col].fillna(df[col].mean())
#                 else:
#                     df[col] = df[col].fillna("Unknown")
#             #SHOW DATA
#             st.subheader("Dataset📋")
#             st.dataframe(df)

#             #KPI
#             st.subheader("Dataset Information🧠")
#             col1, col2, col3 = st.columns(3)
#             col1.metric("Rows", df.shape[0])
#             col2.metric("Columns", df.shape[1])
#             col3.metric("Missing Values", df.isnull().sum().sum())

#             #COLUMN TYPES
#             numeric_columns = df.select_dtypes(include='number').columns.tolist()
#             categorical_columns = df.select_dtypes(include='object').columns.tolist()
#             all_columns = df.columns.tolist()

#             #SIDEBAR
#             st.sidebar.header("Chart Filter🚀")

#             # Aggregation Dropdown
#             aggregation = st.sidebar.selectbox("Select Aggregation⚡",["sum", "mean", "count"])

#             #Line chart setting
#             st.sidebar.subheader("Line Chart")
#             line_x = st.sidebar.selectbox("Line Chart X-axis",all_columns,key="line_x")
#             line_y = st.sidebar.selectbox("Line Chart Y-axis",numeric_columns,key="line_y")

#             #Bar chart setting
#             st.sidebar.subheader("Bar Chart")
#             bar_x = st.sidebar.selectbox("Bar Chart X-axis",all_columns,key="bar_x")
#             bar_y = st.sidebar.selectbox("Bar Chart Y-axis",numeric_columns,key="bar_y")

#             #Line Chart
#             st.subheader("Line Chart📈📉")
#             if line_x == line_y:
#                 st.warning("Line Chart X-axis and Y-axis cannot be same")
#             else:
#                 if aggregation == "sum":
#                     line_data = df.groupby(line_x,as_index=False)[line_y].sum()
#                 elif aggregation == "mean":
#                     line_data = df.groupby(line_x,as_index=False)[line_y].mean()
#                 else:
#                     line_data = df.groupby(line_x,as_index=False)[line_y].count()

#                 fig1 = px.line(line_data,x=line_x,y=line_y,
#                     title=f"{aggregation.upper()} of {line_y}")
#                 st.plotly_chart(fig1, use_container_width=True)

#             #Bar Chart
#             st.subheader("Bar Chart📊")
#             if bar_x == bar_y:
#                 st.warning("Bar Chart X-axis and Y-axis cannot be same")
#             else:
#                 if aggregation == "sum":
#                     bar_data = df.groupby(bar_x,as_index=False)[bar_y].sum()

#                 elif aggregation == "mean":
#                     bar_data = df.groupby(bar_x,as_index=False)[bar_y].mean()
#                 else:
#                     bar_data = df.groupby(bar_x,as_index=False)[bar_y].count()
#                 fig2 = px.bar(bar_data,x=bar_x,y=bar_y,title=f"{aggregation.upper()} of {bar_y}")
#                 st.plotly_chart(fig2, use_container_width=True)

#             #Pie Chart
#             if len(categorical_columns) > 0:
#                 st.subheader("Pie Chart🥧")
#                 cat_col = st.selectbox("Select Category Column",categorical_columns)
#                 pie_data = df[cat_col].value_counts().reset_index()
#                 pie_data.columns = [cat_col, "count"]
#                 fig3 = px.pie(pie_data,names=cat_col,values="count",title="Pie Chart")
#                 st.plotly_chart(fig3, use_container_width=True)
#             else:
#                 st.info("No categorical columns found")

#         except Exception as e:
#             st.error("Error while reading file")
#             st.write(e)
#     else:
#         st.warning("Please upload a file")

import streamlit as st
import pandas as pd
import plotly.express as px

def sample():
    st.title("Welcome 👨‍💻")
    st.header("AI Dashboard 🤖")
    uploaded_file = st.file_uploader("Please Upload File 🗂️",type=["csv", "xlsx"])
    if uploaded_file is not None:
        try:
            # READ FILE
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                excel_file = pd.ExcelFile(uploaded_file)
                st.sidebar.header("Excel Sheet")
                selected_sheet = st.sidebar.selectbox("Select Sheet 📄",excel_file.sheet_names)
                df = pd.read_excel(excel_file,sheet_name=selected_sheet)

            # HANDLE MISSING VALUES
            for col in df.columns:
                if pd.api.types.is_numeric_dtype(df[col]):
                    df[col] = df[col].fillna(df[col].mean())
                else:
                    df[col] = df[col].fillna("Unknown")

            # SHOW DATA
            st.subheader("Dataset 📋")
            st.dataframe(df)
    
            # KPI CARDS
            st.subheader("Dataset Information 🧠")
            col1, col2, col3 = st.columns(3)
            col1.metric("Rows",df.shape[0])
            col2.metric("Columns",df.shape[1])
            col3.metric("Missing Values",df.isnull().sum().sum())

            # COLUMN TYPES
            numeric_columns = df.select_dtypes(include="number").columns.tolist()

            categorical_columns = df.select_dtypes(include="object").columns.tolist()
            all_columns = df.columns.tolist()

            # SIDEBAR FILTERS
            st.sidebar.header("Chart Filter 🚀")
            aggregation = st.sidebar.selectbox(
                "Select Aggregation ⚡",
                ["sum", "mean", "count"])

            # LINE CHART
            st.sidebar.subheader("Line Chart")
            line_x = st.sidebar.selectbox("Line Chart X-axis",all_columns,key="line_x")
            line_y = st.sidebar.selectbox("Line Chart Y-axis",numeric_columns,key="line_y")

            st.subheader("Line Chart 📈")
            if line_x == line_y:
                st.warning("Line Chart X-axis and Y-axis cannot be same.")
            else:
                if aggregation == "sum":
                    line_data = df.groupby(line_x,as_index=False)[line_y].sum()

                elif aggregation == "mean":
                    line_data = df.groupby(line_x,as_index=False)[line_y].mean()

                else:
                    line_data = df.groupby(line_x,as_index=False)[line_y].count()

                fig1 = px.line(line_data,x=line_x,y=line_y,
                    title=f"{aggregation.upper()} of {line_y}")

                st.plotly_chart(fig1,use_container_width=True)

            # BAR CHART
            st.sidebar.subheader("Bar Chart")
            bar_x = st.sidebar.selectbox("Bar Chart X-axis",all_columns,key="bar_x")
            bar_y = st.sidebar.selectbox("Bar Chart Y-axis",numeric_columns,key="bar_y")
            st.subheader("Bar Chart 📊")

            if bar_x == bar_y:
                st.warning("Bar Chart X-axis and Y-axis cannot be same.")

            else:
                if aggregation == "sum":
                    bar_data = df.groupby(bar_x,as_index=False)[bar_y].sum()

                elif aggregation == "mean":
                    bar_data = df.groupby(bar_x,as_index=False)[bar_y].mean()

                else:
                    bar_data = df.groupby(bar_x,as_index=False)[bar_y].count()

                fig2 = px.bar(bar_data,x=bar_x,y=bar_y,title=f"{aggregation.upper()} of {bar_y}")

                st.plotly_chart(fig2,use_container_width=True)

            # PIE CHART
            if len(categorical_columns) > 0:
                st.subheader("Pie Chart 🥧")
                cat_col = st.selectbox("Select Category Column",categorical_columns)

                pie_data = (df[cat_col].value_counts().reset_index())
                pie_data.columns = [cat_col,"Count"]

                fig3 = px.pie(pie_data,names=cat_col,values="Count",title="Pie Chart")

                st.plotly_chart(fig3,use_container_width=True)

            else:
                st.info("No categorical columns found.")

        except Exception as e:
            st.error("Error while reading file.")
            st.write(e)
    else:
        st.warning("Please upload a file.")