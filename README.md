# RESTful API for Vimman

[![Build Status](https://travis-ci.org/OMOSAN/vimman-api.svg?branch=master)](https://travis-ci.org/OMOSAN/vimman-api)
[![Join the chat at https://gitter.im/OMOSAN/vimman-api](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/OMOSAN/vimman-api?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


## Development

1) Setting MySQL

    $ mysql -u {MYSQL_USER_NAME} < data/sql/mysql_createdb.sql
    $ mysql -u {MYSQL_USER_NAME} vimman < data/sql/mysql_schema.sql

2) Execute to command of below.

    $ pip install -r requirements.txt
    $ cp src/config/databases.py.sample src/config/databases.py
    $ python src/app.py

3) Access to `localhost:5000`. ex) `localhost:5000/questions`


## Contribution

1. Fork it ( http://github.com/OMOSAN/vimman-api/fork )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

