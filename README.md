# mbaacc-bracket-data-analytics

Python script to run analytics on CSV data for MBAACC brackets

## Usage

```bash
./mbda path/to/your/file.csv [output_dir]
```

- `path/to/your/file.csv`: Path to your input CSV file.
- `[output_dir]` (optional): Name of the output directory for CSV results. Defaults to `csv-output` if not provided.

The CSV file passed in should have exported data from the "MBAACC Netplay Bracket Stats" spreadsheet from Google Sheets. Ask enpicie for link if needed.

## Output

If not given a distinct `output_dir` name, running `mbda` will output al filtered data in a directory with the name format `<date>-csv-output` where the `<date>` is the current date in format `yyyymmdd` to distinguish the output.

Data is split into separate CSV files for how it is filtered.
