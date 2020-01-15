DROP TABLE hwnorm1c;
CREATE TABLE hwnorm1c (
 key VARCHAR(100)  NOT NULL,
 data TEXT NOT NULL
);
.separator "\t"
.import hwnorm1c_sql_input.txt hwnorm1c
create index datum on hwnorm1c(key);
pragma table_info (ap);
select count(*) from hwnorm1c;
.exit
