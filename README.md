# Time Warp
#### Video Demo: <URL>
#### Description:
A time zone coordination web application.

Time Warp is a project that helps with time zone differences globally. It works
by entering a day of the month, hour and minutes of the day and returns a string 
that will show the local time of different time zones. 

The idea for this project came to me from my friend gaming group chat, where we all
 live in different time zones, even across the world.
We can never remember what time it is for everyone, so I decided to solve that problem!

#### Software:
 - time_warp.py: This is the core logic for the time zone translation. It uses the standard
 library in Python to take a given input for a designated time, in which when you input what
 time zones you want, it will output the respective time zone for that initial designated time.

 There are some preset time zones from North America and Australia, but has the capability to do 
 a quick search for a not-listed time zone that you would like to translate.

 - app.py: This is the Flask application entry point. This holds the routing for the application
 and controls the data passed into each endpoint in the application. This module talks to the
 logic for the time zones and connects it with the information presented to the user.

 - templates/404.html: Holds the 404 markup.
 - templates/index.html: This is the markup for the entry point into the program.
 - templates/layout.html: This is the base design for the html for the app.
 - templates/search.html: This is the markup for the search results page.
 - timezones.html: This is the final page of the application, where the results to the request
 will appear.
 - static/style.css: This holds the style to the app.

 #### Design Choices:
 I was originally going to keep it minimal to just the locations I needed, but as I worked on the
 app I was hit by inspiration, which turned into adding the search feature to be more open
 to the world instead of just my local gaming group.

 I think eventually I might add the feature to allowing as many searches as the user wants, as right
 now it is limited to only one search. I didn't add it as I may need to refactor how I have the logic 
 working at the moment. I want to keep security in mind since how the logic is currently working.

 Ultimately, I wanted to keep this idea on a small scale, as I have plans for another idea that I could
 eventually incorporate this package into.
