import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv('gate_way.csv')

gate_type = data.groupby('GATE_TYPE')['GATE_NAME'].count().reset_index()
gate_type.columns = ["GATE_TYPE", "Count"]

cell_color1 = ['orange', 'lightgreen']

fig1 = go.Figure(data=[go.Table(
    header=dict(values=["GATE_TYPE", "Count"]),
    cells=dict(values=[gate_type['GATE_TYPE'], gate_type['Count']], fill=dict(color=cell_color1)))])

layout = go.Layout(
    title='Gate Type Counts'
)

gate_counts = data.groupby(['GATE_TYPE', 'GATE_NAME']).size().reset_index(name='Count')

cell_color3 = ['green', 'yellow', 'lightblue']

fig3 = go.Figure(data=[go.Table(
    header=dict(values=["GATE_NAME", "GATE_TYPE", "Count"]),
    cells=dict(values=[gate_counts['GATE_NAME'], gate_counts['GATE_TYPE'], gate_counts['Count']], fill=dict(color=cell_color3)))])

layout = go.Layout(
    title='Gate Type and Gate Name Counts'
)

fig1.update_layout(layout)
fig1.show()

fig2 = px.bar(gate_type, x='GATE_TYPE', y='Count',
              title='Gate Type Counts', color_discrete_sequence=['green'])
fig2.show()

fig3.update_layout(layout)
fig3.show()
