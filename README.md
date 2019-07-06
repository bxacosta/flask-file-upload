# Flask simple file upload example
Python script to upload file using flask

## Usage
This application exposes a enpoint:

```
POST http://127.0.0.1:8080/file
```

You can try this application using `Postman` and send a `form-data` in the `body` with a key named `file` or in a `<form>` tag is marked with `enctype=multipart/form-data` and an `<input type=file>` is placed in that form.

## References
* [Uploading Files](http://flask.pocoo.org/docs/1.0/patterns/fileuploads)
* [Request.files](http://flask.pocoo.org/docs/1.0/api/#flask.Request.files)
* [FileStorage](https://werkzeug.palletsprojects.com/en/0.15.x/datastructures/#werkzeug.datastructures.FileStorage)