# Scripts

The scripts are written in Python 3.6. To run the scripts, you may also need
to install the dependencies specified in
[requirements.txt](../requirements.txt).

## Preprocess

### Usage

```
$ python preprocess.py <InputFile> <OutputFile>
```

- Arguments:
  - `InputFile`: (required) the csv file to process
  - `OutputFile`: (required) the csv file for outputting result

## Predict

### Usage

```
$ python predict.py <DatabaseFile> [ShingleLength] [Text]
```

- Arguments
  - `DatabaseFile`: (required) the database file in csv format
  - `ShingleLength`: (optional) the shingle length filter. If provided,
    only shingles with specified length are used. If omitted, all size
    of shingles are used, and take the average as the result.
  - `Text`: (optional) the text to predict. If omitted, users will
    enter the interactive mode.
