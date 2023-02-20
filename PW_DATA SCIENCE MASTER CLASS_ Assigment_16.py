#!/usr/bin/env python
# coding: utf-8

# # Assignment_17-02-2023

# ## 1. What is MongoDB? Explain non-relational databases in short. In which Scenarios it is preferred to use MongoDB over SQL databases?
# 
# ### Ans:-
# 
#        MongoDB is a popular document-oriented, NoSQL database system. It uses a flexible schema design, where data is stored 
#        in the form of documents, which are similar to JSON objects. MongoDB is known for its scalability, high availability, 
#        and automatic sharding features. It is widely used in modern web applications, particularly those that require high
#        scalability and performance.
#         
#         
#        Non-relational databases, also known as NoSQL databases, are a type of database management system that stores and 
#        retrieves data in a non-tabular format. Unlike traditional relational databases, NoSQL databases are not based on 
#        the relational model of data. They use a variety of data models, including key-value, document-oriented, graph, and
#        column-oriented models. Non-relational databases are designed to handle large amounts of unstructured or 
#        semi-structured data, which can be difficult to store in traditional relational databases. 
#        
#        There are several scenarios in which MongoDB is preferred over SQL databases:
# 
#         1.Handling Large Volumes of Data:- MongoDB is designed to handle large volumes of unstructured data, making 
#         it a better option for big data applications.
# 
#         2.High Availability:- MongoDB is built to provide high availability with built-in features like automatic sharding, 
#         replication, and failover.
# 
#         3.Scalability:- MongoDB's dynamic schema and automatic sharding make it easy to scale horizontally by adding new 
#         nodes to a cluster.
# 
#         4.Real-time Analytics:- MongoDB's flexible schema design and dynamic indexing make it easy to perform real-time
#         analytics on large datasets.
# 
#         5.Agile Development:- MongoDB's document-oriented model makes it easier to make changes to the database schema as 
#         the application evolves.
#         
#                                         Overall, MongoDB is a good option for applications that need to handle large 
#          volumes of data and require high scalability and availability.
#         
#         
#         
# 
# 

# ## 2. State and Explain the  Feature of MangoDB.
# 
# ### Ans:-
#             MongoDB is a NoSQL database system that has several features that make it a popular choice for modern web 
#             applications. Here are some of the key features of MongoDB:
# 
#             1.Document-Oriented:- MongoDB is a document-oriented database, which means that data is stored in flexible, 
#             JSON-like documents. This allows for easy mapping between objects in the application and documents in the 
#             database.
# 
#             2.Dynamic Schema:- Unlike traditional relational databases, MongoDB does not require a predefined schema. 
#             Instead, the schema can be created dynamically as data is inserted into the database.
# 
#             3.High Performance:- MongoDB is designed for high performance and scalability, with features like automatic
#             sharding, horizontal scaling, and distributed architecture.
# 
#             4.Indexing:- MongoDB supports a wide range of indexing options, including single field, compound, geospatial,
#             and text indexing. This makes it easy to search for and retrieve data from the database.
#             
#             
#             5.Aggregation Framework:- MongoDB's aggregation framework provides a powerful set of tools for performing 
#             complex queries and analytics on data in the database.
# 
#             6.Replication and High Availability:- MongoDB provides built-in replication and failover mechanisms that ensure 
#             high availability and data redundancy.
# 
#             7.Flexible Data Model:- MongoDB's flexible data model allows for easy storage of a wide range of data types, 
#             including binary data, arrays, and embedded documents.
# 
#             8.Security:- MongoDB includes built-in security features, including authentication, authorization,
#             and role-based access control.

# ## 3. Write a code to connect MangoDB to Python. Also, create a database and a collection in MangoDB.
# 
# ### Ans:-
# 
# 

# In[3]:


import pymongo


# In[5]:


# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")


# In[6]:


# Create a new database called "mydatabase"
mydb = client['Employee']


# In[8]:


# Create a new collection called "Informtion" in the "mydatabase" database
information=mydb.employeeinformtion


# In[ ]:


# Insert a new document into the "information" collection
record = {'First Name':'Manas',"Last Name":"Pandey","Address":"S-1 YamunaBlock"}
x=information.insert_one(record)


# In[ ]:


# Print the ID of the newly inserted document
print(x.inserted_id)


# ## 4. Using the database and the collection created question number 3, write a code to insert one record, and many records. Use the find() and fine_one() method to print the insert record.
# 
# ### Ans:-

# ## 5. Explain how you can use the find() method to query the MongoDB database. write a simple code to demonstrate this.
# 
# ### Ans:-
#             The find() method is used to query the MongoDB database and retrieve documents that match a specific condition.
#             The method accepts a query object as an argument, which specifies the condition to filter the documents.
# 
#             Here's a simple code example that demonstrates how to use the find() method to query a MongoDB database:
# 

# In[ ]:


# import pymongo library
import pymongo

# create a MongoClient instance
client = pymongo.MongoClient()

# select the database and collection
mydb = client['my_database']
collection = db['my_collection']

# define the query object
query = { 'name': 'Manas' }

# use the find() method to retrieve documents that match the query
result = collection.find(query)

# loop through the result and print each document
for doc in result:
    print(doc)


# ## 6. Explain the sort() method. Give an example to demonstrate sorting in MongoDB.
# db.students.find().sort({ gpa: -1 })
# 
# ### Ans:-
# 
#         The sort() method is used in MongoDB to sort the documents in a collection based on a specified field or fields. 
#         The method takes a single parameter, which is an object that defines the fields to sort by and their sorting order.
#         The keys of this object are the fields to sort by, and their corresponding values are either 1 (to sort in ascending
#         order) or -1 (to sort in descending order).
# 
#             Here is an example of how to use the sort() method in MongoDB:
#             
#             
#                                 Suppose we have a collection named "students" that contains documents with the following
#        fields: "name" (string), "age" (number), and "gpa" (number). To sort the documents in the collection by the "gpa" 
#        field in descending order, we can use the following code:
#            
#                     db.students.find().sort({ gpa: -1 })
#                     
#                                 Alternatively, we can also sort by multiple fields by passing an object with multiple 
#        key-value pairs to the sort() method. For example, to sort the "students" collection by "age" in ascending order 
#        and "gpa" in descending order, we can use the following code:
#        
#                   db.students.find().sort({ age: 1, gpa: -1 })
#                   
#                   

# ## 7. Explain why delete_one(),delete_many(), and drop() is used in MongoDB.
# 
# ### Ans:-
#             In MongoDB, there are three methods for deleting data from a collection:
# 
#         1.delete_one():- This method is used to delete a single document from a collection that matches a specified filter.
#         If there are multiple documents that match the filter, only the first document that is found will be deleted. This
#         method is useful when you want to delete a specific document from a collection.
# 
#         2.delete_many():- This method is used to delete all documents from a collection that match a specified filter. This
#         method is useful when you want to delete multiple documents from a collection at once.
# 
#         3.drop():- This method is used to completely remove a collection from a database. This method is useful when you 
#         want to delete an entire collection, including all of its documents and indexes.

# In[ ]:




