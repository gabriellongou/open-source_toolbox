{{
    config(
        materialized='model',
        ml_config={
            'model_type': 'ARIMA_PLUS',
            'time_series_timestamp_col': 'date',
            'time_series_data_col': 'symptom_proba',
            'time_series_id_col': ['country_region', 'symptom']
        }
    )
}}

SELECT
  date,
  symptom_proba,
  country_region,
  symptom
FROM
  {{ ref('symptom_search_country_weekly') }}
