# nb2py
---
Dumps marked code cells from a Jupyter notebook into a single .py file.


## Features
---
- Reads a Jupyter Notebook and export marked code cells with the comment `#~` to a single `.py` file.
- Exports a list of cells into a single file (Useful to export markdown cells as a README.md file)

## Dependencies
---
None

## Usage
---
```
import nb2py
nb2py.dump('NB2PY_SOURCE.ipynb','nb2py.py')
nb2py.dump_indices('NB2PY_SOURCE.ipynb','README.md',[3,2])
```

## Credits
Created by Hugo Guillen, 2017.
