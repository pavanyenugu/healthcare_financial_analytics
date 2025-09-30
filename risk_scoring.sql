-- Example SQL for risk scoring (simplified HCC logic)
SELECT 
    patient_id,
    SUM(
        CASE 
            WHEN diagnosis_code IN ('E11', 'E10') THEN 1.2  -- Diabetes
            WHEN diagnosis_code IN ('I10', 'I11') THEN 0.8  -- Hypertension
            WHEN diagnosis_code IN ('J44') THEN 1.5         -- COPD
            ELSE 0
        END
    ) AS risk_score
FROM diagnoses
GROUP BY patient_id;
