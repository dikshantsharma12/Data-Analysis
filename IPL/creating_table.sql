Create table matches(
    id integer,
    season varchar(100),
    city varchar(100),
    date DATE,
    team1 varchar(100),
    team2 varchar(100),
    toss_winner varchar(100),
    toss_decision varchar(100),
    result varchar(100),
    dl_applied int,
    winner varchar(100),
    win_by_runs int,
    win_by_wickets int,
    player_of_match varchar(100),
    venue varchar(100),
    umpire1 varchar(100),
    umpire2 varchar(100),
    umpire3 varchar(100),
    primary key (id)
);

\ COPY matches
FROM
    '/home/dikshant/_/matches.csv' DELIMITER ',' CSV HEADER;

create table deliveries (
    match_id integer,
    inning integer,
    batting_team varchar(100),
    bowling_team varchar(100),
    over integer,
    ball integer,
    batsman varchar(100),
    non_striker varchar(100),
    bowler varchar(100),
    is_super_over integer,
    wide_runs integer,
    bye_runs integer,
    legbye_runs integer,
    noball_runs integer,
    penalty_runs integer,
    batsman_runs integer,
    extra_runs integer,
    total_runs integer,
    player_dismissed varchar(100),
    dismissal_kind varchar(100),
    fielder varchar(100),
    primary key(match_id, inning, over, ball),
    foreign key(match_id) references matches(id)
);

\ COPY deliveries
FROM
    '/home/dikshant/_/deliveries.csv' DELIMITER ',' CSV HEADER;