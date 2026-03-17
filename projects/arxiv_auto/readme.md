# 项目介绍

# 运行


## Mysql添加
```
CREATE TABLE arxiv_cs_lg (
    id INT AUTO_INCREMENT PRIMARY KEY,
    authors TEXT,
    categories TEXT,
    comment TEXT,
    doi VARCHAR(255),
    entry_id VARCHAR(255),
    journal_ref VARCHAR(255),
    links TEXT,
    primary_category VARCHAR(255),
    published DATETIME,
    summary TEXT,
    title VARCHAR(255),
    updated DATETIME,
    CN_title VARCHAR(255),
    CN_summary TEXT
);
```

## TODO: fix
1. 由于数据库架构问题，重复收录paper于不同的数据库中，比如一个文章同时属于cs.AI和cs.CR，则会同时收录在两个数据库中

