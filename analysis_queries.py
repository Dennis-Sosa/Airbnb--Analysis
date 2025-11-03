"""
SQL-like Analysis Queries for Airbnb Data
Business Intelligence Engineer - Analytical Queries Module
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple


class AirbnbAnalytics:
    """Collection of analytical queries similar to SQL operations"""
    
    def __init__(self, df: pd.DataFrame):
        """
        Initialize with DataFrame
        
        Args:
            df: Processed Airbnb DataFrame
        """
        self.df = df
    
    def top_n_cities_by_price(self, n: int = 5) -> pd.DataFrame:
        """
        Query: Top N cities by average price
        
        Equivalent SQL:
        SELECT city, AVG(realSum) as avg_price, 
               MEDIAN(realSum) as median_price, 
               COUNT(*) as listing_count
        FROM listings
        GROUP BY city
        ORDER BY avg_price DESC
        LIMIT N
        """
        result = self.df.groupby('city')['realSum'].agg([
            'mean', 'median', 'count'
        ]).reset_index()
        result.columns = ['city', 'avg_price', 'median_price', 'listing_count']
        result = result.sort_values('avg_price', ascending=False).head(n)
        return result
    
    def room_type_distribution_by_city(self) -> pd.DataFrame:
        """
        Query: Room type distribution by city
        
        Equivalent SQL:
        SELECT city, room_type, COUNT(*) as count
        FROM listings
        GROUP BY city, room_type
        ORDER BY city, count DESC
        """
        result = pd.crosstab(self.df['city'], self.df['room_type'], margins=True)
        return result
    
    def superhost_performance_analysis(self) -> pd.DataFrame:
        """
        Query: Superhost vs regular host performance
        
        Equivalent SQL:
        SELECT host_is_superhost,
               AVG(realSum) as avg_price,
               MEDIAN(realSum) as median_price,
               AVG(guest_satisfaction_overall) as avg_satisfaction,
               AVG(cleanliness_rating) as avg_cleanliness
        FROM listings
        GROUP BY host_is_superhost
        """
        result = self.df.groupby('host_is_superhost').agg({
            'realSum': ['mean', 'median'],
            'guest_satisfaction_overall': 'mean',
            'cleanliness_rating': 'mean',
            'host_is_superhost': 'count'
        }).round(2)
        result.columns = ['avg_price', 'median_price', 'avg_satisfaction', 
                         'avg_cleanliness', 'count']
        return result
    
    def weekend_vs_weekday_pricing(self) -> Dict:
        """
        Query: Weekend vs weekday pricing comparison
        
        Returns dictionary with comparison metrics
        """
        period_stats = self.df.groupby('period')['realSum'].agg([
            'mean', 'median', 'std', 'count'
        ]).round(2)
        
        weekend_avg = period_stats.loc['weekends', 'mean']
        weekday_avg = period_stats.loc['weekdays', 'mean']
        premium = ((weekend_avg - weekday_avg) / weekday_avg) * 100
        
        return {
            'period_stats': period_stats,
            'weekend_avg': weekend_avg,
            'weekday_avg': weekday_avg,
            'premium_pct': premium
        }
    
    def top_products_by_sales(self, n: int = 3) -> pd.DataFrame:
        """
        Query: Top N cities by listing count (analogous to top products)
        
        Equivalent SQL:
        SELECT city, COUNT(*) as listing_count
        FROM listings
        GROUP BY city
        ORDER BY listing_count DESC
        LIMIT N
        """
        result = self.df.groupby('city').size().reset_index(name='listing_count')
        result = result.sort_values('listing_count', ascending=False).head(n)
        return result
    
    def customer_lifetime_value(self, city: str = None) -> pd.DataFrame:
        """
        Query: Highest value cities (analogous to customer lifetime value)
        Based on average price per person and satisfaction
        
        Equivalent SQL:
        SELECT city,
               AVG(realSum / person_capacity) as avg_price_per_person,
               AVG(guest_satisfaction_overall) as avg_satisfaction,
               COUNT(*) as listing_count
        FROM listings
        [WHERE city = ?]
        GROUP BY city
        ORDER BY avg_price_per_person DESC
        """
        query_df = self.df if city is None else self.df[self.df['city'] == city]
        
        result = query_df.groupby('city').agg({
            'price_per_person': 'mean',
            'guest_satisfaction_overall': 'mean',
            'realSum': 'count'
        }).round(2)
        
        result.columns = ['avg_price_per_person', 'avg_satisfaction', 'listing_count']
        result['value_score'] = result['avg_satisfaction'] / result['avg_price_per_person']
        result = result.sort_values('value_score', ascending=False)
        return result
    
    def inventory_analysis(self, threshold_days: int = 30) -> pd.DataFrame:
        """
        Query: Identify cities with supply concerns
        (analogous to inventory with less than threshold supply)
        
        Args:
            threshold_days: Threshold for identifying low supply
        """
        city_stats = self.df.groupby('city').agg({
            'realSum': 'count',
            'person_capacity': 'mean',
            'bedrooms': 'mean'
        }).round(2)
        
        city_stats.columns = ['listing_count', 'avg_capacity', 'avg_bedrooms']
        city_stats['supply_risk'] = city_stats['listing_count'] < city_stats['listing_count'].quantile(0.25)
        
        return city_stats.sort_values('listing_count')
    
    def revenue_by_country_year_month(self, city: str) -> pd.DataFrame:
        """
        Query: Revenue breakdown by city (country proxy) and period
        
        Equivalent SQL:
        SELECT city, period,
               SUM(realSum) as total_revenue,
               AVG(realSum) as avg_price,
               COUNT(*) as listing_count
        FROM listings
        WHERE city = ?
        GROUP BY city, period
        """
        city_df = self.df[self.df['city'] == city]
        result = city_df.groupby(['city', 'period']).agg({
            'realSum': ['sum', 'mean', 'count']
        }).round(2)
        result.columns = ['total_revenue', 'avg_price', 'listing_count']
        return result.reset_index()
    
    def market_segmentation_analysis(self) -> pd.DataFrame:
        """
        Query: Market segmentation by price segment and city
        
        Returns analysis of market positioning
        """
        result = self.df.groupby(['city', 'price_segment']).agg({
            'realSum': ['count', 'mean'],
            'guest_satisfaction_overall': 'mean',
            'location_score': 'mean'
        }).round(2)
        
        result.columns = ['listing_count', 'avg_price', 'avg_satisfaction', 'avg_location_score']
        return result.reset_index()
    
    def correlation_analysis(self, columns: List[str] = None) -> pd.DataFrame:
        """
        Query: Correlation matrix for numeric columns
        
        Args:
            columns: List of columns to analyze (default: key numeric columns)
        """
        if columns is None:
            columns = ['realSum', 'person_capacity', 'bedrooms', 
                      'cleanliness_rating', 'guest_satisfaction_overall',
                      'dist', 'metro_dist', 'attr_index_norm', 
                      'rest_index_norm', 'price_per_person', 'location_score']
        
        available_cols = [col for col in columns if col in self.df.columns]
        return self.df[available_cols].corr()


if __name__ == "__main__":
    # Example usage
    import sys
    
    # Load data
    try:
        df = pd.read_csv('processed_airbnb_data.csv')
        analytics = AirbnbAnalytics(df)
        
        print("=== Top 5 Cities by Price ===")
        print(analytics.top_n_cities_by_price(5))
        
        print("\n=== Weekend vs Weekday Pricing ===")
        result = analytics.weekend_vs_weekday_pricing()
        print(result['period_stats'])
        print(f"Weekend Premium: {result['premium_pct']:.2f}%")
        
        print("\n=== Superhost Performance ===")
        print(analytics.superhost_performance_analysis())
        
    except FileNotFoundError:
        print("Processed data file not found. Please run ETL pipeline first.")

