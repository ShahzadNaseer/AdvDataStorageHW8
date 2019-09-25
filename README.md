# AdvDataStorageHW8
Week 10, HW 8, Advanced-Data-Storage-and-Retrieval 

## Step 1 - Climate Analysis and Exploration


To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

### Precipitation Analysis

* Design a query to retrieve the last 12 months of precipitation data.

* Select only the `date` and `prcp` values.

* Load the query results into a Pandas DataFrame and set the index to the date column.

* Sort the DataFrame values by `date`.

* Plot the results using the DataFrame `plot` method.

![Imgur Image](https://github.com/ShahzadNaseer/AdvDataStorageHW8/blob/master/DateVsPrecipitation.png)
 
* Use Pandas to print the summary statistics for the precipitation data.

* Design a query to retrieve the last 12 months of temperature observation data (tobs).

  * Filter by the station with the highest number of observations.

  * Plot the results as a histogram with `bins=12`.

    ![station-histogram](https://github.com/ShahzadNaseer/AdvDataStorageHW8/HistMostActiveStation.png)
    
    

#### Data Modeling

Table scripts are created after looking the CSVs files and data. Table names are same as CSV file name. Table creation scripts are https://github.com/ShahzadNaseer/SqlHW7/blob/master/TableCreatioScripts.sql

ERD was created using Microsoft Sql Server Management Studio. Here is ERD file https://github.com/ShahzadNaseer/SqlHW7/blob/master/ERD-HW7.jpg

#### Data Engineering

* Tables were created using scripts in Postgres database

* Data from CSV files were imported into corresponding SQL table.

#### Data Analysis

Query file is included to asnwer following questions. Queries are in this file https://github.com/ShahzadNaseer/SqlHW7/blob/master/SqlQueries.sql

1. List the following details of each employee: employee number, last name, first name, gender, and salary.

2. List employees who were hired in 1986.

3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.

4. List the department of each employee with the following information: employee number, last name, first name, and department name.

5. List all employees whose first name is "Hercules" and last names begin with "B."

6. List all employees in the Sales department, including their employee number, last name, first name, and department name.

7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

### Bonus

Draw bar graph in Jupyter Notebook using sqlalchemy and matplotlib. Jupyter Notebook is https://github.com/ShahzadNaseer/SqlHW7/blob/master/AvgSalaryByTitle.ipynb

### Extra Study

Did further analysis of average salaries of Male vs Female. Results of this analysis is worth looking.

![Imgur Image](https://github.com/ShahzadNaseer/SqlHW7/blob/master/GenderAvgSalaryComparison.png)
