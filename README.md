##  First flask project

--------
* Done:
  * Updated previous homework:
    * creating application 
    * blueprints and updated views:
      * of requirements.txt
      * of user generator
      * of mean value
      * of astronaut
  *  Second part of homework: 
     * application updated for database
     * connect to database and created table
     * added fixtures with value for tracks table and added command for loading fixtures
     * added blueprint and views:
       * of unique artist
       * of quantity tracks
       * of number of tracks for genre
       * of title of song and length of song
       * mean of length and sum of all length
     * added templates for all views
     * updated view for number of tracks for genre, update schema.sql (added new table genres and table tracks was modified), fixtures.sql(added new value for table genres and updated value for table tracks
--------
_Function used requests, os, faker, flask and cvs library_


**How to start project**
* install all from requirements.txt
* for start application write in terminal:
```
    
    $ flask --app homework4 run
    
```
* initialize database
```
    
    $ flask --app homework4 init-db
    
```
* load fixtures for checking homework
```
    
    $ flask --app homework4 load-fixtures
    
```
* to quit press:
```
    
    CTRL+C
    
```
First part of homework:
  * for check requirements view write PATH: /firstpart/requirements/ in URL
  * for check user generator view write PATH: /firstpart/generate-users/ + GET parameter(?count=100)-default
  * for check mean value view write PATH: /firstpart/mean/ in URL
  * for check astronaut view write PATH: /firstpart/space/ in URL

Second part of homework:
* for check unique artist view, write PATH: /secondpart/names/ in URL
* for check quantity tracks view, write PATH: /secondpart/tracks/ in URL
* for check number of tracks view, write PATH: /secondpart/tracks/'genre" in URL
* for check title of song and length of song view, write PATH: /secondpart/tracks-sec/ in URL
* for check mean of length and sum of all length view, write PATH: /secondpart/tracks-sec/statistics/ in URL
