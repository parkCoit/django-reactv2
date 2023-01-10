# create table users(
#     user_id binary(16) primary key,
#     user_email varchar(20),
#     password varchar(20),
#     user_name varchar(20),
#     phone varchar(20),
#     birth varchar(20),
#     address varchar(20),
#     job varchar(20),
#     user_interests varchar(20),
#     token varchar(20),
#     create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
#     updated_at DATETIME DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
# )charset = utf8;
#
# create table articles(
#     art_seq int primary key AUTO_INCREMENT,
#     title varchar(100),
#     content varchar(1000),
#     create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
#     updated_at DATETIME DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
#     user_id binary(16), foreign key (user_id) REFERENCES users (user_id) on update cascade on delete cascade
# )charset = utf8;