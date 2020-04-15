## Javascript

This course will use ES6 version of JavaScript.  

``` Javascript
<script>
  alert('Hello, world!');
</script>
```

#### Common Events
When you can control when JavaScript will run
* **onclick** - Mouse click
* **onmouseover** - Hover over with mouse
* **onkeydown** - Triggered as the key goes down
* **onkeyup** - Triggered as key is released
* **onload** - When load has completed
* **onblur** - When element is out of focus


#### QuerySelector

Works in a similar fashion as CSS and some examples are as follows:


* document.querySelector('tag')
* document.querySelector('#id')
* document.querySelector('.class')


#### Types of variable

* **const** - Constant cannot be updated
* **let** - exists only within the scope
* **var** - exists across all scopes

#### Browser inspect

The console within a browser can be used to return error messages and also add JavaScript and manipulate values of variables.

eg: run selectors or adjust variables

#### Arrow functions - ES6 JavaScript
``` JavaScript
// Arrow function which takes no arguments
() => {
  alert('Hello, world!');
}

// Function which takes x as an input
x => {
  alert(x);
}

// Function takes as input number x and returns x * 2
x => x * 2
```
    Note 'this' may not work with arrow notation and the traditional function keyword would be needed 
