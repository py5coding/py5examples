# User environment for peddie JupyterHub

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/2i2c-org/peddie-image/HEAD?urlpath=lab)

This repository specifies the user environment for the [peddie hub](https://peddie.pilot.2i2c.cloud/)
run by [2i2c](https://2i2c.org/).

## Making a change

1. Make a pull request to this repository with your environment changes (edits to
   `environment.yml`, `postBuild`, etc). A bot will post a link to `mybinder.org` that
   can be used to test your new changes! Use it, and make sure things work the way
   you would like. If not, amend the PR until it seems right.

2. Merge the PR. This will kick off a [GitHub Action](https://github.com/2i2c-org/peddie-image/actions)
   to build and push the container image. We use [quay.io](https://quay.io) instead of
   DockerHub, but that shouldn't matter to you. Wait for this action to finish.

3. Go to the [list of image tags](https://quay.io/repository/2i2c/peddie-image?tab=tags), and find
   the tag of the last push. This is *not* the `latest` tag but is usually under it. Use this
   to construct your image name - `quay.io/2i2c/peddie-image:<tag>`.

4. Open the [Configurator](https://peddie.pilot.2i2c.cloud/services/configurator/) for the peddie
   hub (you need to be logged in as an admin). You can also access it from the hub control panel,
   under *Services* in the top bar. Make a note of the current image name there, and
   put the image tag you constructed in the last step into the `User docker
   image` text box, and click `Submit`. This is alpha level software, so there
   is no 'has it saved' indicator yet :) You can find more information about the Configurator
   [here](https://pilot.2i2c.org/en/latest/admin/howto/configurator.html)

5. Test the new image by starting a new user server! If you already had one running, you need to
   stop and start it again to test.

6. If you find new issues, you can revert back to the previous image by entering the old image name,
   back in the JupyterHub Configurator. This will be streamlined in the future.