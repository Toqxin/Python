import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 

data=pd.read_csv('youtube.csv',encoding='ISO-8859-1')

#figure1 representation -->
data['subscribers'] = data['subscribers'].apply(lambda x: '{:,.0f}'.format(x))
youtuber=data.groupby(['Youtuber','subscribers','category','Country','uploads']).size().reset_index()
cell_height = 50
table_data = [
    go.Table(
        header=dict(values=['YOUTUBER', 'SUBSCRİBER', 'CATEGORY','COUNTRY','UPLOADS']),
        cells=dict(values=[youtuber['Youtuber'], youtuber['subscribers'], youtuber['category'],youtuber['Country'],youtuber['uploads']],
                   fill=dict(color=['lightseagreen', 'yellow', 'lightgrey','yellowgreen','azure']),
                   height=cell_height,
                   align=['center', 'center', 'center'],
                   font=dict(size=16)
                   ))
]
figure1= go.Figure(data=table_data)
figure1.show()

#figure2 representation-->
youtuber_country_count = data.groupby('Country')['Youtuber'].count().reset_index() 
youtuber_country_count.columns = ['Country', 'Youtubers Count']
figure2 = px.bar(youtuber_country_count, x='Country', y='Youtubers Count', title='Youtubers Count By Country',color_discrete_sequence=['lime'])
figure2.update_layout(
    title_font=dict(size=16),
    font=dict(size=16)
)
figure2.update_traces(marker_line_width=2, marker_line_color="black")
figure2.show()

#figure3 representation-->
channel=pd.DataFrame(data['channel_type'].value_counts())
channel=channel.reset_index()
figure3=px.pie(channel,names='channel_type',values='count',title='Channel Category Pie Chart')
figure3.update_layout(
    title_font=dict(size=16),
    font=dict(size=16)
)
figure3.show()

#figure4 representation-->
bigframe = data['category'].unique().tolist()
def extract_top3_countries(data):
    frames = []
    for big in bigframe: 
        bigdata = data.loc[data['category'] == big]
        top3_country = bigdata.groupby('Country')['highest_yearly_earnings'].mean()[:3].index.tolist()
        bigdata = bigdata.loc[data['Country'].isin(top3_country)]
        frames.append(bigdata)
    new_data = pd.concat(frames)
    return new_data

country_big_data = extract_top3_countries(data)
figure4 = px.treemap(country_big_data, path=['category', 'Country'], color='Country', color_discrete_sequence=px.colors.qualitative.Bold)
figure4.update_layout(
    title_text='Top 3 Most Earning Countries in Respective Category',
    font=dict(size=16)
)
figure4.show()
