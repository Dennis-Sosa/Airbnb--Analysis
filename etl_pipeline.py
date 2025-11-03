"""
ETL Pipeline for Airbnb Data
Business Intelligence Engineer - Data Processing Module
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import List, Dict, Tuple
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AirbnbETLPipeline:
    """ETL Pipeline for processing Airbnb listing data"""
    
    def __init__(self, data_dir: str, cities: List[str], periods: List[str]):
        """
        Initialize ETL Pipeline
        
        Args:
            data_dir: Directory containing CSV files
            cities: List of city names
            periods: List of time periods (weekdays, weekends)
        """
        self.data_dir = Path(data_dir)
        self.cities = cities
        self.periods = periods
        self.raw_data = None
        self.processed_data = None
        
    def extract(self) -> pd.DataFrame:
        """
        Extract: Load data from CSV files
        
        Returns:
            Combined DataFrame with all city data
        """
        logger.info("Starting data extraction...")
        all_data = []
        
        for city in self.cities:
            for period in self.periods:
                file_path = self.data_dir / f"{city}_{period}.csv"
                if file_path.exists():
                    try:
                        df = pd.read_csv(file_path)
                        df['city'] = city.capitalize()
                        df['period'] = period
                        all_data.append(df)
                        logger.info(f"Loaded {city}_{period}.csv: {len(df)} records")
                    except Exception as e:
                        logger.error(f"Error loading {file_path}: {e}")
                else:
                    logger.warning(f"File not found: {file_path}")
        
        if not all_data:
            raise ValueError("No data files found!")
        
        combined_df = pd.concat(all_data, ignore_index=True)
        self.raw_data = combined_df
        logger.info(f"Extraction complete. Total records: {len(combined_df)}")
        return combined_df
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Transform: Clean and preprocess data
        
        Args:
            df: Raw DataFrame
            
        Returns:
            Cleaned and transformed DataFrame
        """
        logger.info("Starting data transformation...")
        df_clean = df.copy()
        
        # Remove unnamed index column
        if 'Unnamed: 0' in df_clean.columns:
            df_clean = df_clean.drop('Unnamed: 0', axis=1)
        
        # Handle missing values
        numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            if df_clean[col].isnull().sum() > 0:
                fill_value = df_clean[col].median()
                df_clean[col].fillna(fill_value, inplace=True)
                logger.info(f"Filled {df_clean[col].isnull().sum()} missing values in {col} with median: {fill_value}")
        
        # Ensure boolean columns are properly formatted
        bool_cols = ['room_shared', 'room_private', 'host_is_superhost', 'multi', 'biz']
        for col in bool_cols:
            if col in df_clean.columns:
                df_clean[col] = df_clean[col].astype(bool)
        
        # Create derived features
        df_clean['price_per_person'] = df_clean['realSum'] / df_clean['person_capacity']
        df_clean['location_score'] = (df_clean['attr_index_norm'] + df_clean['rest_index_norm']) / 2
        
        # Price segmentation
        df_clean['price_segment'] = pd.cut(
            df_clean['realSum'],
            bins=[0, df_clean['realSum'].quantile(0.33), 
                  df_clean['realSum'].quantile(0.67), df_clean['realSum'].max()],
            labels=['Budget', 'Mid-range', 'Premium']
        )
        
        # Location quality
        df_clean['location_quality'] = pd.cut(
            df_clean['location_score'],
            bins=[0, 30, 50, 100],
            labels=['Low', 'Medium', 'High']
        )
        
        self.processed_data = df_clean
        logger.info(f"Transformation complete. Processed {len(df_clean)} records")
        return df_clean
    
    def load(self, df: pd.DataFrame, output_path: str = 'processed_airbnb_data.csv'):
        """
        Load: Save processed data to file
        
        Args:
            df: Processed DataFrame
            output_path: Output file path
        """
        logger.info(f"Saving processed data to {output_path}...")
        df.to_csv(output_path, index=False)
        logger.info(f"Data saved successfully. Shape: {df.shape}")
    
    def run_pipeline(self, output_path: str = None) -> pd.DataFrame:
        """
        Run complete ETL pipeline
        
        Args:
            output_path: Optional path to save processed data
            
        Returns:
            Processed DataFrame
        """
        # Extract
        raw_df = self.extract()
        
        # Transform
        processed_df = self.transform(raw_df)
        
        # Load (optional)
        if output_path:
            self.load(processed_df, output_path)
        
        return processed_df
    
    def get_data_quality_report(self, df: pd.DataFrame) -> Dict:
        """
        Generate data quality report
        
        Args:
            df: DataFrame to analyze
            
        Returns:
            Dictionary with quality metrics
        """
        report = {
            'total_records': len(df),
            'total_columns': len(df.columns),
            'missing_values': df.isnull().sum().to_dict(),
            'duplicate_records': df.duplicated().sum(),
            'data_types': df.dtypes.to_dict(),
            'numeric_summary': df.select_dtypes(include=[np.number]).describe().to_dict() if len(df.select_dtypes(include=[np.number]).columns) > 0 else {}
        }
        
        return report


if __name__ == "__main__":
    # Example usage
    CITIES = ['amsterdam', 'athens', 'barcelona', 'berlin', 'budapest',
              'lisbon', 'london', 'paris', 'rome', 'vienna']
    PERIODS = ['weekdays', 'weekends']
    
    pipeline = AirbnbETLPipeline('.', CITIES, PERIODS)
    processed_data = pipeline.run_pipeline(output_path='processed_airbnb_data.csv')
    
    # Generate quality report
    quality_report = pipeline.get_data_quality_report(processed_data)
    print("\n=== Data Quality Report ===")
    print(f"Total Records: {quality_report['total_records']}")
    print(f"Total Columns: {quality_report['total_columns']}")
    print(f"Duplicate Records: {quality_report['duplicate_records']}")

