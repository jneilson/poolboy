![enter image description here](https://csplib.io/images/pb.jpg)

# Poolboy

A simple ChatGPT-genrated Python and Flask script that takes a single Blackboard Ultra question pool (bank) and performs the following fixes:

 - Replaces any instances of "Multiple Answer" with "Multiple Choice"
 - Within the <code>&lt;resprocessing&gt;&lt;respcondition title="correct"&gt;</code> section of each question, removes any answer wrapped in a <code>&lt;not&gt;</code> tag
 - Removes any remaining <code>&lt;and&gt;</code> tags

## Setup
### Install dependencies
You'll need Python and Flask installed on your system for this to work. These instructions assume you're running Windows. Run the following commands in Powershell:

     Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
This command will set the execution policy to allow the execution of locally created scripts.

    .\install_python_flask.ps1
This command will check if Python and Flask are already installed. If they're not installed, it will install them.

    Set-ExecutionPolicy Restricted -Scope CurrentUser -Force
This command resets the execution policy back to a more restrictive setting.
You should now be able to run Poolboy

### Setup Poolboy
Create a directory with the following files:

 - `poolboy.py`
 - `/templates` directory
	 - `index.html`
	 - `result.html`

## Run Poolboy
In Command Prompt, navigate to the directory you created. [Here's](https://www.howtogeek.com/659411/how-to-change-directories-in-command-prompt-on-windows-10/) how to navigate in Command Prompt.

Run the following:

    python poolboy.py

This will launch the script and a Flask web app.
In your browser, go to http://127.0.0.1:5000
You will be taken to the web interface for the Poolboy app.

When your finished, go back to Command Prompt and type `CTRL` + `C` to quit the server/app.
