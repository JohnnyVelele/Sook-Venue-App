# Sook-Venue-App
Web App for searching for a given location and returning venues near by


Initally I started off by understanding the Foursquare API and testing it with a couple different locations to ensure I had it working correctly.
I then followed up by writing this in to a file to make it easier to read for myself.
This way I could see how the JSON data was formatted when received.
I then took this over to start creating my FLASK program, and created the method that could be called when the JSON data had to be reached.
I created the inital template to show a user input, which was the location of the search, and this was used in the venues method after they would press submit.
Using request to get that input from the form, I call the getVenues method which specifically for looping through the JSON data retreived when the location the input was used.
This loop creates a new list of the name of every venue in a 500 meter radius of the location they specified and returns it.
All this is then represented on the venues template in a table form, which I felt suitbale for this amount of data.
I then created a button to show more info on any of the venues. This will get the rest of the JSON data linked to that Venues name, including location etc.
This is then shown on its own page, though I haven't formatted it in the most appealing way currently.
