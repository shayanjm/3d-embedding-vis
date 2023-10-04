import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="3D Embedding Visualization", page_icon=":mag:")
# Streamlit layout for file uploader
st.write("# 3D Interactive Cluster Visualization")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded file into a DataFrame
    df_visualization = pd.read_csv(uploaded_file)

    # Truncate the 'Prompt' text to a maximum of 50 characters
    df_visualization['Truncated_Prompt'] = df_visualization['Prompt'].apply(lambda x: (x[:97] + '...') if len(x) > 100 else x)

    # Create the scatter plot
    fig = px.scatter_3d(df_visualization, x='Dimension 1', y='Dimension 2', z='Dimension 3', color='Cluster',
                        color_continuous_scale='Viridis', title='3D Interactive Cluster Visualization')

    # Customize hover template
    hovertemplate = (
        "<b>Original Index:</b> %{customdata[0]}<br>" +
        "<b>Cluster:</b> %{customdata[1]}<br>" +
        "<b>Truncated Prompt:</b> %{customdata[2]}<br>" +
        "<extra></extra>"
    )

    # Update hover template and text size
    fig.for_each_trace(lambda trace: trace.update(hovertemplate=hovertemplate, customdata=df_visualization[['Original Index', 'Cluster', 'Truncated_Prompt']].values))
    fig.update_layout(hoverlabel=dict(font=dict(size=16)))

    # Set background color to black
    fig.update_layout(scene=dict(bgcolor='black'))

    # Display the scatter plot
    st.plotly_chart(fig, use_container_width=True)
