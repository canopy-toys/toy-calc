# Changelog

## Unreleased

- Division by zero now exits with status 2 (was 1), so scripts can tell it apart from a bad number.

## 0.1.0

- `add`, `sub`, `mul`, and `div` subcommands.
- `--precision` to round the result to a number of decimal places.
