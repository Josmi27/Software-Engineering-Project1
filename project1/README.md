## What was the theme you chose?
The theme that I chose for this project is a donut theme. The reason why is because I love donuts, and wanted to share my love for donuts with the world!

## How did you pick your searches to fit the theme?
In order to successfully pick searches to fit my theme, I used a trial and error method. I originally tried using a search involving a hashtag, but that was too broad. After a few more attempts, I became satisfied with the results yielded from 'yummy donuts' in the Twitter search bar. 

## What are at least 3 issues you encountered with your project? How did you fix them?
One issue that I encountered was getting the picture of the recipe to display. I solved this issue by incorporating the 'Get Recipe By ID' API, and then correctly parsed through the data to access a usable image url.

Another issue that I encountered was figuring out how to successfully use the Spoonacular 'Get Recipe Information By ID' API. The problem was that I had to dynamically refer to each donut ID separately, in order to get various recipe information. I didn't remember how to inject a changing variable into a string, but I used Google to remember the string format option, and my problem was fixed very soon.

One last issue that I encountered during this project was verifying that I had enough search results with the Spoonacular Search API. I realized during testing that I was getting the same types of donuts more often than not. So to verify that I would have at least 7 different results, I printed the json results, and used jsonformatter to confirm that there were at least 7 different entries for me to load results for. 

## What are known problems, if any, with your project?
One known problem with my project is that there is lack of creativity with the formatting. Also, the ingredients of the recipe does not appear on the page. One last issue that I know about is that my API keys are exposed in my code. Even though we learned how to use OS.getenv() to let Heroku store the keys in secrecy, my code did not recognize some of my Twitter keys after I added them into Heroku's config files. 

## What would you do to improve your project in the future?
I would style my project to be more visually appealing in the future. Also, I would pick a different food that gave more results to work with.

<br>
<em> Link To Production: </em> https://mysterious-sea-27802.herokuapp.com/
