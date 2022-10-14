import os
from enum import Enum


class FileTypes(Enum):
    CSV = 'csv'
    XLSX = 'xlsx'
    XLS = 'xls'


PRIORITIES = ['L', 'C', 'H', 'M']

MIN_TOTAL_PROFIT = int(os.environ.get('MIN_TOTAL_PROFIT', 1000))
MAX_TOTAL_COST = int(os.environ.get('MAX_TOTAL_COST', 5000000))

REGION_COUNTRIES = {
    'Sub-Saharan Africa': ['Chad', 'Democratic Republic of the Congo', 'South Africa', 'Eritrea', 'Zambia', 'Mauritius ', 'Ghana', 'Guinea', 'Malawi', 'Seychelles ', 'Madagascar', 'Benin', 'Senegal', 'Mauritania', 'Central African Republic', 'Niger', 'Ethiopia', 'Swaziland', 'Zimbabwe', 'Burkina Faso', 'Sao Tome and Principe', 'Mali', 'Botswana', 'Lesotho', 'Togo', 'Sudan', 'Namibia', 'Kenya', 'The Gambia', 'Rwanda', 'Uganda', 'Mozambique', 'Djibouti', 'Angola', 'Tanzania', 'Comoros', 'Cameroon', 'Nigeria', 'Burundi', 'Sierra Leone', 'Equatorial Guinea', 'Cape Verde', 'Liberia', 'Gabon', 'Republic of the Congo', 'South Sudan', 'Guinea-Bissau', "Cote d'Ivoire"],
    'Europe': ['Latvia', 'Czech Republic', 'Bosnia and Herzegovina', 'Germany', 'Vatican City', 'Lithuania', 'Ukraine', 'Russia', 'Liechtenstein', 'Greece', 'Albania', 'Andorra', 'Switzerland', 'San Marino', 'Serbia', 'Italy', 'Bulgaria', 'Poland', 'France', 'Slovenia', 'Spain', 'Moldova ', 'Luxembourg', 'Georgia', 'Iceland', 'Montenegro', 'Estonia', 'Hungary', 'Austria', 'Sweden', 'Portugal', 'Armenia', 'Netherlands', 'United Kingdom', 'Macedonia', 'Malta', 'Slovakia', 'Finland', 'Cyprus', 'Norway', 'Denmark', 'Croatia', 'Belarus', 'Romania', 'Ireland', 'Belgium', 'Kosovo', 'Monaco'],
    'Middle East and North Africa': ['Pakistan', 'Algeria', 'Lebanon', 'Azerbaijan', 'Turkey', 'Somalia', 'Kuwait', 'Oman', 'Libya', 'Tunisia ', 'Morocco', 'Iran', 'Iraq', 'Syria', 'United Arab Emirates', 'Afghanistan', 'Saudi Arabia', 'Israel', 'Egypt', 'Yemen', 'Qatar', 'Jordan', 'Bahrain'],
    'Asia': ['Laos', 'China', 'India', 'Japan', 'Bangladesh', 'Bhutan', 'Sri Lanka', 'Cambodia', 'Taiwan', 'Indonesia', 'North Korea', 'Myanmar', 'Singapore', 'Thailand', 'Nepal', 'Mongolia', 'Tajikistan', 'Brunei', 'Kyrgyzstan', 'Uzbekistan', 'Vietnam', 'Maldives', 'Turkmenistan', 'Philippines', 'Kazakhstan', 'South Korea', 'Malaysia'],
    'Central America and the Caribbean': ['Haiti', 'Cuba', 'Dominica', 'Trinidad and Tobago', 'Nicaragua', 'Jamaica', 'Dominican Republic', 'Saint Lucia', 'Antigua and Barbuda ', 'Barbados', 'Honduras', 'Saint Kitts and Nevis ', 'Guatemala', 'Belize', 'Saint Vincent and the Grenadines', 'El Salvador', 'The Bahamas', 'Panama', 'Costa Rica', 'Grenada'],
    'Australia and Oceania': ['Palau', 'Federated States of Micronesia', 'Australia', 'Samoa ', 'Tuvalu', 'Papua New Guinea', 'New Zealand', 'Tonga', 'Kiribati', 'East Timor', 'Nauru', 'Vanuatu', 'Marshall Islands', 'Fiji', 'Solomon Islands'],
    'North America': ['United States of America', 'Canada', 'Greenland', 'Mexico']
}

ISSUES = {
    'region_country_mismatch': 'Region and Country mismatch on row: {}',
    'priority_not_exists': 'Priority value does not exists in the customer\'s MDM system on row: {}',
    'min_total_profit': 'Total Profit value should be not less than {} on row: {}',
    'max_total_cost': 'Total Cost value should be not bigger than {} on row: {}',
    'wrong_dates': 'Order Date should be less than Ship Date on row: {}',
    'wrong_total_revenue': 'Total Revenue value is wrong on row: {}',
    'wrong_total_cost': 'Total Cost value is wrong on row: {}',
}

DTYPES = {
    'Region': 'string',
    'Country': 'string',
    'Item Type': 'string',
    'Sales Channel': 'string',
    'Order Priority': 'string',
    'Order Date': 'string',
    'Order ID': 'int',
    'Ship Date': 'string',
    'Units Sold': 'int',
    'Unit Price': 'float',
    'Unit Cost': 'float',
    'Total Revenue': 'float',
    'Total Cost': 'float',
    'Total Profit': 'float'
}
