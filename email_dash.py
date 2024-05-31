import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import requests
import re

app = dash.Dash(__name__)


df = pd.read_csv('combined_emails.csv')
df = df.dropna()


def create_bar_chart():
    label_counts = df['label'].value_counts().reset_index()
    label_counts.columns = ['label', 'count']
    label_counts['label'] = label_counts['label'].map({1: 'Spam', 0: 'Ham'})
    fig = px.bar(label_counts, x='label', y='count', title="Distribution of Email Types")
    return fig

def word_freq(type, section):
    vectorizer = CountVectorizer(stop_words='english')
    word_matrix = vectorizer.fit_transform(df[type])

    # Sum up word counts and convert to a DataFrame
    word_counts = pd.DataFrame(word_matrix.sum(axis=0), columns=vectorizer.get_feature_names_out())
    word_counts = word_counts.transpose().reset_index()
    word_counts.columns = ['word', 'count']
    asc = False
    if section == 'bot':
        asc = True
    top_words = word_counts.sort_values('count', ascending=asc).head(20)

    if section == 'bot':
        var_title = "Rarest Words in Email " + type
    else:
        var_title = "Top Words in Email " + type
    fig = px.bar(top_words, x='word', y='count', title=var_title)
    return fig

def clean_text(text):
   
    cleaned_text = re.sub(r'[^\w\s,.?!]', '', text.replace('\n', ' ').replace('\r', ' '))
    return cleaned_text




app.layout = html.Div(children=[
    html.H1('Email Classification Dashboard'),

    html.Div('SpamDash: A dashboard for spam email classification and ML model metrics'),
    dcc.Input(id="input-subject", type="text", placeholder="Enter Email Subject", style={'width': '100%'}),
    dcc.Textarea(id="input-body", placeholder="Enter Email Body", style={'width': '100%', 'height': 100}),
    html.Button("Classify Email", id="classify-button"),
    html.Div(id="result-output"),

    dcc.Graph(id='email-type-distribution'),
    html.Div([
        dcc.Dropdown(
            id='subject-word-dropdown',
            options=[
                {'label': 'Top Words', 'value': 'top'},
                {'label': 'Bottom Words', 'value': 'bot'}
            ],
            value='top',
            style={'width': '50%'}
        ),
        dcc.Graph(id='subject-word-frequency'),
    ]),
    html.Div([
        dcc.Dropdown(
            id='body-word-dropdown',
            options=[
                {'label': 'Top Words', 'value': 'top'},
                {'label': 'Bottom Words', 'value': 'bot'}
            ],
            value='top',
            style={'width': '50%'}
        ),
        dcc.Graph(id='body-word-frequency'),
    ])
])

@app.callback(
    Output("result-output", "children"),
    Input("classify-button", "n_clicks"),
    [Input("input-subject", "value"), Input("input-body", "value")]
)
def classify_email(n_clicks, subject, body):
    if n_clicks is None or not subject or not body:
        return "Please enter a subject and body to classify the email."
    url = 'http://localhost:5000/predict'  # Ensure this matches endpoint exactly
    subject_clean = clean_text(subject)
    body_clean = clean_text(body)
    data = {'subject': subject_clean, 'body': body_clean}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        result = response.json()['prediction']
        return f"The email is classified as: {result}"
    else:
        return "Error: Could not connect to the backend."

@app.callback(
    Output('email-type-distribution', 'figure'),
    Input('email-type-distribution', 'id')  
)
def update_email_type_graph(_):
    return create_bar_chart()

@app.callback(
    Output('subject-word-frequency', 'figure'),
    [Input('subject-word-dropdown', 'value'),
     Input('subject-word-frequency', 'id')]
)
def update_subject_word_freq_graph(dropdown_value, _):
    return word_freq('subject', dropdown_value)

@app.callback(
    Output('body-word-frequency', 'figure'),
    [Input('body-word-dropdown', 'value'),
     Input('body-word-frequency', 'id')]
)
def update_body_word_freq_graph(dropdown_value, _):
    return word_freq('body', dropdown_value)


if __name__ == '__main__':
    app.run_server(debug=True)
