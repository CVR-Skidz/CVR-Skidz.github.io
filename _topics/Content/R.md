---
name: R
tag: Languages
layout: page
---

The R programming language for statistics

## Datasets

A dataset is a collection of data. In a dataset an observation is equivalent to a row and a variable is equivalent to a row.

```R
library(help="datasets")
```

| Syntax    | Description                               |
| --------- | ----------------------------------------- |
| `data(x)` | Loads a dataset `x`                       |
| `head(x)` | Display the first 6 observations from `x` |
| `x$y`     | Extract the  variable `y` from `x`        |
| `View(x)` | Views `x`                                 |

### Built in constants

| Name         | Description                   |
| ------------ | ----------------------------- |
| `LETTERS`    | letters of the alphabet (A-Z) |
| `letters`    | letters of the alphabet (a-z) |
| `month.abb`  | Months (abbreviated)          |
| `month.name` | Months                        |
| `pi`         | $\pi$                         |

## Vectors

A list of values

```R
c(1:9) #vector 1 - 9
c(1,2,3,4,5,6,7,8,9) #vector 1 - 9
```

Vectors treat math operations individually for each element.

```R
c(1:9)*2 #vector 2 - 18
```

When operating on two vectors the operation is applied to matching indexes (i.e. index 1a + index 1b). If vectors have different lengths, R will recycle the indexes.

```R
c(1:9) + c(1:3) #1 + 1, 2 + 2, 3 + 3, 4 + 1 ...
```

## Subsetting

Equivalent to indexing.

```R
LETTERS[3] # C
LETTERS[3 : 5] # C, D, E
LETTERS[-3:-5] # A, B, F, G ...
LETTERS[repeat(c(TRUE, FALSE), 13)] # A, C, E ...
```

### Multidimensional Data

Multidimensional subsetting is ordered by `[obs, var]`  an empty value is equivalent to returning all values of that index.

```R
> x = data.frame(3:5, 6:8)
'''
  X3.5 X6.8
1    3    6
2    4    7
3    5    8
'''
```

| Subset    | Value   |
| --------- | ------- |
| `x[ , 2]` | 6, 7, 8 |
| `x[2 , ]` | 2, 4, 7 |

**Subsets can be logical conditions.**

```R
> x[x$X3.5 == 4, 2]
[1] 7
```



