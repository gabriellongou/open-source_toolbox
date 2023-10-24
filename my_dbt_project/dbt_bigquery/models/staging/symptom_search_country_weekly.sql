WITH source AS (

    SELECT * FROM {{ source('covid19_symptom_search', 'symptom_search_country_weekly') }}

)

SELECT
    country_region,
    date,
    symptom_depression,
    symptom_fatigue,
    symptom_headache
FROM source