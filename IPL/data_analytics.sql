-- 1. Total runs scored by team
select
    batting_team,
    sum(total_runs) as total_runs
from
    deliveries
group by
    batting_team
order by
    total_runs desc;

-- 2. Top batsman for Royal Challengers Bangalore
select
    batsman,
    sum(total_runs) as total_runs
from
    deliveries
where
    batting_team = 'Royal Challengers Bangalore'
group by
    batsman
order by
    total_runs desc
limit
    10;

-- 3. Foreign umpire analysis
select
    country,
    count(*) as umpire_count
from
    umpires
where
    country != ' India'
group by
    country
order by
    umpire_count 
    
-- 4. Stacked chart of matches played by team by season
select
    team,
    season,
    sum(count) as Matches_Played
from
    (
        select
            team1 as team,
            season,
            count(*)
        from
            matches
        group by
            team1,
            season
        union
        select
            team2 as team,
            season,
            count(*)
        from
            matches
        group by
            team2,
            season
        order by
            team,
            season
    ) as team
group by
    team,
    season 
    
-- 5. Number of matches won per team per year in IPL.
select
    winner,
    season,
    count(*)
from
    matches
group by
    winner,
    season
order by
    winner,
    season;

-- 6. Number of matches played per year for all the years in IPL.
select
    team1 as team,
    count(*) as Matches_Played
from
    matches
group by
    team1
union
select
    team2 as team,
    count(*) as Matches_Played
from
    matches
group by
    team2
order by
    Matches_Played desc 
-- 7. Extra runs conceded per team in the year 2016
select
    bowling_team,
    sum(extra_runs) as Extra_runs_conceeded
from
    deliveries
where
    match_id in (
        select
            id
        from
            matches
        where
            season = '2016'
    )
group by
    bowling_team
order by
    Extra_runs_conceeded desc,
    bowling_team 
    
-- 8. Top 10 economical bowlers in the year 2015
select
    bowler,
    round((sum(total_runs) /(count(*) * 1.0)) * 6, 2) as "Top 10 Economical_Bowlers"
from
    deliveries
where
    match_id in (
        select
            id
        from
            matches
        where
            season = '2015'
    )
group by
    bowler
order by
    "Top 10 Economical_Bowlers" asc,
    bowler
limit
    10