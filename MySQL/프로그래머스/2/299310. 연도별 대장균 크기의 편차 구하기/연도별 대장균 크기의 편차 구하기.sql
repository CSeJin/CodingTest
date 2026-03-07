-- 코드를 작성해주세요
SELECT E2.YEAR,
        (E2.MAX_SIZE-E.SIZE_OF_COLONY) AS YEAR_DEV,
        E.ID
FROM ECOLI_DATA E, (select year(differentiation_date) as 'YEAR',
                            max(size_of_colony) as 'MAX_SIZE'
                    from ecoli_data
                    GROUP BY YEAR) E2
where e2.year = year(e.differentiation_date)
order by year, year_dev;