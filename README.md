# Pants Viewer

# Overview of Application

This is a read only, RESTful web app that displays a few products and their respective inventories, while providing metadata on each product. I used python with Flask on the backend, ReactJS for the front-end viewer. I used a sqlite database which was actually checked in to source control since it was so small, and eliminates the overhead of recreating the database.

# Setup Server

The app can be brought down and used locally

Clone the repository: 
```
$ git clone git@github.com:userkaranb/pants-viewer.git
```

Setup your python virtualenv. This will provide a clean slate from all python dependencies you may have installed on your system, and will be configured to only use what is necessary to run the app. If you don't have virtualenv installed, go here. http://docs.python-guide.org/en/latest/dev/virtualenvs/ . After, in the directory above the cloned repo, run this:
```
$ virtualenv sandbox && source sandbox/bin/activate
```

This will create a new virtualenv with no pip packages and activate it. You can call deactivate to get out of your sandbox instance.

cd into the python source code and install all dependencies
```
$ cd pants-viewer/server
$ python setup.py install
```

Start the python app. It will open on port 5000
```
$ python app.py
```

Now, if you go to localhost:5000/ in your browser, you should see a landing page with the different routes. The server is up. Now let's set up the client

# Setup Client

Setting up the client should be very straightforward. All you need to do is install the dependencies, and then start the client, which you can do in one command:

```
npm install && npm start
```

You should now be able to to view the client at http://localhost:3000/ which will contact the server you started up in the previous step at http://localhost:5000

# Using the app

One thing to note is that the main View, the HomeView, is what I intended the output of this project to be. This view (which is at localhost:3000/) displays each of the products and some metadata about each product. If you go to the bottom, you will see the table displaying all rows of inventory. I have included the product Id in each row.

There were two additional routes that I created, and they are for a different workflow which was not asked for in the assignment. If you go to localhost:3000/products -- you will see a view highlighting the 4 products. If you click on one, you will be redirected to a new screen which shows the inventory just for that product. I just added this if the user wants a different view of a particular product. 

# Architecture

The technology decision was to go with a python flask server for the backend, and react for the front end. React is new and interesting, and I definitely wanted to get more comfortable with it after using this project. Python is a language I have used in the past, and I love how easy it is integrable with many databases. I used sqlite3, because I know the size of our database and I could actually check in our .db file. 

On startup, the server creates a ProductCachingService, a class responsible for grabbing products and inventories from the database, and transforming them into dictionaries immediately ready for consumption by a client. It keeps these dictionaries in memory, to avoid unnecessary and repeated queries to the database. We assume this data isn't going to be changed. The backend is completely unit tested (with the exception of DataAccess, which hits the database for trivial operations).

The front end, is fairly light, and displays all 4 of the products on the home page along with a table displaying the inventory. There is only one call to the server, which is the /products_with_inventory route at localhost:5000

# Testing

To test the server, all you have to do is call the following from server/ folder

```
$ nosetests --nocapture
```

The above command will discover all tests below (which are all in the test driectory) and print out any stdout.

# Future Work

There are a few things that can definitely be done to enhance this app.

The first thing I would like to highlight is client side caching. In React, one can utilize Redux to maintain state. Since our data is not changing, we can afford to keep all this data in memory and avoid unnecssary calls to the server.

On the backend, it would be nice to use a real logger, to measure behavior and latency. If the size of our database grows, these queries could become more costly. 

I would also like to deploy this to a real environment, like heroku. I could place this in a docker container, and add config files so the URLs aren't hardcoded. Currently, this is only set up to run locally.

Another thing would be adding tests to the front end viewer. The front end is fairly simple, and isn't doing a whole lot. The backend was tested pretty thorougly, which is why I was confident in the integrity of the data being displayed. That being said, if I had more time, I would like to add some tests to test our components.