# Customer-Experience-Analytics-for-Fintech-Apps — Week 2

Project: Customer experience analytics pipelines, experiments and visualizations for fintech mobile/web apps.  
This repository contains code, notebooks and documentation for Week 2 analysis tasks

## Used structure
.
├── README.md 
├── notebooks/
│   ├── preprocessing_EDA.ipynb

│   ├── sentiment_analysis.ipynb

│   ├── insert_into_tables.ipynb

│   └── display_results.ipynb

├── scripts/

│   ├── config.py

│   ├── preprocessing.py

│   ├── scraper.py

│   └── sentiment_utils.py

│   └── load_data.py

├── requirements.txt

├── sql/

│   ├── schema.sql


## Quickstart
1. Clone repository
     git clone <repo-url>
2. Create environment
3. Creating Scripts folder and creating the necessary .py files to include classes and functions involved in scraping and preprocessing.
4. Creating notebooks folder to create the EDA notebook for exploring the data and necessary visualizations.


## Branches
| Branch     | Purpose                                |
| ---------- | -------------------------------------- |
| **task-1** | Data scraping & preprocessing          |
| **task-2** | Sentiment analysis + thematic clusters |
| **task-3** | Database creation + data insertion     |


## Key Deliverables 

Scraped customer reviews from fintech apps
Cleaned and preprocessed datasets
BERT sentiment classification
Thematic clustering from review text
Postgres database with banks and reviews tables
Visualizations comparing sentiment, ratings, banks, and themes
