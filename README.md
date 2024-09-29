# 40Thiefs
Python Implementation of the "40 Ladrões" game described  here: https://www.youtube.com/watch?feature=shared&amp;v=ghporyNawck

Instructions to run the game with windows powershell:

1. Navigate to src  (cd src)
2. Create a virtual environment (python -m venv virtualenv)
3. Activate the virtualenv (.\virtualenv\bin\Activate.ps1) (if you don't have the permission to run scripts in powershell set it executing the "Set-ExecutionPolicy RemoteSigned" command.)
3. Install the requirements (pip install -r ../requirements.txt) (no requirements for this first version, you can ignore this step)
4. Go back one level (cd..)
5. Run the game (python src/forty_thiefs.py)