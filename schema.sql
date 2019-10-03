-- customersテーブルがあったら削除する
drop table IF EXISTS customers;

-- customersテーブルを作る
create TABLE customers (
    name TEXT,
    age INTEGER
);

-- 初期データをいくつかいれる（わかりやすいから）
insert into
    customers
values
    ('Bob', 15),
    ('Tom', 57),
    ('Ken', 73)
;