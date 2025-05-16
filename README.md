# aws-data-engineering
The course for AWS data engineering

## Job Bookmarks
feature of ETL jobs to track already processed data  

## Glue Databrew
automate data validation and preparation using UI/ also can custom python scripts.

## Schema Registry vs Data catalog
scheme constistency for streaming data(by kafka)  
Data catalog - for defining strcuture of data.

## Cross account access to S3 data
use bucket based policy or resouce based policy with specific account id

## Difference between LSI and GSI
Partition key - LSI(same) - GSI(can be different)  
sort Key = both different  
created time : LSI(during table creation) GSI(can be created/deleted any time)  
consistency: LSI(string) ; GSI(eventually consistent)  
provisined throughput: LSI(same as base table) ; GSI(separete from base table)  
number allowed: LSI(5): GSI(20- can increase)  

## Type of key
Partition Key - HASH  
Sort Key - Range Key  

## Improve performance of your query by:
compressing , partitioninng and converting into columnar format (like parquet)

## Upto 10 Petebyte tranfer
snowball edge: there is no way to put in glacier. You need to place in other place and move it to glacier.  

## for lifecycle transition
you need to store for 30 days min

## Formula to calculate the partition in dynamodb
Number of partitions = max(ceil(Table size (GB) / 10), ceil(WCU / 1000), ceil(RCU / 3000))

## Kinesis components
Kinesis Data Streams (KDS): Real-time streaming of data (shards, producers, consumers).  
Kinesis Data Firehose: Loads streaming data into S3, Redshift, Elasticsearch, or Splunk (no code, auto-scaling).  
Kinesis Data Analytics: Real-time analytics on streaming data using SQL.  

## Kinesis Firehose - auto managed
can not be two source (data stream and  Kinesis Agent at a same time)

## s3 VPC gateway endpoint
connect s3 to vpc with out public internet

## Connect VPC to AWS services
1. VPC gateway endpoint
used by s3 and dynamodb - use route table

2. VPC Interface endpoint (AWS PrivateLink)
used by other services by using elasctic network interface.  

## Encrption in s3
metadata are not encrypted

## Avro vs Parquet
Avro - row based, optimized for writing
parquet - column based, optmized for analytical operations

## Apache Hive
Open source data warehouse ystem built in top of Hadoop  
It allows you to query and manage large datasets stored in distributed storage using a SQL-like language called HiveQL. 
Hive organize data into tables and partitions(folders) and store metadatas (like table schema and partition info in a metastore - which is a database)
Hive can read data in many formats: text, CSV, JSON, Parquet, ORC, Avro, etc.
It lets you run SQL-like queries (HiveQL) on large datasets stored in distributed storage (like HDFS or S3).
Hive translates SQL queries into MapReduce, Tez, or Spark jobs to process data at scale.
The Hive Metastore is just a metadata catalog—other tools (like Athena, Presto, Spark) can use it to understand how to read the data.

## AWS Athena
Data Catalog: tores metadata: table names, columns, partitions, file locations, etc.  - use to find where and how to queries data in s3.  
Athena use catalog for metadata but it actually scan s3 for queries  
you do not pay for data returned but you pay for data scanned  


## Big Data Technologies Summary

| Technology   | Type           | One-line Description                                   | Common Uses                        |
|--------------|----------------|-------------------------------------------------------|-------------------------------------|
| Hadoop       | Framework      | Distributed storage and batch processing of big data   | Batch ETL, data lakes               |
| Spark        | Engine         | Fast, in-memory analytics and processing               | Real-time analytics, ML, ETL        |
| Hive         | SQL Engine     | SQL-like queries on large datasets over Hadoop         | Data warehousing, batch analytics   |
| Presto/Trino | SQL Engine     | Distributed, interactive SQL queries on big data       | Ad hoc analytics, federated queries |
| HBase        | NoSQL Database | Scalable, distributed, real-time NoSQL database        | Time-series, random access storage  |
| Parquet      | File Format    | Columnar storage format optimized for analytics        | Efficient storage, fast queries     |
| Avro         | File Format    | Row-based storage format, good for streaming           | Data serialization, streaming       |
| ORC          | File Format    | Columnar storage format, often used with Hive          | Data warehousing, analytics         |

## AWS Data exchange  
AWS Data Exchange is a fully managed AWS service that enables you to find, subscribe to, and use third-party data in the AWS Cloud. It acts as a marketplace for data products, allowing data providers to publish datasets and data subscribers to access and integrate those datasets directly into their AWS environment (typically delivered to Amazon S3).