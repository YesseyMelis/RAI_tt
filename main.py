from typing import BinaryIO, List
import pandas as pd

from constants import *


def read_file(file_data: BinaryIO):
    if FileTypes.CSV.value in file_data.name:
        df = pd.read_csv(
            file_data,
            dtype=DTYPES,
            parse_dates=['Order Date', 'Ship Date'],
        )
        return df
    elif FileTypes.XLSX.value in file_data.name or FileTypes.XLS.value in file_data.name:
        df = pd.read_excel(
            file_data,
            dtype=DTYPES,
            parse_dates=['Order Date', 'Ship Date']
        )
        return df


def validate_dataset(dataset) -> List[str]:
    issues = []
    for index, row in dataset.iterrows():
        index += 2
        if row['Country'] not in REGION_COUNTRIES.get(row['Region']):
            issues.append(ISSUES.get('region_country_mismatch').format(*[index]))
        if row['Order Priority'] not in PRIORITIES:
            issues.append(ISSUES.get('priority_not_exists').format(*[index]))
        if row['Total Profit'] < MIN_TOTAL_PROFIT:
            issues.append(ISSUES.get('min_total_profit').format(*[MIN_TOTAL_PROFIT, index]))
        if row['Total Cost'] > MAX_TOTAL_COST:
            issues.append(ISSUES.get('max_total_cost').format(*[MAX_TOTAL_COST, index]))
        if row['Order Date'] > row['Ship Date']:
            issues.append(ISSUES.get('wrong_dates').format(*[index]))
        revenue = round(row['Units Sold'] * row['Unit Price'], 2)
        if revenue != row['Total Revenue']:
            issues.append(ISSUES.get('wrong_total_revenue').format(*[index]))
        cost = round(row['Units Sold'] * row['Unit Cost'], 2)
        if cost != row['Total Cost']:
            issues.append(ISSUES.get('wrong_total_cost').format(*[index]))
    return issues
