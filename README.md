# pawlessprint

pawlessprint is a webserver running an API that takes in an encoded facial image, identifies a user, and returns the user's associated cloud printing directory. It has the following endpoints:

### Login (POST)

Login requires a file upload. Upon recieving the login POST request at `login/` with the encoded facial image provided the backend collects all files from the AWS s3 bucket with the prefix `face/` and runs the facial recognition software on this directory of faces. The filename of the matching face `face/[uni]` provides the UNI is contained in the response:

`('uni')`

### Files (GET)

A GET request to the endpoint `files/<uni>/` will return all files associated with the provided uni.

### File Remove (POST)

File Remove requires a single argument of the form `'(filename)'` which will follow the convention `('[uni]/[actual filename]')` corresponding to a file on the AWS s3 bucket. The file is removed from the bucket.

### File Add (POST)

File Add requires a file upload. The file is added to the s3 bucket. The filename should be `'[uni]/[actual filename]'` by convention for the bucket.
