# 🏅 OlympiTrack - Olympic Insights Dashboard

**Your ultimate Olympic data hub**

*Track the triumphs, trace the trends.*

OlympiTrack is an interactive web application built with Streamlit that provides comprehensive analysis and visualization of Olympic Games data. Explore medal tallies, analyze athlete performance, and discover trends across different countries, sports, and time periods.

## 📊 Features

### 🏆 Medal Tally Analysis
- View overall medal tallies across all Olympic Games
- Filter by specific years and countries
- Analyze individual country performance by year
- Historical medal tracking and comparisons

### 📈 Overall Analysis
- Comprehensive statistics dashboard showing:
  - Total Olympic editions, sports, host cities, events, nations, and athletes
  - Participation trends over the years
  - Event evolution timeline
  - Sport-wise event heatmaps
  - Most successful athletes across different sports

### 🌍 Country-wise Analysis
- Individual country performance tracking
- Medal tally trends over time
- Sport specialization analysis with heatmaps
- Top performing athletes by country

### 👤 Athlete-wise Analysis
- Age distribution analysis for all athletes and medalists
- Sport-specific age distribution for gold medalists
- Height vs Weight scatter plots by sport and gender
- Gender participation trends over time

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Required Packages
Install the required dependencies using pip:

```bash
pip install streamlit pandas matplotlib seaborn plotly
```

Or install from requirements.txt (create this file with the above packages):

```bash
pip install -r requirements.txt
```

### Data Files
Ensure you have the following data files in your project directory:

1. **Data folder structure:**
   ```
   data/
   ├── athlete_events.csv
   └── noc_regions.csv
   ```

2. **Logo file:**
   ```
   logo.png
   ```

3. **Helper modules:**
   ```
   preprocessor.py
   helper.py
   ```

## 🚀 Usage

1. **Clone or download the project files**
2. **Ensure all required files are in place:**
   - Main application file (your Streamlit app)
   - Data files in the `data/` folder
   - Logo image
   - Helper modules (`preprocessor.py` and `helper.py`)

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```
   Replace `app.py` with your main application filename.

4. **Access the dashboard:**
   - The application will open in your default web browser
   - Navigate using the sidebar menu to explore different analysis sections

## 📁 File Structure

```
olympitrack/
├── app.py                 # Main Streamlit application
├── preprocessor.py        # Data preprocessing functions
├── helper.py             # Helper functions for analysis
├── logo.png              # Application logo
├── data/
│   ├── athlete_events.csv # Main Olympic dataset
│   └── noc_regions.csv   # Country/region mapping
└── README.md             # This file
```

## 📊 Data Sources

The application uses Olympic Games data that should include:
- **athlete_events.csv**: Individual athlete records with events, medals, and personal details
- **noc_regions.csv**: Mapping of National Olympic Committee codes to regions/countries

### Expected Data Columns
- **athlete_events.csv**: Name, Sex, Age, Height, Weight, Team, NOC, Games, Year, Season, City, Sport, Event, Medal
- **noc_regions.csv**: NOC, region, notes

## 🎨 Features Overview

### Interactive Sidebar Navigation
- **Medal Tally**: Historical medal analysis with year and country filters
- **Overall Analysis**: Comprehensive Olympic statistics and trends
- **Country-wise Analysis**: Individual country performance deep-dive
- **Athlete-wise Analysis**: Demographics and performance patterns

### Visualization Types
- Interactive line charts (Plotly)
- Heatmaps (Seaborn)
- Distribution plots (Plotly)
- Scatter plots (Matplotlib/Seaborn)
- Statistical tables

## 🔧 Customization

### Styling
The application includes custom CSS for:
- Sidebar theming with dark blue background
- Logo and header positioning
- Container padding adjustments

### Adding New Analysis
To extend the application:
1. Add new analysis functions to `helper.py`
2. Create new menu options in the sidebar radio selection
3. Implement the corresponding analysis section in the main application

## 🐛 Troubleshooting

### Common Issues
1. **Missing data files**: Ensure all CSV files are in the correct `data/` directory
2. **Import errors**: Verify all required packages are installed
3. **Logo not found**: Check that `logo.png` exists in the root directory
4. **Helper module errors**: Ensure `preprocessor.py` and `helper.py` are properly implemented

### Performance Optimization
- Large datasets may require additional caching using `@st.cache_data`
- Consider data sampling for very large datasets
- Optimize plotting functions for better rendering speed

## 📄 License

This project is open source. Please ensure you have appropriate rights to use the Olympic data according to your local regulations and data source terms.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For questions or issues:
- Check the troubleshooting section
- Review Streamlit documentation: https://docs.streamlit.io
- Check data preprocessing and helper function implementations

---

*Built with ❤️ using Streamlit, Pandas, Plotly, and Matplotlib*
