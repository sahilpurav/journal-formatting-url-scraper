# Journal Formatting URL Scraper
Are you into researcher / author service industry? Do you help author to publish their paper? If yes, then you must have already known with the pain to grab the formatting URLs considering the huge number of Journals we've in the world.

This small python based application is existsted to solve this issue.

Every Journal has it's own formatting style and Authors around the world have had a hard time to find the formatting guidelines for their same research.

## Who should use this repository?
Anyone who desired to find the formatting URL from the list of journals.

## What is pre-requisite?
- Application uses python 3
- You need to have pipenv installed on your machine
- Any operating system
- This application assumes that, you've list of Journals in CSV format. Sample is already included in the root folder ("sample.csv")

In case you want to try out before using it in real world, application also supports fetching of formatting Url for single author.

## How to use?
Assuming you've installed pipenv and python3 use following commands to get started:

### Clone the repository
```
git clone git@github.com:sahilpurav/journal-formatting-url-scraper.git
```

### Install dependancies with pipenv
```
pipenv --three
```

### Spawn the process with shell
```
pipenv shell
```

### Run the application
```
python3 scraper.py
```

### Answer following questions
#### Enter the Journal name or file path (CSV Only)
- If you want to test this application just pass the full journal name
- If you've file with list of journal names then pass the full path

#### Enter the Output file name (CSV Only)
- Output path of the file. You can include / exclude the file extension. Currently application supports CSV format only.

> One above commands are executed, it may take a while to scrap all the data from Google and at the end, it will generate a file inside **dist** folder with the name mentioned in the *output file name* question.

## Issues
Raise an issue in GitHub, and I will look at it on weekly basis.

## Contribution
If you want to contribute, please feel free to raise a PR.
