-- A/B Test Metrics
-- Compute conversion rate per experiment group

SELECT
    group_name,
    COUNT(*) AS total_users,
    SUM(converted) AS converted_users,
    ROUND(SUM(converted) * 1.0 / COUNT(*), 4) AS conversion_rate
FROM ab_test_data
GROUP BY group_name;

