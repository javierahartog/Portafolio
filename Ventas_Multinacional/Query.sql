-- Paises con presencia de ventas
SELECT count(DISTINCT Country) AS Total_Countries
FROM Sales

-- Paises con mayor y menor registro de clientes
SELECT Country, count(*) AS Total_Customers
FROM Sales
GROUP BY Country
ORDER BY Total_Customers DESC;

SELECT Country, count(*) AS Total_Customers
FROM Sales
GROUP BY Country
ORDER BY Total_Customers ASC

-- Numero de categorias de los productos
SELECT count(DISTINCT CategoryName) AS Total_Category
FROM Sales

--Promedio de ventas (Q) y sus montos ($) por categoria
SELECT CategoryName, round(avg(Quantity)) AS Avg_Quantity,
	   round(avg(TotalSales)) AS Avg_TotalSales 
FROM Sales 
GROUP BY CategoryName

--Clientes regulares (+1 compra)
SELECT (count(DISTINCT Regular_Customers) * 100 / count(DISTINCT Total_Customers)) 
AS Percent_Regular_Customers
FROM (
	SELECT CustomerID AS Regular_Customers
	FROM Sales
	GROUP BY CustomerID
	HAVING count(*) > 1) t1,
	(SELECT CustomerID AS Total_Customers
	FROM Sales
	GROUP BY CustomerID) t2
