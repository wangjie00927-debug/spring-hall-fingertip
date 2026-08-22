# Spring-Hall Fingertip

Open research resources for an excitation-referenced Spring-Hall tactile sensing project involving three-axis force measurement and contact localization.

## Overview

The project studies a research-oriented compliant fingertip instrument that observes deformation through four tri-axis Hall sensors. Adjacent background and excitation-on observations provide excitation-referenced differential measurements for three-axis force and contact-related reconstruction. This repository provides public orientation, documentation, and a validated inspection utility; the associated experimental data and result-source artifacts are distributed separately through IEEE DataPort.

## Repository Scope

- A concise system and repository overview.
- Data and reproducibility documentation linked to the IEEE DataPort dataset.
- A validated local DataPort inspection utility requiring no third-party Python packages.
- Unit tests for the inspection utility.
- Architecture-level scope documentation for hardware, firmware, software, and calibration resources.

## Not Included

Experimental data are hosted separately on IEEE DataPort. Historical development code, large model artifacts, hardware-specific runtime configurations, CAD, PCB, manufacturing files, firmware implementation, and unpublished project materials are not part of this release.

The repository intentionally focuses on public documentation, reproducibility guidance, and a validated dataset-inspection utility.

## Repository Structure

```text
spring-hall-fingertip/
|-- README.md
|-- CITATION.cff
|-- LICENSE
|-- LICENSE_SCOPE.md
|-- NOTICE.md
|-- docs/
|-- hardware/
|-- firmware/
|-- software/
|-- calibration/
|-- examples/
`-- tests/
```

## Dataset

The experimental dataset is not duplicated in this repository.

**Spring-Hall Fingertip Dataset for Contact Localization, Three-Axis Force Measurement, and Magnetic-Disturbance Rejection**

- DOI: `10.21227/kpv-jq50`
- URL: <https://doi.org/10.21227/kpv-jq50>

The DataPort record contains the released paper-evidence tables, training feature cache, model artifact, selected software, metadata, and documentation.

## Quick Start

Requirements: Python 3.10 or later. The inspection example uses only the Python standard library.

After downloading and extracting the DataPort package:

```powershell
python examples/inspect_dataport_export.py --package PATH_TO_EXTRACTED_DATAPORT_PACKAGE
```

Run the local test suite with:

```powershell
python -m unittest discover -s tests -v
```

The inspection utility reads and validates selected released DataPort files. It reports expected module directories, selected CSV row counts, and JSON key summaries. It does not download data, perform model training, or reproduce the complete experimental pipeline.

## Hardware

The repository provides architecture-level documentation only. No CAD, PCB, manufacturing, or hardware-design source files are included. See [`hardware/README.md`](hardware/README.md).

## Firmware

No firmware implementation is distributed in this release. The firmware section describes only the public scope and its relationship to the measurement system. See [`firmware/README.md`](firmware/README.md).

## Software

The public software scope consists of the validated IEEE DataPort inspection utility and its tests. See [`software/README.md`](software/README.md).

## Calibration

This repository documents how to locate and interpret released calibration evidence on IEEE DataPort. It does not distribute a complete calibration implementation. See [`calibration/README.md`](calibration/README.md).

## Reproducibility

Use this repository together with the IEEE DataPort record. GitHub provides orientation, documentation, and a lightweight validated inspection utility. IEEE DataPort provides the released experimental data, result-source tables, and associated artifacts. See [`docs/data_and_reproducibility.md`](docs/data_and_reproducibility.md).

## Known Limitations

This repository is a research resource rather than a production software package. Hardware-dependent control modules and manufacturing sources are not distributed. No one-command end-to-end reproduction of the physical experiments is claimed. See [`docs/known_limitations.md`](docs/known_limitations.md).

## Citation

If you use the released experimental data or reproduce analyses based on the published dataset, please cite the associated IEEE DataPort dataset. For machine-readable citation metadata, see [`CITATION.cff`](CITATION.cff). GitHub exposes repository citation metadata from this file.

## License

Copyright (C) 2026 Wangjie Ma.

Source code under `examples/` and `tests/` is licensed under `GPL-3.0-only`. Original documentation and original repository graphics are licensed under `CC-BY-SA-4.0`. See `LICENSE` and [`LICENSE_SCOPE.md`](LICENSE_SCOPE.md) for details.

The IEEE DataPort dataset is distributed separately and is governed by the license and terms of its DataPort record.

## Contact

Corresponding contact published with the project materials:

Xin Meng<br>
School of Electrical and Electronic Engineering, Shanghai Institute of Technology<br>
E-mail: `mengxinlzy936@163.com`
