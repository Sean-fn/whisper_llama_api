# Whisper Llama API

# Flask File Processing API

This is a simple Flask application that provides an API for uploading and processing `.wav` files.

## Endpoints

- `POST /api/upload`: Upload a `.wav` file. The file should be included in the request's `file` parameter. Returns a JSON object with a `file_id` that can be used to process the file.

- `GET /api/process/<file_id>`: Process the file with the given `file_id`. The processing logic is not yet implemented.

## Setup

1. Clone the repository.
2. Install the requirements with `pip install -r requirements.txt`.
3. Run the application with `flask run`.

## Configuration

The application expects the following environment variables:

- `UPLOAD_FOLDER`: The path to the folder where uploaded files should be stored. This should be an absolute path.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)