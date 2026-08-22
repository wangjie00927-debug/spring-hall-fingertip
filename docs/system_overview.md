# System Overview

## Measurement path

```text
Mechanical contact
  -> compliant Spring-Hall fingertip deformation
  -> four tri-axis Hall observations
  -> adjacent background and excitation-on measurements
  -> phase correction and differential observation
  -> causal force/contact reconstruction
  -> three-axis force and prescribed contact-location outputs
```

The research prototype uses a titanium-alloy spring, a flux-guiding sleeve, an excitation coil, and four MLX90393 tri-axis Hall sensors. The released dataset describes 12-channel Hall observations, force labels or estimates, contact state, and five prescribed contact anchors.

## Public resource split

```text
GitHub
  -> overview, scope, local inspection example, and tests

IEEE DataPort
  -> released experimental data, paper-evidence tables,
     training feature cache, model artifact, and selected software
```

This separation avoids duplicating large research data and keeps the first source repository small enough to review file by file.
