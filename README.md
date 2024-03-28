# Ramsey

Open-source and better alternative to [AWS Neptune](https://aws.amazon.com/neptune/)


Ramsey, named after [Frank Ramsey](https://en.wikipedia.org/wiki/Frank_Ramsey_(mathematician)), is a open-source managed graph database.


## Why?


Neptune DB has some glaring [limitations](https://docs.aws.amazon.com/neptune/latest/userguide/limits.html) that make it unfit for many applications. Ramsey is an attempt to solve some of those issues. 

Some particular ones to note: 
1. There is a size limit of 55 MB on the size of an individual property or label.
2. The total size of Gremlin and SPARQL HTTP requests must be less than 150 MB.
3. A Neptune cluster volume can grow to a maximum size of 128 tebibytes (TiB) (this one might be hard for Ramsey to solve)


