"""
================================================================================
🎓 WORLD UNIVERSITY RANKING INTERACTIVE DASHBOARD
================================================================================
A Power BI-style interactive dashboard built with Python

WHAT THIS APP DOES:
- Displays university rankings with interactive charts
- Allows filtering by country, rank, and score
- Predicts university ranking using Machine Learning
- Shows recommendations based on filters

TECHNOLOGIES USED:
- Streamlit: Web app framework (creates the UI)
- Pandas: Data manipulation (handles CSV data)
- Plotly: Interactive charts (creates visualizations)
- Scikit-learn: Machine Learning (prediction model)

HOW TO RUN THIS APP:
1. Open terminal/command prompt
2. Navigate to project folder: cd "d:\World University Ranking"
3. Install requirements: pip install -r requirements.txt
4. Run the app: streamlit run app.py
5. Open browser at: http://localhost:8501

Author: Data Science Project
================================================================================
"""

# ==============================================================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# ==============================================================================
# Each library has a specific purpose:

import streamlit as st          # Creates web interface (buttons, sliders, charts)
import pandas as pd             # Reads and manipulates data (like Excel for Python)
import plotly.express as px     # Creates interactive charts easily
import plotly.graph_objects as go  # Creates custom/advanced charts
from sklearn.ensemble import RandomForestRegressor  # Machine Learning model
import numpy as np              # Mathematical operations on arrays

# ==============================================================================
# STEP 2: CONFIGURE THE PAGE
# ==============================================================================
# This sets up how the web page looks when it loads

st.set_page_config(
    page_title="World University Rankings",  # Browser tab title
    page_icon="🎓",                          # Browser tab icon
    layout="wide"                            # Use full screen width
)

# ==============================================================================
# STEP 3: ADD CUSTOM STYLING (CSS)
# ==============================================================================
# CSS controls colors, fonts, spacing of elements
# This is optional but makes the app look professional

