## HTML 5

There are some new useful tags in HTML 5.  These can be used to identify common sections of a page:
* ```<header>```
* ```<nav>```
* ```<section>```
* ```<footer>```

Other new common tags:
* ```<audio>``` - embedding audio
* ```<video>``` - embedding video
* ```<datalist>``` - Auto complete options

## CSS

CSS Selectors examples:

| Selector | Purpose                   |
|:--------:|---------------------------|
| a, b     | Multiple Element Selector |
| a b      | Descendant Selector       |
| a > b    | Child Selector            |
| a + b    | Adjacent Sibling Selector |
| [a=b]    | Attribute Selector        |
| a:b      | Pseudoclass Selector      |
| a::b     | Pseudoelement Selector    |


## Bootstrap

[Bootstrap](https://getbootstrap.com/) can be activated by linking to the their stylesheet in the head of the html. They provide the link code on their website.  
eg:

```html
<head>
  <title>The webpage title</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
</head>
```
Bootstrap splits the page into 12 columns and these can be used to space webpage elements across the page.  For example you could allocate 3 columns worth to 4 div elements so that they equally share the space across the screen.  They can even be used dynamically so that on a large screen more columns are used than on a smaller one.  see [columns0.html](columns0.html)

## SASS

Sass is an extension to css which allows the use of added features such as variables.  However Sass files need to be compiled/converted to css files in order to work with within browsers. It uses the extension ```scss```

You need to download and install Sass to process scss files into css.  The command to compile a Sass file is follows:
```sass input.scss output.css```  

Each change which is made to a Sass file requires it to be recompiled to a css.  As this could be repetitive and annoying when developing you can set Sass to watch a file and recompile it whenever it changes:

```sass --watch input.scss:output.css```
