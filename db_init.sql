create database djangotest;
create user test@localhost identified by "testing321";
grant all on djangotest.* to test@localhost;