# datafun-07-ml
```
git push
```
## Project Setup (Windows / PowerShell, loacl computer C:)

 Clone to local: Open a **machine terminal** in your **`Repos`** folder and clone your new repo.

  ```shell
  git clone https://github.com/tmims71-ctrl/datafun-07-ml
  ```

4. Open project in VS Code: Change directory into the repo and open the project in VS Code by running `code .` ("code dot"):

  ```shell
  cd datafun-04-notebooks
  code .
  ```

5. Install recommended extensions.

   - When VS Code opens, accept the Extension Recommendations (click **`Install All`** or similar when asked).

6. Set up a project Python environment (managed by `uv`) and align VS Code with it.

   - Use VS Code menu option `Terminal` / `New Terminal` to open a **VS Code terminal** in the root project folder.
   - Run the following commands, one at a time, hitting ENTER after each:

    ```shell
    uv self update
    uv python pin 3.14
    uv sync --extra dev --extra docs --upgrade
    ```

If asked: "We noticed a new environment has been created. Do you want to select it for the workspace folder?" Click **"Yes"**.

If successful, you'll see a new `.venv` folder appear in the root project folder.

Optional (recommended): install and run pre-commit checks (repeat the git `add` and `commit` twice if needed):

```shell
uvx pre-commit install
git add -A
uvx pre-commit run --all-files
git add -A
uvx pre-commit run --all-files
```
pip install -r requirements.txt

## Requirements

- jupyterlab

- numpy

- pandas

- pyarrow

- matplotlib

- seaborn

- scipy

## Reminders Notes

- Default README.md created with creation of repostory

- Project cloned to local computer C:\Repos.

- Added .gitignore from a list recommended by Github, selected one compatible with Python

- Created and activated a local virtual environment (.venv).

- Installed required packages.

- Added requirements.txt
