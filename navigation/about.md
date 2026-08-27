---
layout: post
title: About
permalink: /about/
comments: true
---

## As a conversation Starter

Here are some places I have lived.

<comment>
Flags are made using Wikipedia images
</comment>

<style>
    /* Style looks pretty compact, 
       - grid-container and grid-item are referenced the code 
    */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); /* Dynamic columns */
        gap: 10px;
    }
    .grid-item {
        text-align: center;
    }
    .grid-item img {
        width: 100%;
        height: 100px; /* Fixed height for uniformity */
        object-fit: contain; /* Ensure the image fits within the fixed height */
    }
    .grid-item p {
        margin: 5px 0; /* Add some margin for spacing */
    }

    .image-gallery {
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        gap: 10px;
        }

    .image-gallery img {
        max-height: 150px;
        object-fit: cover;
        border-radius: 5px;
    }
</style>

<!-- This grid_container class is used by CSS styling and the id is used by JavaScript connection -->
<div class="grid-container" id="grid_container">
    <!-- content will be added here by JavaScript -->
</div>

<script>
    // 1. Make a connection to the HTML container defined in the HTML div
    var container = document.getElementById("grid_container"); // This container connects to the HTML div

    // 2. Define a JavaScript object for our http source and our data rows for the Living in the World grid
    var http_source = "https://upload.wikimedia.org/wikipedia/commons/";
     var living_in_the_world = [
        {"flag": "f/fa/Flag_of_the_People%27s_Republic_of_China.svg", "greeting": "你好", "description": "China - 0 to 13"},
        {"flag": "0/01/Flag_of_California.svg", "greeting": "Hey", "description": "California - 14 to present"},
    ];

    // 3a. Consider how to update style count for size of container
    // The grid-template-columns has been defined as dynamic with auto-fill and minmax

    // 3b. Build grid items inside of our container for each row of data
    for (const location of living_in_the_world) {
        // Create a "div" with "class grid-item" for each row
        var gridItem = document.createElement("div");
        gridItem.className = "grid-item";  // This class name connects the gridItem to the CSS style elements
        // Add "img" HTML tag for the flag
        var img = document.createElement("img");
        img.src = http_source + location.flag; // concatenate the source and flag
        img.alt = location.flag + " Flag"; // add alt text for accessibility

        // Add "p" HTML tag for the description
        var description = document.createElement("p");
        description.textContent = location.description; // extract the description

        // Add "p" HTML tag for the greeting
        var greeting = document.createElement("p");
        greeting.textContent = location.greeting;  // extract the greeting

        // Append img and p HTML tags to the grid item DIV
        gridItem.appendChild(img);
        gridItem.appendChild(description);
        gridItem.appendChild(greeting);

        // Append the grid item DIV to the container DIV
        container.appendChild(gridItem);
    }
</script>

### Journey through Life

Here is what I did at those places

- (≧∇≦)/ Finished elementary school and 7th grade in China, Beijing. (elementary school in Beijing is from 1st to 6th grade)
- (oﾟ▽ﾟ)o Middle school (8th) and high school in San Diego.
- (๑>◡<๑) Oak Valley Middle School class of 2024. 
- (￣▽￣)~ Del Norte High School class of 2029. 

### Culture, Family, and Fun

Everything for me, as for many others, revolves around family and faith.

- Both of my parents are Chinese, and I have a order sister who is currently studying in USC for her graduate degree. 
- I have very close relationship with my aunt and three cousins.
- The gallery of pics has some of my family, fun, culture and faith memories.

<comment>
Gallery of Pics, scroll to the right for more ...
</comment>
<div class="image-gallery">
  <img src="{{site.baseurl}}/images/about/jinyuzuozhe.png" alt="Image 1">
  <img src="{{site.baseurl}}/images/about/xiyu.png" alt="Image 2">
  <img src="{{site.baseurl}}/images/about/xiyujinyu.png" alt="Image 3">
  <img src="{{site.baseurl}}/images/about/chifan.jpg" alt="Image 4">
  <img src="{{site.baseurl}}/images/about/shengdan.jpg" alt="Image 5">
  <img src="{{site.baseurl}}/images/about/ruoruo.jpg" alt="Image 6">


</div>
