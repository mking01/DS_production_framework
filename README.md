# Coronavirus Predictions - Production DS Project

### Technical Skills Goal
The goal of this project is to practice coding for data science production projects.  This includes:
- building a framework
- connecting framework files and parts to one another (e.g. import configs into main .py script)
- constructing modularized code
- using pipelines to process and model data for simplicity and maintainability
- creating unit tests
- using classes / OOP to manage and manipulate data

### Project Goal
This project aims to predict whether patients being tested for COVID-19 should be quarantined or released based on their interaction patterns, health indicators, and travel patterns.

### Data
Data for this project is pulled from an open source dataset provided by the Korean Center for Disease Control.  It is available on Github here: https://github.com/jihoo-kim/Coronavirus-Dataset.

### Folders
- data: stores all data files (in real life, data would likely be pulled in through a cloud or database connection)
- notebooks: stores all notebooks used for analysis and data discovery
- src: all source code used for production
- src / scripts:  all production .py scripts
- src / configs: all changeable components for the project (e.g. file paths)
- src / lib: contains module created for the project
- tests: contains all tests used to check code and data for the project, such as unit tests
- documentation: contains all notes about the project, the code, and the problem context

### Resources
Modeling disease transmission: https://systems.jhu.edu/research/public-health/ncov-model-2/
