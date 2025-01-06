create table actors
(
    id         integer
        constraint actors_pk
            primary key autoincrement,
    first_name varchar(255) not null,
    last_name  varchar(255) not null
);

