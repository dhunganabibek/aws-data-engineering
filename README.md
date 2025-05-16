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