# Data and Reproducibility

## Data record

The released data are hosted on IEEE DataPort:

- Title: *Spring-Hall Fingertip Dataset for Contact Localization, Three-Axis Force Measurement, and Magnetic-Disturbance Rejection*
- DOI: `10.21227/kpv-jq50`
- URL: <https://doi.org/10.21227/kpv-jq50>

## Data modules

The DataPort package is organized into force/contact calibration, magnetic-disturbance tests, cross-instance calibration, robotic tasks, figure-source tables, provenance records, model training resources, and selected GUI software.

## Local inspection

`examples/inspect_dataport_export.py` checks a locally extracted package. It confirms the expected module directories, reads selected CSV headers and row counts, and reports selected JSON key summaries. It does not alter the package.

## Reproduction boundary

The repository does not claim a single command that regenerates every paper result. Use the file-level manifests and documentation in the DataPort package to identify the released source table or artifact for a specific analysis. Preserve complete-trial grouping when reproducing trial-level metrics.
