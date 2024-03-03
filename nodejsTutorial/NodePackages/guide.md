# npm package manager in JS

- `npm init`
- `npm init --yes`

## Semantic Versioning

- X.Y.Z
- Where X is a major, Y is a minor and Z is a patch.
- Semantic versioning always starts with 0.1.0
- 0.Y.Z (a major version of zero) is used for initial development
- When the code is production ready, you increment to version 1.0.0
- Even the simplest of changes has to be done with an increase in the version number.

### Versioning Rules

- When you fix a bug and the code stays backwards compatible you increment the patch version. For example 1.1.1 to 1.1.2.
- When you add new functionality but the code stays backwards compatible, you increment the minor version. You also reset the patch version to zero. For example 1.1.1 to 1.2.0.
- When you make changes and the code is no more backwards compatible,you increment the major version. You also reset the minor and patch version to zero. For example 1.1.1 to 2.0.0.
