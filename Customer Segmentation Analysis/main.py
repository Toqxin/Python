import pandas as pd
import plotly.express as px

data = pd.read_csv('dataset.csv', encoding='ISO-8859-1')

profession_gender = data.groupby(['Profession', 'Gender']).size().reset_index()
profession_gender.columns = ['Professions', 'Genders', 'Count']

male_data = profession_gender[profession_gender['Genders'] == 'Male']
male_graph = px.bar(male_data, x='Professions', y='Count', title='Male')
male_graph.show()

female_data = profession_gender[profession_gender['Genders'] == 'Female']
female_graph = px.bar(female_data, x='Professions', y='Count', title='Female',color_discrete_sequence=['pink'])
female_graph.show()

profession_spendingScore = data.groupby(['Profession', 'Spending_Score']).size().reset_index()
profession_spendingScore.columns = ['Professions', 'Spending Score', 'Count']
profession_spendingScore_graph = px.bar(profession_spendingScore, x='Professions', y='Count', color='Spending Score', title='Spending Score')
profession_spendingScore_graph.show()

profession_pie = pd.DataFrame(data['Profession'].value_counts()).reset_index()
profession_pie_graph = px.pie(profession_pie,names='Profession', values='count',title='Profession Pie Graph')
profession_pie_graph.show()

