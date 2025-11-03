"""
Main script to run complete Airbnb analysis
Business Intelligence Engineer - End-to-End Project Runner
"""

import sys
from pathlib import Path

# Import modules
from etl_pipeline import AirbnbETLPipeline
from analysis_queries import AirbnbAnalytics
from visualizations import AirbnbVisualizations
import pandas as pd
import matplotlib.pyplot as plt

def main():
    """Run complete analysis pipeline"""
    
    # Configuration
    CITIES = ['amsterdam', 'athens', 'barcelona', 'berlin', 'budapest',
              'lisbon', 'london', 'paris', 'rome', 'vienna']
    PERIODS = ['weekdays', 'weekends']
    DATA_DIR = '.'
    
    print("=" * 60)
    print("AIRBNB SUPPLY ANALYSIS - BUSINESS INTELLIGENCE ENGINEER PROJECT")
    print("=" * 60)
    print()
    
    # Step 1: ETL Pipeline
    print("STEP 1: Running ETL Pipeline...")
    print("-" * 60)
    pipeline = AirbnbETLPipeline(DATA_DIR, CITIES, PERIODS)
    processed_data = pipeline.run_pipeline(output_path='processed_airbnb_data.csv')
    print()
    
    # Step 2: Analysis Queries
    print("STEP 2: Running Analytical Queries...")
    print("-" * 60)
    analytics = AirbnbAnalytics(processed_data)
    
    print("\n--- Top 5 Cities by Average Price ---")
    top_cities = analytics.top_n_cities_by_price(5)
    print(top_cities)
    
    print("\n--- Weekend vs Weekday Pricing ---")
    period_analysis = analytics.weekend_vs_weekday_pricing()
    print(period_analysis['period_stats'])
    print(f"Weekend Premium: {period_analysis['premium_pct']:.2f}%")
    
    print("\n--- Superhost Performance ---")
    superhost_perf = analytics.superhost_performance_analysis()
    print(superhost_perf)
    print()
    
    # Step 3: Visualizations
    print("STEP 3: Generating Visualizations...")
    print("-" * 60)
    viz = AirbnbVisualizations(processed_data)
    
    # Generate individual visualizations
    print("Generating price distribution plot...")
    viz.plot_price_distribution_by_city()
    plt.savefig('price_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Generating city supply dashboard...")
    viz.plot_city_supply_dashboard()
    plt.savefig('city_supply_dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Generating correlation heatmap...")
    viz.plot_correlation_heatmap()
    plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Generating full dashboard...")
    viz.generate_full_dashboard(save_path='full_dashboard.png')
    plt.close()
    
    print("\nVisualizations saved:")
    print("  - price_distribution.png")
    print("  - city_supply_dashboard.png")
    print("  - correlation_heatmap.png")
    print("  - full_dashboard.png")
    print()
    
    # Step 4: Export Summary Statistics
    print("STEP 4: Exporting Summary Statistics...")
    print("-" * 60)
    city_summary = processed_data.groupby('city').agg({
        'realSum': ['mean', 'median', 'std', 'count'],
        'guest_satisfaction_overall': 'mean',
        'host_is_superhost': 'mean',
        'person_capacity': 'mean',
        'bedrooms': 'mean'
    }).round(2)
    
    city_summary.columns = ['avg_price', 'median_price', 'price_std', 'listing_count',
                           'avg_satisfaction', 'superhost_pct', 'avg_capacity', 'avg_bedrooms']
    city_summary = city_summary.reset_index()
    city_summary.to_csv('city_summary_statistics.csv', index=False)
    print("City summary statistics exported to 'city_summary_statistics.csv'")
    print()
    
    # Step 5: Business Insights
    print("STEP 5: Business Intelligence Insights...")
    print("-" * 60)
    
    # Calculate key insights
    city_prices = processed_data.groupby('city')['realSum'].mean().sort_values(ascending=False)
    city_supply = processed_data.groupby('city').size().sort_values(ascending=False)
    
    print("\nKEY INSIGHTS:")
    print(f"  Most expensive city: {city_prices.index[0]} (€{city_prices.iloc[0]:.2f})")
    print(f"  Most affordable city: {city_prices.index[-1]} (€{city_prices.iloc[-1]:.2f})")
    print(f"  City with most listings: {city_supply.index[0]} ({city_supply.iloc[0]} listings)")
    print(f"  Weekend premium: {period_analysis['premium_pct']:.2f}%")
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE!")
    print("=" * 60)
    print("\nOutput files generated:")
    print("  - processed_airbnb_data.csv")
    print("  - city_summary_statistics.csv")
    print("  - *.png (visualization files)")
    print("\nFor detailed analysis, see: airbnb_analysis.ipynb")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error running analysis: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

