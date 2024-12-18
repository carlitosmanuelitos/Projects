import pandas as pd
import plotly.graph_objs as go

# Load the dataset
file_path = 'data_revenue_LSP.csv'  # Replace with your file path
data = pd.read_csv(file_path, delimiter=';')

# Prepare the data for visualization
country_revenue = data.groupby('COUNTRY')['EUR'].sum().reset_index()
country_revenue_sorted = country_revenue.sort_values('EUR', ascending=False)

# Extract top 5 countries and group the rest as "Other"
top_5_countries = country_revenue_sorted.head(5)
other_countries = country_revenue_sorted.iloc[5:]
viz_data = top_5_countries.copy()
viz_data.loc[len(viz_data)] = ['Other', other_countries['EUR'].sum()]

# Sort "Other" as the last entry
viz_data = viz_data.sort_values(by='EUR', ascending=False)
viz_data = pd.concat([viz_data[viz_data['COUNTRY'] != 'Other'], viz_data[viz_data['COUNTRY'] == 'Other']])

# Color palette: Professional and clean (Apple-like)
colors = ['#2F4F4F', '#4F81BD', '#9BBB59', '#C0504D', '#8064A2', '#A6A6A6']

# Function to create labels: Two rows with country code, % and value
def generate_labels(viz_data):
    total = viz_data['EUR'].sum()
    labels = [
        f"<b>{row['COUNTRY']} - {row['EUR']/total:.1%}</b><br>{row['EUR']/1_000_000:.1f}€ Million"
        for _, row in viz_data.iterrows()
    ]
    return labels

# Create the donut chart
def create_country_revenue_donut(viz_data):
    total_revenue = viz_data['EUR'].sum()
    largest_piece_index = viz_data['EUR'].idxmax()
    pull_values = [0.1 if idx == largest_piece_index else 0 for idx in viz_data.index]

    custom_labels = generate_labels(viz_data)

    fig = go.Figure(data=[go.Pie(
        labels=viz_data['COUNTRY'],  # Legend will show country codes
        values=viz_data['EUR'],
        hole=0.4,  # Donut chart
        marker_colors=colors,
        text=custom_labels,  # Custom visible labels
        textinfo='text',  # Custom text only
        textposition='outside',
        hovertemplate='<b>%{label}</b><br>Revenue: €%{value:,.2f}<br>Percentage: %{percent}<extra></extra>',
        pull=pull_values  # Protrude the largest slice
    )])

    fig.update_layout(
        title={
            'text': 'Revenue Distribution by Country - 2024',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#2C3E50')
        },
        legend=dict(
            title=None,  # Remove legend title
            font=dict(color='#2C3E50', size=12),
            traceorder='normal'  # Maintain order, "Other" at bottom
        ),
        font=dict(family="Arial, sans-serif", size=14, color='#2C3E50'),
        height=600,
        width=900,
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin=dict(t=100, b=50, l=50, r=50)
    )

    return fig

# Create and display the chart
fig = create_country_revenue_donut(viz_data)
fig.show()




import pandas as pd
import plotly.graph_objs as go

# Load the dataset
file_path = 'data_revenue_LSP.csv'  # Replace with your file path
data = pd.read_csv(file_path, delimiter=';')

# Group data by ORDER_CHANNEL and sum EUR
channel_revenue = data.groupby('ORDERCHANNEL')['EUR'].sum().reset_index()

# Sort data in descending order of revenue
channel_revenue_sorted = channel_revenue.sort_values('EUR', ascending=False)

# Get the top 5 order channels
top_5_channels = channel_revenue_sorted.head(5)
other_channels = channel_revenue_sorted.iloc[5:]

# Combine 'Other' category
other_total = other_channels['EUR'].sum()
viz_data = top_5_channels.copy()
viz_data.loc[len(viz_data)] = ['Other', other_total]

# Define Apple-like color palette
colors = ['#2F4F4F', '#4F81BD', '#9BBB59', '#C0504D', '#8064A2', '#A6A6A6']  # Top 5 + 'Other'

# Function to create custom labels: Two rows (Channel & %, Value in Millions)
def generate_labels(viz_data):
    total = viz_data['EUR'].sum()
    labels = [
        f"<b>{row['ORDERCHANNEL']} - {row['EUR']/total:.1%}</b><br>{row['EUR']/1_000_000:.1f}€ Million"
        for _, row in viz_data.iterrows()
    ]
    return labels

# Create the donut chart
def create_top5_order_channel_donut(viz_data):
    total_revenue = viz_data['EUR'].sum()
    largest_piece_index = viz_data['EUR'].idxmax()  # Find the largest slice
    pull_values = [0.1 if idx == largest_piece_index else 0 for idx in viz_data.index]

    custom_labels = generate_labels(viz_data)

    # Create the chart
    fig = go.Figure(data=[go.Pie(
        labels=viz_data['ORDERCHANNEL'],  # Legend shows order channel names
        values=viz_data['EUR'],
        hole=0.4,  # Donut chart
        marker_colors=colors,
        text=custom_labels,  # Custom labels
        textinfo='text',  # Show custom text outside the slices
        textposition='outside',
        hovertemplate='<b>%{label}</b><br>Revenue: €%{value:,.2f}<br>Percentage: %{percent}<extra></extra>',
        pull=pull_values  # Protrude the largest slice
    )])

    # Customize layout
    fig.update_layout(
        title={
            'text': 'Revenue Distribution by Order Channel - 2024',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#2C3E50')
        },
        legend=dict(
            title=None,  # Remove legend title
            font=dict(color='#2C3E50', size=12),
            traceorder='normal'  # Maintain original order
        ),
        font=dict(family="Arial, sans-serif", size=14, color='#2C3E50'),
        height=600,
        width=900,
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin=dict(t=100, b=50, l=50, r=50)
    )

    return fig

# Create and display the chart
fig = create_top5_order_channel_donut(viz_data)
fig.show()
