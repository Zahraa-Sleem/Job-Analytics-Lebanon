# Job Analytics Lebanon



## Introduction:

In the dynamic landscape of the Lebanese job market, it has become increasingly evident that there is a noticeable dearth of comprehensive studies and research dedicated to exploring the perspectives and opportunities available to job seekers. This gap in understanding has left job seekers navigating the employment landscape without the necessary insights and tools to make informed decisions about their career paths. To address this pressing issue, our ambitious project is driven by the purpose of filling this void and providing a powerful and efficient means to analyze and visualize job prospects within Lebanon.

Our project stands as a beacon of hope for job seekers who are often left to their own devices in a complex and rapidly changing job market. By leveraging cutting-edge technology and innovative methodologies, we intend to offer a robust solution that will empower job seekers with valuable insights into their employment options. Here is how our project aims to achieve this:

1. **Comprehensive Data Collection:** To build a solid foundation, we will meticulously collect data from various sources, including job postings, industry reports, and government statistics. This data will encompass a wide range of factors, including job titles, industries, locations, educational requirements, and employment types.

2. **Sophisticated Analysis:** With a wealth of data at our disposal, our project will employ advanced data analysis techniques within the Lebanese job market. We will explore how different industries are evolving and which job sectors are growing.

3. **Visualization Tools:** To make the information easily accessible and understandable for job seekers, we will develop intuitive and user-friendly data visualization tools. These tools will enable users to interact with the data, allowing them to explore job opportunities  and employment patterns across departments, locations, and employment types.

4. **Real-time Updates:** The job market is dynamic and constantly evolving. Therefore, our project will incorporate real-time data updates to ensure that job seekers have access to the most current information, enabling them to adapt to changing market conditions effectively.

By embarking on this ambitious endeavor, our project seeks to empower job seekers in Lebanon with the knowledge and tools they need to navigate the job market with confidence. Through data-driven insights and user-friendly interfaces, we aim to bridge the gap between job seekers and employment prospects, fostering a more informed and thriving workforce within Lebanon. Ultimately, we believe that this initiative will contribute to the overall growth and prosperity of the Lebanese economy by aligning talent with opportunity in a more efficient and effective manner.
In the Lebanese Job Market, there is a lack of studies concerning the prospectives of job seekers.
Therefore this project aims to provide an efficient way to analyze and visualise job opportunities and patterns between departments,locations,employment type.

![](ReadMeStuff/netmo.gif)


## How to run the program?
This program uses selenium,pyqt5,PyQtWebEngine,folium,OpenCageGeocode,plotlyexpress. To install the required dependencies, run:

```
$ pip install -r requirements.txt
```

Then you can run the code using:
for running Window use:
```
python GUI.py
```
for recollecting data:
```
python webscraping.py
```



## user Manual:


## 1
![](ReadMeStuff/Main.png)

click the filter button, display statistical plots about the filtered data.



## 2
![](ReadMeStuff/Notfiltered.png)

The first bar graph shows the number of jobs in each department.
The pie chart next illustrates the employment type distribution.
The adjacent bar graph displays the number of jobs associated with specific tags or categories.
The map provides information about the distribution of job locations.


## 3
![](ReadMeStuff/Department.png)

Filter the job opportunities for each of the following departments.



## 4
![](ReadMeStuff/Location.png)

Filter the job opportunities for each of the following locations.



## 5
![](ReadMeStuff/Time.png)

Filter the job opportunities for each of the following employee type.


## 6
![](ReadMeStuff/Filtered.png)


A sample where the output was filtered on department Information Technology and Contract Employee type with no location filter.


## program structure

 In this program a website is scraped and provides a GUI that enables the user to visualize and understand the collected data.


## webscraping.py:

Using selenium webdriver,jobs available on jobsforlebanon website were scraped from the See All section.

All jobs available are now loaded and all Load More buttons are clicked to get all jobs available.

The job title,department and employment type are taken and the object is added to the   `objects.json` file.


##  statistics_1.py:

`countdepartment`: Takes all the data scraped and returns a dataframe with columns department and count where count represents the numbers of jobs in each department.

`countlocation`: Takes all the data scraped and returns a dataframe with columns location and count where count represents the numbers of jobs in each location.

`counttime`: Takes all the data scraped and returns a dataframe with columns time and count where count represents the numbers of jobs in each employment type.

`counttags`: Takes all the data scraped and returns a dataframe with columns Tag and Frequency where Frequency represents the numbers of jobs in each tag.


## plotting.py:

`plotdepartments`:Takes a dataframe and returns a bar graph of departments and frequency.
`plotlocation`:Takes a dataframe and returns a map of locations with frequency markers.
`plottime`:Takes a dataframe and returns a pie chart of time and frequency.
`plottags`:Takes a dataframe and returns a bar graph of tags and frequency.

## filtering.py:

`filter_dataframe`: Takes input the data scraped and the columns to filter on in addition to the values to filter on and returns the new data.

## getcategory.py:


`getdepartments`: A function that gets all department values from the scraped data.
`getlocations`: A function that gets all location values from the scraped data.
`gettime`: A function that gets all time values from the scraped data.

## datacleaning.py:

Cleans the data by removing /n from its job title and taking the country name in addition to adding tags to each job.


## GUI.py:

## NOTE:











