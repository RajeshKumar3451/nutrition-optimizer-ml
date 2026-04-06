import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)

class NutritionPreprocessor:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def remove_duplicates(self):
        initial_count = len(self.df)
        self.df.drop_duplicates(inplace=True)
        logger.info(f"Removed {initial_count - len(self.df)} duplicate rows.")
        return self

    def handle_missing_values(self):
        # Using Median for numerical columns to stay robust
        cols_to_fix = ['protein_intake_g', 'calorie_deficit', 'weight_loss_kg']
        for col in cols_to_fix:
            median_val = self.df[col].median()
            self.df[col] = self.df[col].fillna(median_val)
        logger.info("Missing values imputed with median.")
        return self

    def filter_outliers_iqr(self, column: str):
        """Removes outliers using the IQR method."""
        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        self.df = self.df[(self.df[column] >= lower_bound) & (self.df[column] <= upper_bound)]
        logger.info(f"Outliers removed for {column}.")
        return self

    def get_clean_data(self) -> pd.DataFrame:
        return self.df