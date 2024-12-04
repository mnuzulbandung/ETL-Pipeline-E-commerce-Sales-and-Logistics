# **ETL Pipeline**
# **E-commerce Sales and Logistics**

This program is tailored for e-commerce marketplaces, enabling users to analyze sales and shipping performance effectively. It implements an end-to-end ETL (Extract, Transform, Load) data pipeline to automate data processing. Then, it also used Kibana to generate interactive dashboards. The solution leverages PostgreSQL for data storage, Apache Airflow for workflow automation, Elasticsearch for fast and scalable data indexing, and Kibana for intuitive data visualization.

File __


## **Introduction**

In e-commerce, products can have widely varying profit margins. While some generate substantial profits, others may result in losses if their revenues fail to cover production costs. Without clear insight into which products are profitable or unprofitable, the gains from high-performing items may be offset by losses from underperforming ones. This imbalance can create a "robbing Peter to pay Paul" situation, where overall profitability is compromised. To resolve this, it is crucial to identify products with the highest and lowest profit margins. Furthermore, analyzing the relationship between frequently sold items and their profitability is key. Unprofitable products can be phased out, and even popular items with low profit margins may need to be reconsidered. By focusing on products that are both in demand and generate significant profits, stores can enhance operational efficiency and maximize their bottom line.


## **Data Overview**

The dataset used for this project is sourced from Kaggle and consists of 20 features. The features Product ID, Category, Sub-Category, and Product Name describe the characteristics of the product. Then, the features Customer ID, Customer Name, Segment, Country, City, State, Postal Code, and Region describe the characteristics of the customer. Furthermore, the features Order Date, Ship Date, Ship Mode, Sales, Quantity, Discount, and Profit describe the characteristics of the order made by customer.

Source: [Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)

Here’s a summary of the columns in the dataset:

| Key Name      | Description                                                                                              | Data Type   |
|---------------|----------------------------------------------------------------------------------------------------------|-------------|
| Order ID      | A unique identifier for each order placed in the e-commerce system.                                      | Categorical |
| Order Date    | The date when the order was placed by the customer.                                                      | Numerical   |
| Ship Date     | The date when the order was shipped to the customer.                                                     | Numerical   |
| Ship Mode     | The shipping method selected for the order, such as Standard, Express, or Priority.                      | Categorical |
| Customer ID   | A unique identifier for each customer in the database.                                                   | Categorical |
| Customer Name | The full name of the customer who placed the order.                                                      | Categorical |
| Segment       | The market segment the customer belongs to, such as Consumer, Corporate, or Home Office.                 | Categorical |
| Country       | The country where the order was placed or shipped.                                                       | Categorical |
| City          | The city where the order was placed or shipped.                                                          | Categorical |
| State         | The state or province where the order was placed or shipped.                                             | Categorical |
| Postal Code   | The postal or ZIP code of the customer's shipping address.                                               | Numerical   |
| Region        | The geographical region (e.g., East, West, Central) associated with the customer's location.             | Categorical |
| Product ID    | A unique identifier for the product ordered.                                                             | Categorical |
| Category      | The main category of the product, such as Furniture, Office Supplies, or Technology.                     | Categorical |
| Sub-Category  | The subcategory of the product, providing a more specific classification within the main category (e.g., Chairs, Binders, Phones). | Categorical |
| Product Name  | The specific name or description of the product ordered.                                                 | Categorical |
| Sales         | The total revenue generated from the sale of the product (calculated as quantity sold multiplied by the unit price, minus any discounts applied). | Numerical   |
| Quantity      | The number of units of the product ordered.                                                              | Numerical   |
| Discount      | The discount percentage or amount applied to the order.                                                  | Numerical   |
| Profit        | The profit generated from the sale of the product (calculated as sales minus the cost of goods sold and other expenses). | Numerical   |


## **Overall Methodology**

1.	**Input Data**: Upload data from local storage into the PostgreSQL database, serving as the central Data Warehouse.
2.	**ETL Data Pipeline**: Develop Airflow DAGs to automate the Extract, Transform, and Load (ETL) processes: a). **Extraction**: Retrieve data from the PostgreSQL database. b). **Transformation**: Perform data cleaning and preprocessing. c). **Loading**: Push the cleaned data into the Elasticsearch database, functioning as the Data Mart.
3.	**Dashboard Creation**: Generate dashboards using Kibana that is connected with the Elasticsearch database.


## **Conclusion**

- **Most Sold Products**: Products sold the most are related to office appliances, such as staples, binders, and paper.
- **Comparing High Profit Products and Most Sold Products**: Even though Binders and Paper are the most sold products, they do not bring a significant profit compared to copiers and phones. It can lead to low operational cost efficiency.
- **Low Profit Products**: Tables (furniture) are the products with a considerable loss. It can lower the overall profit margin. This loss might be due to the product being broken while being shipped, the buyer cancelling it, and we need to refund it.
- **Shipment Class**: Most buyers chose to ship our products from the standard class. It can lead to low logistic performance since most people use the same shipment type. The shipment can be late, and products can be broken while being shipped. This might be due to the high price of first-class and same-day shipment.
- **Buyers Location**: Most buyers were from California. We can build a new warehouse in California to reduce the shipment price for First Class and Same-Day.


## **Recommendations**

- We need to increase the price for binders and paper.
- We need to discontinue the table to be sold on our platform.
- We need to lower the price for First and Same Day shipment classes by building a new warehouse in California.


## **Recommendations (Technical)**

The Kibana, which we used for data analysis, can not analyse whether the shipment is late by generating a new field by subtracting the ship date from the order date. We need to generate a new field in the ETL Pipeline.


## **Dependencies**

- Database: PostgreSQL
- ETL Tool: Apache Airflow
- Search Engine: Elasticsearch
- Visualization Tool: Kibana

## **Libraries Used**
- Pandas
- GreatExpectation
- Elasticsearch
- Apache Airflow

## **Author**

M Nuzul  
LinkedIn: [M Nuzul](https://www.linkedin.com/in/m-nuzul/)
