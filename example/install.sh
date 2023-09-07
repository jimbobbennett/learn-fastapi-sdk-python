python -m venv .venv
source .venv/bin/activate
pip install build
python -m build --outdir dist ../ 
pip install dist/exciting_soda-200.40.40-dev-py3-none-any.whl
