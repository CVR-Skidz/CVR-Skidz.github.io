---
name: PHP
tag: Languages
layout: page
---

PHP hypertext processor is an embedded scripting language heavilly used on the web. It runs server-side (never on the client) embedded within a document. Running through the PHP engine scripts are outputted as text, returned as parts of an html document.

We can include multiple PHP files within one another, similar to packages or header files. We can do so using the `require` and `include` methods:

- `require("myfile")` - includes `myfile` and crashes early if it is not found.
- `include("myfile")` - includes `myfile` and raises a warning if not found.
- `require_once("myfile")` - includes `myfile` only once throughout the file to avoid duplicated definitions, crashing if not found.

![PHP Engine](../Assets/PHP_Engine.png)

## Fundamentals

PHP can be embedded within a document using:

```html
<?php ... ?>
```

```html
<script language="php"> ... </script>
```

- PHP is generally c-sytanx like, php statements are delimited with `;`
- Comments are applicable with `//` or `#` or `/* ... */`
- PHP has a unique contains a unique string concatenation operator `.`

## Datatypes

All variables in php other than constants start with a `$`. PHP is dynamically typed and are not declared without initialization (this allows the initial type to be set). Constants are defined with the `define` method:

```php
define("NAME", "test");
define("AGE", -1);
define("ALIEN", false);

echo NAME." is ".AGE." and is an alien? ".ALIEN;
```

Strings in php can substitute varaibles without concatenation, `'` delimit literal strings whilts `"` delimit standard strings:

```php
$x = 100;

echo "x is $x"; //x is 100
echo 'x is $x'; //x is $x
```

PHP supports primitive and complex types. Reference support allows PHP to create objects and other data strcutures such as arrays. Arrays are a built in construct:

```php
$my_array = array(1,2,3);
$my_cool_array = [4,5,6];
$my_fake_array = ["a"=>7,"b"=>8];
$my_concatenated_array = $my_array + $my_cool_array;

for($i = 0; $i < count($my_array); ++$i) { echo $my_array[$i]." "; }

foreach($my_cool_array as $i) {  echo "$i "; }

echo $my_fake_array["a"]." ".$my_fake_array["b"];
//prints: 1 2 3 4 5 6 7 8
```

Additionally PHP contains pre-defined varaibles such as `$_GET` and `$_POST`. 

### Primitives

|Type|Description|
|----|-----------|
|String|Text|
|Integer|Numeric data|
|Float|Double floating point numeric data|
|Boolean|True and false|
|NULL|Absence of data|

## Functions

Functions in PHP do not need to define a return type:

```php
function my_function ($my_param) {
    echo $my_param;
    return $my_param;
}
```

## Operators

Since PHP is dynamically typed equality can be either strict or not:

- Strict equality: operands are of equal value and type `1 === 1`
- Non-strict equality: operands are of equal value `"1" == 1`
