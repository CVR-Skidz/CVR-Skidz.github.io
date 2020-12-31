---
name: SQL
tag: Languages
layout: page
---

Ultra simple Structured Query Language reference

|SQL type|Description|
|---|---|
|DDL|Data definition languages create the database relationships|
|DML|Data Manipulation languages insert, delete, and modify a database|

- Use UPPERCASE for keys and observers
- Terminate a statement with a `;`

## Selection
> Querying the value of columns in a table

```
Select [DISTINCT] {*, column {alias}, ...}
FROM table;
```

An example: 

```
SELECT * 
FROM departments
```

|Selector|Description|
|---|---|
|`*`|All| 
|`[COLUMN, ...]`| Selects all of the specified columns for each row, multiple columns are comma separated.|

**Alias:**
> Renames a column heading in the output of a query

```
SELECT [DISTINCT] {column [AS] {alias}}
FROM {table};
```

Example: 

```
SELECT name AS "First Name", familly AS "Last Name"
FROM customers
```

- The `AS` keyword is optional

**Conditions:**

```
SELECT ... WHERE {column}{operator}{value} ... ; 
```

Example: Selecting the names of customers who live in London.

```
SELECT last_name, first_name
FROM customers
WHERE city = 'London';
```

**Unique Selection:**
We can select only unique values (remove duplicates) from a query using the `DISTINCT` keyword.

```
SELECT DISTINCT dep_id
FROM employees;
```

## Viewing Tables

```
DESCRIBE table
```

## Importing Scripts

```
@[PATH_TO_SCRIPT]
...
```

## Types

|Type|Syntax|
|---|---|
|Character data (Strings)|`'[TEXT]'`|
|Character data with formatting| `"[TEXT]"`|

- Character data is case sensitive.

## Arithmetic

|Operator|Description|
|---|---|
|`+`|Add|
|`-`|Subtract|
|`*`|Multiply|
|`\`|Divide|
|`{pipe}{pipe}`|Concatenation: combining columns|


## Concatenation
> Combining the values present in multiple specified rows

```
SELECT familly || ', ' || first AS "Full Name"
FROM customers;
```

- The result of concatenation is always a character expression.

## Comparison Operators

|Operator|Description|
|---|---|
|`<`| Less than |
|`>`| Greater than |
|`<=`| Less than equal to |
|`>=`|...|
|`=`| equal to|
|`!=` or `<>`| Not equal to|
|`BETWEEN x AND y`| Between `x` and `y` inclusive |
|`IN (list)`| Is in list | 
| `LIKE {char sequence}` | Matches character sequence|
| `IS NULL` | Is `x`, in this case `NULL` |
| `NOT` | Logical inverse |
| `AND` | Logical intersect |
| `OR` | Logical conjunction |

Character matching e.g `LIKE 'A_C%'`:
- `%` matches zero or more characters
- `_` matches one character
- The above example matches a string starting with 'A', then has any character separating 'C', followed by any sequence of characters.
- We can escape characters using `LIKE 'ABC{c}%' ESCAPE '{c}'`, which designates an escape character `c`. 

## Sorting

```
ORDER BY {column [ASC(default) or DESC], ...}; 
```

- When sorting by multiple columns it will sort by column 1 then by column 2 etc

## Substitution Variables
> Temporarily storing values

```
{Statement} &{variable_name};
```

A variable can be set in the script, but if it is not, it will be prompted when running the query.

## Creation Statements
> Statements used to create database objects
> 
### Creating Tables

To create a table we must have the appropriate privilege.

```
CREATE TABLE {name}  ({column name} {type}({size}), ...);
```

We can also use `DEFAULT` to provide a default attribute: e.g. `dob date DEFAULT sysdate` provides the default `dob` as the current system date

|Type|Description|
|---|---|
|`CHAR(size)`|Character string of length `size`|
|`VARCAHR2`|Variable length character data|
|`CLOB`|Character data up to 8TB|
|`NUMBER(p, s)`|Variable length numeric data|
|`DATE`|Date and time|
|`BLOB`|Binary data up to 8TB|
|`RAW`|Raw binary data|
|`BFILE`|Binary data stored in the operating system (outside the database)|

Tables can also be created from a subquery, where a new table will created from a query.

```
CREATE TABLE {name} AS {subquery};
```

Tables are created as user tables (where the user owns them). The server maintains a data dictionary which is a database owned by the server containing information on other databases, users, etc.

### Modifying Tables

Tables can be modified using `ALTER`.

``` 
ALTER TABLE {name} {ADD or MODIFY} ({name} {type} [DEFAULT])
```

- `ADD` insets a new column
- `MODIFY` changes the type or size of a column (only if there are no values stored in that column)

We can also rename: 

```
RENAME TABLE {name} TO {new name}
``` 

... or we can truncate (remove all data but do not drop table):

```
TRUNCATE TABLE {name};
```

Furthermore we can comment an attribute:

```
COMMENT ON COLUMN {table}.{column} IS '{comment}';
```

### Dropping Tables

Tables can be deleted with `DROP` 

``` 
DROP TABLE {name};
```

## Constraints
> Constraints are used to enforce how data is inserted.

Some constraints include: `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN_KEY`, `CHECK`, `INDEX` 

Constraints should be named to be easily referenced. Constraints can be specified for a table or column:

- Table constraint: `CREATE TABLE ... ( ... CONSTRAINT {name} {constraint} {column name}, ...)`
- Column constraints: `{name} {type} [DEFAULT] [column constraint]` (*Note that the `CONSTRAINT` keyword is not used for columns*)

Composite keys must be declared at a table level with `PRIMARY KEY({a}, {b}, ...)`. 

Foreign keys follow the following syntax:

```
CONSTRAINT {constraint name} FOREIGN KEY ({column name}) REFERENCES {foreign table name} ({column name});
```

## Data Manipulation
> Making changes to data.

Adding data to a table uses `INSERT`:

```
INSERT INTO {table_name} ([column], ...) values ([value], ...);
```

- You do not have to specify column names when inserting values to all the columns in a row.

`INSERT` can also copy values from one table to another (by selecting the values to copy):

```
INSERT INTO {table_name} ([colunm], ...) SELECT ...;
```

A row can be updated using `UPDATE`:

```
UPDATE {table_name} 
SET [row_name] = [value]
WHERE [row_name] = [value]; 
```

A row can be deleted using `DELETE`:

```
DELETE FROM {table_name}
WHERE [row_name] = [value;]
```