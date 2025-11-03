"""
Data Visualization Module for Airbnb Analysis
Business Intelligence Engineer - Visualization Dashboard
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import Optional, List, Tuple


class AirbnbVisualizations:
    """Collection of visualization functions for Airbnb data analysis"""
    
    def __init__(self, df: pd.DataFrame, style: str = 'seaborn-v0_8-darkgrid'):
        """
        Initialize visualization class
        
        Args:
            df: Processed DataFrame
            style: Matplotlib style
        """
        self.df = df
        plt.style.use(style)
        sns.set_palette("husl")
    
    def plot_price_distribution_by_city(self, figsize: Tuple[int, int] = (14, 8)):
        """Box plot of price distribution by city"""
        plt.figure(figsize=figsize)
        df_sorted = self.df.sort_values('realSum')
        sns.boxplot(data=df_sorted, x='city', y='realSum', palette='Set2')
        plt.title('Price Distribution by City', fontsize=16, fontweight='bold')
        plt.xlabel('City', fontsize=12)
        plt.ylabel('Price (realSum)', fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        return plt
    
    def plot_room_type_analysis(self, figsize: Tuple[int, int] = (14, 6)):
        """Room type distribution and pricing"""
        fig, axes = plt.subplots(1, 2, figsize=figsize)
        
        # Pie chart
        room_counts = self.df['room_type'].value_counts()
        axes[0].pie(room_counts.values, labels=room_counts.index, 
                   autopct='%1.1f%%', startangle=90)
        axes[0].set_title('Room Type Distribution', fontsize=14, fontweight='bold')
        
        # Box plot
        sns.boxplot(data=self.df, x='room_type', y='realSum', ax=axes[1])
        axes[1].set_title('Price by Room Type', fontsize=14, fontweight='bold')
        axes[1].set_xlabel('Room Type')
        axes[1].set_ylabel('Price')
        
        plt.tight_layout()
        return plt
    
    def plot_city_supply_dashboard(self, figsize: Tuple[int, int] = (16, 12)):
        """Comprehensive city supply analysis dashboard"""
        fig, axes = plt.subplots(2, 2, figsize=figsize)
        
        # Average price by city
        city_price = self.df.groupby('city')['realSum'].mean().sort_values(ascending=False)
        axes[0, 0].barh(city_price.index, city_price.values, color='steelblue')
        axes[0, 0].set_title('Average Price by City', fontsize=12, fontweight='bold')
        axes[0, 0].set_xlabel('Average Price')
        
        # Listing count by city
        city_count = self.df.groupby('city').size().sort_values(ascending=False)
        axes[0, 1].bar(city_count.index, city_count.values, color='coral')
        axes[0, 1].set_title('Number of Listings by City', fontsize=12, fontweight='bold')
        axes[0, 1].set_xlabel('City')
        axes[0, 1].set_ylabel('Count')
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # Superhost percentage
        superhost_pct = self.df.groupby('city')['host_is_superhost'].mean() * 100
        axes[1, 0].bar(superhost_pct.index, superhost_pct.values, color='green')
        axes[1, 0].set_title('Superhost Percentage by City', fontsize=12, fontweight='bold')
        axes[1, 0].set_xlabel('City')
        axes[1, 0].set_ylabel('Percentage (%)')
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # Average satisfaction
        satisfaction = self.df.groupby('city')['guest_satisfaction_overall'].mean().sort_values(ascending=False)
        axes[1, 1].barh(satisfaction.index, satisfaction.values, color='purple')
        axes[1, 1].set_title('Average Guest Satisfaction by City', fontsize=12, fontweight='bold')
        axes[1, 1].set_xlabel('Average Satisfaction Score')
        
        plt.tight_layout()
        return plt
    
    def plot_correlation_heatmap(self, figsize: Tuple[int, int] = (12, 10)):
        """Correlation matrix heatmap"""
        numeric_cols = ['realSum', 'person_capacity', 'bedrooms', 'cleanliness_rating',
                        'guest_satisfaction_overall', 'dist', 'metro_dist',
                        'attr_index_norm', 'rest_index_norm', 'price_per_person', 'location_score']
        
        available_cols = [col for col in numeric_cols if col in self.df.columns]
        correlation_matrix = self.df[available_cols].corr()
        
        plt.figure(figsize=figsize)
        sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm',
                   center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
        plt.title('Feature Correlation Matrix', fontsize=16, fontweight='bold')
        plt.tight_layout()
        return plt
    
    def plot_period_comparison(self, figsize: Tuple[int, int] = (18, 5)):
        """Weekend vs weekday comparison"""
        fig, axes = plt.subplots(1, 3, figsize=figsize)
        
        # Price comparison
        sns.boxplot(data=self.df, x='period', y='realSum', ax=axes[0])
        axes[0].set_title('Price: Weekday vs Weekend', fontsize=12, fontweight='bold')
        
        # Satisfaction comparison
        sns.boxplot(data=self.df, x='period', y='guest_satisfaction_overall', ax=axes[1])
        axes[1].set_title('Satisfaction: Weekday vs Weekend', fontsize=12, fontweight='bold')
        
        # Listing count
        period_count = self.df['period'].value_counts()
        axes[2].bar(period_count.index, period_count.values, color=['skyblue', 'lightcoral'])
        axes[2].set_title('Listing Count by Period', fontsize=12, fontweight='bold')
        axes[2].set_ylabel('Count')
        
        plt.tight_layout()
        return plt
    
    def plot_market_segmentation(self, figsize: Tuple[int, int] = (14, 8)):
        """Market segmentation by price segment"""
        fig, axes = plt.subplots(1, 2, figsize=figsize)
        
        # Price segment distribution
        segment_dist = self.df['price_segment'].value_counts()
        axes[0].bar(segment_dist.index, segment_dist.values, color=['green', 'orange', 'red'])
        axes[0].set_title('Price Segment Distribution', fontsize=12, fontweight='bold')
        axes[0].set_xlabel('Price Segment')
        axes[0].set_ylabel('Count')
        
        # Price segment vs satisfaction
        sns.boxplot(data=self.df, x='price_segment', y='guest_satisfaction_overall', ax=axes[1])
        axes[1].set_title('Satisfaction by Price Segment', fontsize=12, fontweight='bold')
        axes[1].set_xlabel('Price Segment')
        axes[1].set_ylabel('Satisfaction Score')
        
        plt.tight_layout()
        return plt
    
    def plot_location_analysis(self, figsize: Tuple[int, int] = (14, 6)):
        """Location quality impact on pricing"""
        fig, axes = plt.subplots(1, 2, figsize=figsize)
        
        # Location quality distribution
        location_dist = self.df['location_quality'].value_counts()
        axes[0].bar(location_dist.index, location_dist.values, color=['red', 'yellow', 'green'])
        axes[0].set_title('Location Quality Distribution', fontsize=12, fontweight='bold')
        axes[0].set_xlabel('Location Quality')
        axes[0].set_ylabel('Count')
        
        # Location quality vs price
        sns.boxplot(data=self.df, x='location_quality', y='realSum', ax=axes[1])
        axes[1].set_title('Price by Location Quality', fontsize=12, fontweight='bold')
        axes[1].set_xlabel('Location Quality')
        axes[1].set_ylabel('Price')
        
        plt.tight_layout()
        return plt
    
    def generate_full_dashboard(self, save_path: Optional[str] = None):
        """Generate complete dashboard with all visualizations"""
        # Create figure with subplots
        fig = plt.figure(figsize=(20, 16))
        gs = fig.add_gridspec(4, 3, hspace=0.3, wspace=0.3)
        
        # 1. Price distribution by city
        ax1 = fig.add_subplot(gs[0, :])
        df_sorted = self.df.sort_values('realSum')
        sns.boxplot(data=df_sorted, x='city', y='realSum', ax=ax1, palette='Set2')
        ax1.set_title('Price Distribution by City', fontsize=14, fontweight='bold')
        ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')
        
        # 2. Room type distribution
        ax2 = fig.add_subplot(gs[1, 0])
        room_counts = self.df['room_type'].value_counts()
        ax2.pie(room_counts.values, labels=room_counts.index, autopct='%1.1f%%', startangle=90)
        ax2.set_title('Room Type Distribution', fontsize=12, fontweight='bold')
        
        # 3. Average price by city
        ax3 = fig.add_subplot(gs[1, 1])
        city_price = self.df.groupby('city')['realSum'].mean().sort_values(ascending=False)
        ax3.barh(range(len(city_price)), city_price.values, color='steelblue')
        ax3.set_yticks(range(len(city_price)))
        ax3.set_yticklabels(city_price.index)
        ax3.set_title('Average Price by City', fontsize=12, fontweight='bold')
        ax3.set_xlabel('Average Price')
        
        # 4. Listing count
        ax4 = fig.add_subplot(gs[1, 2])
        city_count = self.df.groupby('city').size().sort_values(ascending=False)
        ax4.bar(range(len(city_count)), city_count.values, color='coral')
        ax4.set_xticks(range(len(city_count)))
        ax4.set_xticklabels(city_count.index, rotation=45, ha='right')
        ax4.set_title('Listings by City', fontsize=12, fontweight='bold')
        ax4.set_ylabel('Count')
        
        # 5. Weekend vs Weekday
        ax5 = fig.add_subplot(gs[2, 0])
        sns.boxplot(data=self.df, x='period', y='realSum', ax=ax5)
        ax5.set_title('Price: Weekday vs Weekend', fontsize=12, fontweight='bold')
        
        # 6. Superhost percentage
        ax6 = fig.add_subplot(gs[2, 1])
        superhost_pct = self.df.groupby('city')['host_is_superhost'].mean() * 100
        ax6.bar(range(len(superhost_pct)), superhost_pct.values, color='green')
        ax6.set_xticks(range(len(superhost_pct)))
        ax6.set_xticklabels(superhost_pct.index, rotation=45, ha='right')
        ax6.set_title('Superhost % by City', fontsize=12, fontweight='bold')
        ax6.set_ylabel('Percentage (%)')
        
        # 7. Satisfaction by city
        ax7 = fig.add_subplot(gs[2, 2])
        satisfaction = self.df.groupby('city')['guest_satisfaction_overall'].mean().sort_values(ascending=False)
        ax7.barh(range(len(satisfaction)), satisfaction.values, color='purple')
        ax7.set_yticks(range(len(satisfaction)))
        ax7.set_yticklabels(satisfaction.index)
        ax7.set_title('Avg Satisfaction by City', fontsize=12, fontweight='bold')
        ax7.set_xlabel('Satisfaction Score')
        
        # 8. Correlation heatmap
        ax8 = fig.add_subplot(gs[3, :])
        numeric_cols = ['realSum', 'person_capacity', 'bedrooms', 'cleanliness_rating',
                        'guest_satisfaction_overall', 'dist', 'attr_index_norm', 
                        'rest_index_norm', 'price_per_person']
        available_cols = [col for col in numeric_cols if col in self.df.columns]
        corr_matrix = self.df[available_cols].corr()
        sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0,
                   ax=ax8, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
        ax8.set_title('Feature Correlation Matrix', fontsize=14, fontweight='bold')
        
        plt.suptitle('Airbnb Supply Analysis - Comprehensive Dashboard', 
                    fontsize=18, fontweight='bold', y=0.995)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Dashboard saved to {save_path}")
        
        return plt


if __name__ == "__main__":
    # Example usage
    import sys
    
    try:
        df = pd.read_csv('processed_airbnb_data.csv')
        viz = AirbnbVisualizations(df)
        
        # Generate individual plots
        viz.plot_price_distribution_by_city()
        plt.savefig('price_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        viz.plot_city_supply_dashboard()
        plt.savefig('city_supply_dashboard.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # Generate full dashboard
        viz.generate_full_dashboard(save_path='full_dashboard.png')
        plt.close()
        
        print("Visualizations generated successfully!")
        
    except FileNotFoundError:
        print("Processed data file not found. Please run ETL pipeline first.")

