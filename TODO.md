# TODO

- Fix tests


### testing todos:
unit tests for:
- [X] db/db_item_descriptor
- [X] models/products module
- [/!] db/adapters/product_adapter --- cant test without mysql server
- [/!] db/db_connection --- cant test without mysql server
- [/!] db/db_migrator --- cant test without mysql server
- [/!] webserver/api --- cant test without mysql server

options: create new database exclusively for testing, OR mock the database connection

maybe unit tests for:
- db/db_cursor
- db/db_error

integration test script with and without docker?