# TODO

- Fix tests
- change config in following to values set by docker:
    - tests/db/db_connection.py
    - tests/db/adapters/product_adapter.py

## Testing TODO

unit tests for:
- [X] db/db_item_descriptor
- [X] models/products module
- [X/] db/db_connection --- has some tests, dont think more are relevant?
- [/] db/adapters/product_adapter --- WIP
- [] db/db_migrator
- [] webserver/api

options: create new database exclusively for testing, OR mock the database connection

maybe unit tests for:

- db/db_cursor
- db/db_error

integration test script with and without docker?
