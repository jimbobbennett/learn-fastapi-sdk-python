python3 -m venv .venv
source .venv/bin/activate
pip3 install build
python3 -m build --outdir dist ../ 
pip3 install dist/exciting_soda-200.40.40-dev-py3-none-any.whl