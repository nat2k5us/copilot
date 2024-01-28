# My Python Project

This project is a simple dashboard that displays the top 10 processes by CPU usage. The dashboard updates every second.

## Installation

To install the project, you need to have Python 3.6 or later installed on your machine. 

1. Clone the repository:

```
git clone https://github.com/yourusername/my-python-project.git
```

2. Navigate to the project directory:

```
cd my-python-project
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

To run the project, navigate to the `src` directory and run the `main.py` script:

```
cd src
python main.py
```

The dashboard should now be visible and start updating every second.

## Testing

To run the tests, navigate to the `tests` directory and run the `test_process_monitor.py` script:

```
cd tests
python test_process_monitor.py
```

## Dependencies

This project uses the following Python libraries:

- Toga: A Python native, OS native GUI toolkit.
- psutil: A cross-platform library used to access system details and process utilities.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)