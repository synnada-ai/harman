# Releases

This folder contains information about all currently released Mithril versions. You can check what has changed in each release in this folder.


## Release Checklist

The person responsible for the upcoming release of Mithril should follow this checklist:

- [ ] Check that all examples run without issues.
- [ ] Ensure that all README models run without issues.
- [ ] Re-check all newly added features and ensure they are well-tested.
- [ ] Verify that the version number is correct.
- [ ] Run speed benchmarks. Ensure that pure framework models are not significantly faster than Mithril models.
- [ ] Run `cProfile` in the library and, if possible, compare it with the previous release.
- [ ] Verify all distributions in the release, ensuring that all tests pass.