st.markdown("""
<style>
    .block-container {padding-top: 1rem; padding-bottom: 1rem;}
    h1, h2, h3 {color: #1e3a5f;}
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# STEP 4: CREATE FUNCTIONS TO LOAD DATA AND TRAIN MODEL
# ==============================================================================

# @st.cache_data is a "decorator" - it saves the result so we don't reload
# the CSV file every time the user interacts with the app (makes it faster!)
@st.cache_data
def load_data():
    """
    Load university data from CSV file
    Returns: DataFrame containing all university information
    """
    return pd.read_csv("data.csv")

# @st.cache_resource caches the ML model so it's not retrained every time
@st.cache_resource
def train_model(_df):
    """
    Train a Machine Learning model to predict university ranking
    
    How it works:
    - Input (X): Teaching, Research, Citations scores
    - Output (y): University Rank
    - Model learns the relationship between scores and rank
    
    Parameters:
        _df: DataFrame with university data
    Returns:
        Trained RandomForest model
    """
    # Features (inputs) - what we use to predict
    X = _df[['Teaching', 'Research', 'Citations']]
    
    # Target (output) - what we want to predict
    y = _df['Rank']
    
    # Create and train the model
    # n_estimators=50 means use 50 decision trees
    # random_state=42 ensures reproducible results
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X, y)  # Train the model
    
    return model

# ==============================================================================
# STEP 5: LOAD DATA AND TRAIN MODEL
# ==============================================================================
# Call our functions to get data and trained model

df = load_data()          # Load CSV into a DataFrame
model = train_model(df)   # Train ML model on the data

# ==============================================================================
# STEP 6: CREATE SIDEBAR FILTERS
# ==============================================================================
# Sidebar appears on the left side of the page
# Users can filter data using these controls

st.sidebar.header("🎛️ Filters")

# ------------------------------------------------------------------------------
# Filter 1: Country Selection (Multiselect dropdown)
# ------------------------------------------------------------------------------
# Get unique countries from data, sort alphabetically
countries = sorted(df['Country'].unique().tolist())

# Create multiselect widget - users can select multiple countries
selected_countries = st.sidebar.multiselect(
    "Select Countries",           # Label shown to user
    options=countries,            # Available options
    default=countries             # Default: all countries selected
)

# ------------------------------------------------------------------------------
# Filter 2: Rank Range (Slider)
# ------------------------------------------------------------------------------
# Users can select a range of ranks (e.g., Top 1-50)
rank_range = st.sidebar.slider(
    "Rank Range",
    min_value=1,                  # Minimum possible value
    max_value=100,                # Maximum possible value
    value=(1, 100)                # Default range (tuple of start, end)
)

# ------------------------------------------------------------------------------
# Filter 3: Score Range (Slider)
# ------------------------------------------------------------------------------
# Users can filter by overall score
score_range = st.sidebar.slider(
    "Score Range",
    min_value=60.0,
    max_value=100.0,
    value=(60.0, 100.0),
    step=1.0                      # Slider moves in steps of 1.0
)

# ------------------------------------------------------------------------------
# Apply All Filters to Data
# ------------------------------------------------------------------------------
# Filter the DataFrame based on user selections
# The & symbol means AND - all conditions must be true

if selected_countries:  # Check if at least one country is selected
    filtered_df = df[
        (df['Country'].isin(selected_countries)) &    # Country matches selection
        (df['Rank'] >= rank_range[0]) &               # Rank >= minimum
        (df['Rank'] <= rank_range[1]) &               # Rank <= maximum
        (df['Overall_Score'] >= score_range[0]) &     # Score >= minimum
        (df['Overall_Score'] <= score_range[1])       # Score <= maximum
    ].copy()  # .copy() creates a new DataFrame (avoids warnings)
else:
    filtered_df = pd.DataFrame()  # Empty DataFrame if no country selected

# ------------------------------------------------------------------------------
# Show Statistics in Sidebar
# ------------------------------------------------------------------------------
st.sidebar.markdown("---")  # Horizontal line separator
st.sidebar.metric("Showing", f"{len(filtered_df)} universities")

# ==============================================================================
# STEP 7: CREATE MAIN HEADER
# ==============================================================================
# This is the title shown at the top of the page

st.title("🎓 World University Rankings")
st.caption("Interactive dashboard for exploring global university rankings")

# ==============================================================================
# STEP 8: CREATE KPI CARDS (Key Performance Indicators)
# ==============================================================================
# KPI cards show important summary statistics at a glance
# Similar to the cards you see at the top of Power BI dashboards

if len(filtered_df) > 0:  # Only show if we have data
    
    # Create 4 columns for 4 KPI cards
    c1, c2, c3, c4 = st.columns(4)
    
    # Card 1: Total number of universities after filtering
    c1.metric("Total Universities", len(filtered_df))
    
    # Card 2: Average overall score
    # .mean() calculates average, :.1f formats to 1 decimal place
    c2.metric("Avg Score", f"{filtered_df['Overall_Score'].mean():.1f}")
    
    # Card 3: Country with most universities
    # .value_counts() counts occurrences, .index[0] gets the top one
    c3.metric("Top Country", filtered_df['Country'].value_counts().index[0])
    
    # Card 4: Best (lowest number) rank in filtered data
    c4.metric("Best Rank", f"#{filtered_df['Rank'].min()}")
    
else:
    # Show warning if no data matches filters
    st.warning("No universities match your filters. Please adjust the selection.")
    st.stop()  # Stop execution here (don't render rest of page)

st.markdown("---")  # Horizontal line separator

# ==============================================================================
# STEP 9: CREATE CHARTS - ROW 1
# ==============================================================================
# Create two columns side by side for charts

col1, col2 = st.columns(2)

# ------------------------------------------------------------------------------
# Chart 1: Top 10 Universities (Horizontal Bar Chart)
# ------------------------------------------------------------------------------
with col1:  # First column
    st.subheader("Top 10 Universities")
    
    # Get top 10 universities (lowest rank numbers = best)
    # nsmallest(10, 'Rank') gets 10 rows with smallest Rank values
    top_10 = filtered_df.nsmallest(10, 'Rank')
    
    # Create horizontal bar chart using Plotly Express
    fig_bar = px.bar(
        top_10,                          # Data to plot
        x='Overall_Score',               # X-axis: scores (bar length)
        y='University',                  # Y-axis: university names
        orientation='h',                 # 'h' = horizontal bars
        color='Overall_Score',           # Color bars by score
        color_continuous_scale=[[0, '#e8f4f8'], [1, '#2c5282']],  # Blue gradient
        hover_data=['Country', 'Rank']   # Extra info shown on hover
    )
    
    # Customize the chart appearance
    fig_bar.update_layout(
        height=400,                              # Chart height in pixels
        yaxis={'categoryorder': 'total ascending'},  # Sort bars by value
        showlegend=False,                        # Hide legend
        coloraxis_showscale=False,               # Hide color scale bar
        margin=dict(l=0, r=0, t=10, b=0),       # Reduce margins
        xaxis_title="Overall Score",
        yaxis_title=""
    )
    
    # Display the chart in Streamlit
    st.plotly_chart(fig_bar, use_container_width=True)

# ------------------------------------------------------------------------------
# Chart 2: Country Distribution (Pie/Donut Chart)
# ------------------------------------------------------------------------------
with col2:  # Second column
    st.subheader("Country Distribution")
    
    # Count universities per country, get top 10
    country_counts = filtered_df['Country'].value_counts().head(10).reset_index()
    country_counts.columns = ['Country', 'Count']  # Rename columns
    
    # Create donut chart (pie chart with hole in center)
    fig_pie = px.pie(
        country_counts,
        values='Count',                  # Size of each slice
        names='Country',                 # Labels for slices
        hole=0.4,                        # 0.4 = 40% hole (makes it a donut)
        color_discrete_sequence=px.colors.sequential.Blues_r  # Blue colors
    )
    
    # Customize appearance
    fig_pie.update_layout(
        height=400,
        margin=dict(l=0, r=0, t=10, b=0)
    )
    
    # Show count and percentage inside slices
    fig_pie.update_traces(textposition='inside', textinfo='value+percent')
    
    st.plotly_chart(fig_pie, use_container_width=True)

# ==============================================================================
# STEP 10: CREATE CHARTS - ROW 2
# ==============================================================================

col3, col4 = st.columns(2)

# ------------------------------------------------------------------------------
# Chart 3: Score vs Rank (Scatter Plot)
# ------------------------------------------------------------------------------
with col3:
    st.subheader("Score vs Rank")
    
    # Scatter plot shows relationship between two variables
    # Each dot = one university
    fig_scatter = px.scatter(
        filtered_df,
        x='Overall_Score',               # X-axis position
        y='Rank',                        # Y-axis position
        color='Country',                 # Different color per country
        hover_name='University',         # Show name on hover
        size_max=12,                     # Maximum dot size
        color_discrete_sequence=px.colors.qualitative.Safe  # Colorblind-friendly
    )
    
    fig_scatter.update_layout(
        height=400,
        yaxis=dict(autorange='reversed'),  # Reverse Y so rank 1 is at top
        margin=dict(l=0, r=0, t=10, b=0),
        showlegend=True,
        legend=dict(font=dict(size=9), itemsizing='constant')
    )
    
    # Make dots semi-transparent to see overlapping points
    fig_scatter.update_traces(marker=dict(size=8, opacity=0.7))
    
    st.plotly_chart(fig_scatter, use_container_width=True)

# ------------------------------------------------------------------------------
# Chart 4: Correlation Heatmap
# ------------------------------------------------------------------------------
with col4:
    st.subheader("Correlation Heatmap")
    
    # Correlation shows how variables relate to each other
    # Value of 1.0 = perfect positive correlation
    # Value of -1.0 = perfect negative correlation
    # Value of 0 = no correlation
    
    # Select numeric columns for correlation
    num_cols = ['Teaching', 'Research', 'Citations', 'Industry_Income', 'International_Outlook', 'Overall_Score']
    
    # Calculate correlation matrix
    corr = filtered_df[num_cols].corr()
    
    # Create heatmap using graph_objects (more control than express)
    fig_heat = go.Figure(data=go.Heatmap(
        z=corr.values,                   # Correlation values (colors)
        x=['Teaching', 'Research', 'Citations', 'Industry', 'Intl Outlook', 'Overall'],
        y=['Teaching', 'Research', 'Citations', 'Industry', 'Intl Outlook', 'Overall'],
        colorscale=[[0, '#f7fbff'], [0.5, '#6baed6'], [1, '#08306b']],  # Blue scale
        text=np.round(corr.values, 2),   # Show values as text
        texttemplate='%{text}',          # Format for text
        textfont={"size": 10},
        showscale=False                  # Hide color bar
    ))
    
    fig_heat.update_layout(
        height=400,
        margin=dict(l=0, r=0, t=10, b=0),
        xaxis=dict(tickangle=45)         # Angle x-axis labels
    )
    
    st.plotly_chart(fig_heat, use_container_width=True)

st.markdown("---")

# ==============================================================================
# STEP 11: CREATE DATA TABLE
# ==============================================================================
# Interactive table where users can explore the data

st.subheader("📋 University Data")

# Dropdown to choose sorting column
sort_by = st.selectbox(
    "Sort by",
    ['Rank', 'Overall_Score', 'Teaching', 'Research', 'Citations'],
    index=0  # Default to first option (Rank)
)

# Sort the data by selected column
display_df = filtered_df.sort_values(by=sort_by).reset_index(drop=True)

# Display interactive table
# Only show selected columns for cleaner view
st.dataframe(
    display_df[['Rank', 'University', 'Country', 'Overall_Score', 'Teaching', 'Research', 'Citations']],
    use_container_width=True,  # Expand to full width
    height=350                 # Fixed height with scroll
)

# Download button - allows users to export filtered data as CSV
st.download_button(
    "📥 Download Data",                    # Button label
    filtered_df.to_csv(index=False),      # Convert DataFrame to CSV string
    "universities.csv",                    # Downloaded filename
    "text/csv"                            # File type
)

st.markdown("---")

# ==============================================================================
# STEP 12: PREDICTION AND RECOMMENDATIONS SECTION
# ==============================================================================

col_pred, col_rec = st.columns(2)

# ------------------------------------------------------------------------------
# Left Column: Machine Learning Prediction
# ------------------------------------------------------------------------------
with col_pred:
    st.subheader("🤖 Predict Ranking")
    
    # Input sliders for ML model
    # Users adjust these to see predicted ranking
    teaching = st.slider("Teaching Score", 30, 100, 70)
    research = st.slider("Research Score", 30, 100, 70)
    citations = st.slider("Citations Score", 30, 100, 70)
    
    # Predict button
    if st.button("Predict", type="primary"):
        # Create input array for model (must be 2D: [[values]])
        # model.predict() returns array, [0] gets first value
        pred = model.predict([[teaching, research, citations]])[0]
        
        # Ensure prediction is between 1 and 100
        pred = int(max(1, min(100, round(pred))))
        
        # Show result
        st.success(f"**Predicted Rank: #{pred}**")
        
        # Find similar universities (within 3 ranks)
        similar = df[(df['Rank'] >= pred - 3) & (df['Rank'] <= pred + 3)].head(3)
        if len(similar) > 0:
            st.write("**Similar universities:**")
            for _, r in similar.iterrows():
                st.write(f"• #{r['Rank']} {r['University']}")

# ------------------------------------------------------------------------------
# Right Column: Smart Recommendations
# ------------------------------------------------------------------------------
with col_rec:
    st.subheader("🎯 Top Recommendations")
    
    # Get top 5 universities from filtered data
    top_5 = filtered_df.nsmallest(5, 'Rank')
    
    # Display each recommendation with medal emoji
    for _, row in top_5.iterrows():
        # Assign medal based on rank
        medal = "🥇" if row['Rank'] == 1 else "🥈" if row['Rank'] == 2 else "🥉" if row['Rank'] == 3 else "🏅"
        
        # Display formatted recommendation
        st.markdown(f"""
        **{medal} #{int(row['Rank'])} - {row['University']}**  
        📍 {row['Country']} • Score: {row['Overall_Score']:.1f}
        """)

# ==============================================================================
# STEP 13: FOOTER
# ==============================================================================
st.markdown("---")
st.caption("World University Rankings Dashboard • Built with Streamlit & Plotly")

# ==============================================================================
# END OF APP
# ==============================================================================
"""
SUMMARY OF WHAT WE BUILT:
========================

1. SIDEBAR FILTERS - Let users filter data interactively
2. KPI CARDS - Show summary statistics at a glance  
3. BAR CHART - Top 10 universities visualization
4. PIE CHART - Country distribution
5. SCATTER PLOT - Score vs Rank relationship
6. HEATMAP - Correlation between metrics
7. DATA TABLE - Explore and download data
8. ML PREDICTION - Predict rank from scores
9. RECOMMENDATIONS - Top universities based on filters

KEY STREAMLIT CONCEPTS USED:
============================
- st.sidebar.*      : Creates sidebar elements
- st.columns()      : Creates side-by-side layout
- st.metric()       : Creates KPI cards
- st.plotly_chart() : Displays Plotly charts
- st.dataframe()    : Displays interactive tables
- st.button()       : Creates clickable buttons
- st.slider()       : Creates slider inputs
- @st.cache_data    : Caches data to improve performance

NEXT STEPS TO LEARN:
====================
1. Try modifying the color schemes
2. Add more charts (line chart, box plot)
3. Add more ML models (compare accuracy)
4. Deploy to Streamlit Cloud (free hosting)
"""
