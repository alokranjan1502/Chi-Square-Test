# Chi-Square-Test
Chi-Square Test using python
Chi Square Test is Non-Parametric test to be performed for categorical variables. It is used for two different purposes. Most of people usages Chi-Square for only “goodness-of-fit”. But it can be used for “test of association” (also known as test of independence). Let us discuss in more detail regarding these two method in details and how python can help us to calculate these values.
Test of Association
 Chi-Square test is used to find association between two categorical variables. It is similar to correlation. In Correlation we calculate correlation between two numeric variables. But in Chi-Square Test we usage categorical variables such as gender, grade, type, like/dislike and other types of values. Chi-square will be measured by below formula	
 
	 Xsq=∑▒〖(Observed-Expected)〗^2/Expected

         Expected=  (RT*CT)/(Total )

Where RT = Row Total of Contingency Table,
      CT = Column Total of Contingency Table
      Total =Total Observations

Contingency Table – is cross table frequency distribution table of given categorical variable

Above calculated Xsq is compared with Xsq of Chi-Square Table (Xsq critical value). If Xsq calculated is more than Xsq critical value then we reject Null Hypothesis (H0). In order to get Xsq critical value we need degree of freedom and significance level (can be taken as 5% by default).

Degree of freedom = (R-1)*(C-1)
R = No of Rows in Contingency Table and C = No of Columns in Contingency Table

Assumptions of Chi-Square Test is as follow.
H0 (Null Hypothesis): There is no association between given variables
H1 (Null Hypothesis): There is association between given variables

There is another method also to make conclusion using P-value. If P-value is greater than or equal to 0.05, then we accept H0 else we reject H0. Rejection of H0 means you have to accept H1.
