# 🎓 World University Ranking Interactive Dashboard

A **Power BI-style** interactive dashboard built with **Streamlit** and **Plotly** for exploring world university rankings data.

> **Perfect for Beginners!** This project includes detailed comments explaining every line of code.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.18+-green.svg)

---

## 📋 Table of Contents

1. [Quick Start (3 Steps)](#-quick-start-3-steps)
2. [Detailed Setup Guide](#-detailed-setup-guide)
3. [Features](#-features)
4. [Project Structure](#-project-structure)
5. [How the Code Works](#-how-the-code-works)
6. [Troubleshooting](#-troubleshooting)

---

## 🚀 Quick Start (3 Steps)

```bash
# Step 1: Navigate to project folder
cd "d:\World University Ranking"

# Step 2: Install all required packages
pip install -r requirements.txt

# Step 3: Run the dashboard
streamlit run app.py
```

**That's it!** Your browser will open automatically at `http://localhost:8501`

---

## 📖 Detailed Setup Guide

### Prerequisites

Before starting, make sure you have:

- ✅ **Python 3.9 or higher** installed ([Download Python](https://www.python.org/downloads/))
- ✅ **pip** (Python package manager - comes with Python)
- ✅ **Web browser** (Chrome, Firefox, Edge, etc.)

### Step-by-Step Instructions

#### Step 1: Open Terminal/Command Prompt

**Windows:**

- Press `Win + R`, type `cmd`, press Enter
- OR search for "Command Prompt" in Start menu

**Mac/Linux:**

- Open Terminal application

#### Step 2: Navigate to Project Folder

```bash
# Windows
cd /d "d:\World University Ranking"

# Mac/Linux
cd ~/path/to/World\ University\ Ranking
```

#### Step 3: (Optional) Create Virtual Environment

Virtual environments keep project packages separate from system packages.

```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate
```

You'll see `(venv)` in your terminal when activated.

#### Step 4: Install Required Packages

```bash
pip install -r requirements.txt
```

**What gets installed:**
| Package | Purpose | Size |
|---------|---------|------|
| streamlit | Web app framework | ~80MB |
| pandas | Data handling | ~50MB |
| plotly | Interactive charts | ~25MB |
| scikit-learn | Machine Learning | ~30MB |
| numpy | Math operations | ~20MB |

_Total: ~200MB (first install takes 2-5 minutes)_

#### Step 5: Run the Dashboard

```bash
streamlit run app.py
```

**Expected output:**

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

#### Step 6: Open in Browser

- Browser should open automatically
- If not, manually go to: `http://localhost:8501`

#### Step 7: Stop the Server

Press `Ctrl + C` in terminal to stop the app.

---

## ✨ Features

### 🎛️ Interactive Filters (Sidebar)

- **Country Selection** - Choose one or more countries
- **Rank Range** - Filter by ranking (1-100)
- **Score Range** - Filter by overall score

### 📊 KPI Cards

- Total Universities count
- Average Score
- Top Country
- Best Rank

### 📈 Interactive Charts

| Chart            | Description                        |
| ---------------- | ---------------------------------- |
| **Bar Chart**    | Top 10 universities by score       |
| **Pie Chart**    | University distribution by country |
| **Scatter Plot** | Score vs Rank relationship         |
| **Heatmap**      | Correlation between metrics        |

### 📋 Data Table

- Sortable by any column
- Downloadable as CSV
- Shows filtered results

### 🤖 ML Prediction

- Input Teaching, Research, Citations scores
- Get predicted ranking instantly
- See similar ranked universities

### 🎯 Smart Recommendations

- Top 5 universities based on your filters
- Shows country and score

---

## 📁 Project Structure

```
World University Ranking/
│
├── app.py              # Main application (ALL code here)
│                       # Contains: UI + Charts + ML + Logic
│
├── data.csv            # Dataset with 100 universities
│                       # Columns: Rank, University, Country,
│                       # Teaching, Research, Citations, etc.
│
├── requirements.txt    # Python package dependencies
│                       # Install with: pip install -r requirements.txt
│
└── README.md           # This documentation file
```

---

## 🔍 How the Code Works

The `app.py` file is organized into **13 steps**:

| Step | What It Does                                       |
| ---- | -------------------------------------------------- |
| 1    | Import libraries (streamlit, pandas, plotly, etc.) |
| 2    | Configure page settings (title, icon, layout)      |
| 3    | Add custom CSS for styling                         |
| 4    | Define functions to load data and train ML model   |
| 5    | Load data from CSV, train model                    |
| 6    | Create sidebar filters (country, rank, score)      |
| 7    | Display main header                                |
| 8    | Create KPI metric cards                            |
| 9    | Create Row 1 charts (bar + pie)                    |
| 10   | Create Row 2 charts (scatter + heatmap)            |
| 11   | Create sortable data table                         |
| 12   | Add prediction and recommendations                 |
| 13   | Add footer                                         |

### Key Streamlit Functions Used

```python
# Layout
st.columns(4)           # Create 4 columns side by side
st.sidebar.slider()     # Create slider in sidebar

# Display
st.title("Text")        # Large title
st.metric("Label", 42)  # KPI card with value
st.dataframe(df)        # Interactive table

# Charts
st.plotly_chart(fig)    # Display Plotly chart

# Input
st.button("Click")      # Clickable button
st.slider("Score", 0, 100)  # Slider input

# Caching
@st.cache_data          # Cache data (don't reload every time)
```

---

## 🔧 Troubleshooting

### "streamlit is not recognized"

**Solution:** Add Python Scripts to PATH or use:

```bash
python -m streamlit run app.py
```

### "No module named streamlit"

**Solution:** Install requirements:

```bash
pip install streamlit pandas plotly scikit-learn numpy
```

### Port 8501 already in use

**Solution:** Use a different port:

```bash
streamlit run app.py --server.port 8502
```

### Charts not showing

**Solution:** Update Plotly:

```bash
pip install --upgrade plotly
```

### Data not loading

**Solution:** Ensure you're in the correct directory:

```bash
cd /d "d:\World University Ranking"
dir  # Should show app.py and data.csv
```

---

## 🎓 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Plotly Python Documentation](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)

---

## 📝 Dataset Information

The `data.csv` contains 100 world universities with these columns:

| Column                | Description             | Example          |
| --------------------- | ----------------------- | ---------------- |
| Rank                  | World ranking position  | 1, 2, 3...       |
| University            | Institution name        | "Oxford", "MIT"  |
| Country               | Country location        | "United Kingdom" |
| Teaching              | Teaching score (0-100)  | 92.3             |
| Research              | Research score (0-100)  | 99.7             |
| Citations             | Citations score (0-100) | 98.0             |
| Industry_Income       | Industry income score   | 74.9             |
| International_Outlook | International score     | 96.2             |
| Overall_Score         | Combined score          | 96.4             |

---

## 🚀 Next Steps

After running this project, try:

1. **Modify colors** - Change the color schemes in charts
2. **Add new charts** - Try line charts, box plots
3. **Expand data** - Add more universities to CSV
4. **Deploy online** - Host on [Streamlit Cloud](https://streamlit.io/cloud) for free!

---

**Built with ❤️ using Python, Streamlit & Plotly**

_Happy Learning! 🎓_
#   W o r l d - U n i v e r s i t y - R a n k i n g  
 