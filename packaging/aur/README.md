# APOD Fetch AUR package

This directory contains the AUR package recipe for the development version of
APOD Fetch. The application source stays in `src/apodfetch/` at the repository
root. AUR uses a separate Git repository containing this directory's
`PKGBUILD`, `.SRCINFO`, and `LICENSE` files.

The `LICENSE` in this directory covers only the AUR packaging files. The
application uses MIT, with its license in the repository root and its license
identifier in the `PKGBUILD` metadata.

To build the package locally, run `makepkg -s` in this directory. The recipe
clones the published GitHub repository, builds a Python wheel, and installs it
into an Arch package. Commit and push the root `LICENSE` and metadata changes
before building; the recipe does not package uncommitted local changes.

Before submitting an update to AUR, run `makepkg --printsrcinfo > .SRCINFO`
and commit the changed packaging files to the AUR repository.
