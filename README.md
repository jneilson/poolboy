![enter image description here](https://csplib.io/images/pb.jpg)

# Poolboy

A simple ChatGPT-genrated Python and Flask script that takes a single Blackboard Ultra question pool (bank) and performs the following fixes:

1. Replace any instances of "Multiple Answer" with "Multiple Choice"
2. Within the <code>&lt;resprocessing&gt;&lt;respcondition title="correct"&gt;</code> section of each question, remove any answer wrapped in a <code>&lt;not&gt;</code> tag
3. Removes any remaining <code>&lt;and&gt;</code> tags

*1. Replace any instances of "Multiple Answer" with "Multiple Choice"*
This script assumes your question pool contains only multiple-choice questions. Blackboard Ultra has a bug where multiple-choice questions are exported as multiple-answer. This script will update all multiple-answer questions to multiple-choice, including any that you intend to be multiple-answer. You'll need to fix these manually.

*2. Within the <code>&lt;resprocessing&gt;&lt;respcondition title="correct"&gt;</code> section of each question, remove any answer wrapped in a <code>&lt;not&gt;</code> tag*
Blackboard Ultra has a bug where the correct and incorrect answers are not formatted correctly in the export file. The incorrect formatting looks like this:

				<resprocessing scoremodel="SumOfScores">
					<outcomes>
						<decvar varname="SCORE" vartype="Decimal" defaultval="0" minvalue="0" maxvalue="10.00000"/>
					</outcomes>
					<respcondition title="correct">
						<conditionvar>
							<and>
								<not>
									<varequal respident="response" case="No">7e3d0c716b2a4e3db69edfe18aa99c52</varequal>
								</not>
								<not>
									<varequal respident="response" case="No">a908b0aa7a984638bee6cbc813f8d8d1</varequal>
								</not>
								<not>
									<varequal respident="response" case="No">cb2f663c223b4d44a6857b4913abb96a</varequal>
								</not>
								<varequal respident="response" case="No">76df1c9c9e8d418188a322b365f3f1a1</varequal>
							</and>
						</conditionvar>
						<setvar variablename="SCORE" action="Set">SCORE.max</setvar>
						<setvar variablename="single_correct_answer" action="Set">true</setvar>
						<displayfeedback linkrefid="correct" feedbacktype="Response"/>
					</respcondition>
					<respcondition title="incorrect">
						<conditionvar>
							<other/>
						</conditionvar>
						<setvar variablename="SCORE" action="Set">0</setvar>
						<displayfeedback linkrefid="incorrect" feedbacktype="Response"/>
					</respcondition>
					<respcondition>
						<conditionvar>
							<varequal respident="7e3d0c716b2a4e3db69edfe18aa99c52" case="No"/>
						</conditionvar>
						<setvar variablename="SCORE" action="Set">0</setvar>
					</respcondition>
					<respcondition>
						<conditionvar>
							<varequal respident="a908b0aa7a984638bee6cbc813f8d8d1" case="No"/>
						</conditionvar>
						<setvar variablename="SCORE" action="Set">0</setvar>
					</respcondition>
					<respcondition>
						<conditionvar>
							<varequal respident="cb2f663c223b4d44a6857b4913abb96a" case="No"/>
						</conditionvar>
						<setvar variablename="SCORE" action="Set">0</setvar>
					</respcondition>
					<respcondition>
						<conditionvar>
							<varequal respident="76df1c9c9e8d418188a322b365f3f1a1" case="No"/>
						</conditionvar>
						<setvar variablename="SCORE" action="Set">0</setvar>
					</respcondition>
				</resprocessing>


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
